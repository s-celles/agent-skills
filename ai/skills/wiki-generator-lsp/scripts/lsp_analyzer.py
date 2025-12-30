#!/usr/bin/env python3
"""
LSP-based codebase analyzer for documentation generation.
Extracts symbols, references, call hierarchies, and type information.
"""

import json
import subprocess
import sys
import os
import re
import time
import socket
from pathlib import Path
from dataclasses import dataclass, asdict, field
from typing import Optional
import argparse

# ============================================================================
# Data Structures
# ============================================================================

@dataclass
class Symbol:
    name: str
    kind: str  # class, function, method, variable, interface, etc.
    file: str
    line: int
    end_line: int
    detail: str = ""
    children: list = field(default_factory=list)
    references: list = field(default_factory=list)
    calls: list = field(default_factory=list)
    called_by: list = field(default_factory=list)
    docstring: str = ""

@dataclass
class FileInfo:
    path: str
    language: str
    symbols: list = field(default_factory=list)
    imports: list = field(default_factory=list)
    exports: list = field(default_factory=list)

@dataclass
class ProjectAnalysis:
    name: str
    root: str
    language: str
    framework: str = ""
    entry_points: list = field(default_factory=list)
    files: list = field(default_factory=list)
    dependencies: dict = field(default_factory=dict)
    call_graph: dict = field(default_factory=dict)

# ============================================================================
# Project Detection
# ============================================================================

def detect_project_type(root: Path) -> tuple[str, str, str]:
    """Detect primary language, LSP server, and framework."""
    
    # TypeScript/JavaScript
    if (root / "package.json").exists():
        pkg = json.loads((root / "package.json").read_text())
        deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
        
        framework = ""
        if "next" in deps: framework = "Next.js"
        elif "react" in deps: framework = "React"
        elif "vue" in deps: framework = "Vue"
        elif "express" in deps: framework = "Express"
        elif "fastify" in deps: framework = "Fastify"
        
        if "typescript" in deps or (root / "tsconfig.json").exists():
            return "typescript", "typescript-language-server", framework
        return "javascript", "typescript-language-server", framework
    
    # Python
    if any((root / f).exists() for f in ["pyproject.toml", "setup.py", "requirements.txt"]):
        framework = ""
        for f in root.rglob("*.py"):
            content = f.read_text(errors="ignore")
            if "from fastapi" in content or "import fastapi" in content:
                framework = "FastAPI"; break
            if "from django" in content or "import django" in content:
                framework = "Django"; break
            if "from flask" in content or "import flask" in content:
                framework = "Flask"; break
        return "python", "pylsp", framework
    
    # Go
    if (root / "go.mod").exists():
        return "go", "gopls", ""
    
    # Rust
    if (root / "Cargo.toml").exists():
        return "rust", "rust-analyzer", ""
    
    # Java
    if (root / "pom.xml").exists() or (root / "build.gradle").exists():
        return "java", "jdtls", ""
    
    # C/C++
    if (root / "CMakeLists.txt").exists() or (root / "Makefile").exists():
        return "cpp", "clangd", ""
    
    return "unknown", "", ""

# ============================================================================
# LSP Client (Simplified)
# ============================================================================

class LSPClient:
    """Minimal LSP client for code analysis."""
    
    def __init__(self, server_cmd: list, root: Path):
        self.root = root
        self.request_id = 0
        self.process = None
        self.server_cmd = server_cmd
        
    def start(self) -> bool:
        """Start the LSP server process."""
        try:
            self.process = subprocess.Popen(
                self.server_cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=str(self.root)
            )
            return self._initialize()
        except FileNotFoundError:
            return False
    
    def stop(self):
        """Shutdown the LSP server."""
        if self.process:
            self._send_notification("shutdown", {})
            self._send_notification("exit", {})
            self.process.terminate()
    
    def _send_request(self, method: str, params: dict) -> Optional[dict]:
        """Send a JSON-RPC request and get response."""
        self.request_id += 1
        message = {
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": method,
            "params": params
        }
        return self._communicate(message)
    
    def _send_notification(self, method: str, params: dict):
        """Send a JSON-RPC notification (no response expected)."""
        message = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params
        }
        self._write_message(message)
    
    def _write_message(self, message: dict):
        """Write a message to the LSP server."""
        content = json.dumps(message)
        header = f"Content-Length: {len(content)}\r\n\r\n"
        self.process.stdin.write(header.encode() + content.encode())
        self.process.stdin.flush()
    
    def _read_message(self) -> Optional[dict]:
        """Read a message from the LSP server."""
        try:
            # Read headers
            headers = {}
            while True:
                line = self.process.stdout.readline().decode()
                if line == "\r\n":
                    break
                if ":" in line:
                    key, value = line.split(":", 1)
                    headers[key.strip()] = value.strip()
            
            # Read content
            length = int(headers.get("Content-Length", 0))
            if length:
                content = self.process.stdout.read(length).decode()
                return json.loads(content)
        except Exception:
            pass
        return None
    
    def _communicate(self, message: dict) -> Optional[dict]:
        """Send request and wait for response."""
        self._write_message(message)
        
        # Wait for response with matching ID
        start = time.time()
        while time.time() - start < 10:  # 10s timeout
            response = self._read_message()
            if response and response.get("id") == message["id"]:
                return response.get("result")
        return None
    
    def _initialize(self) -> bool:
        """Initialize the LSP connection."""
        result = self._send_request("initialize", {
            "processId": os.getpid(),
            "rootUri": f"file://{self.root}",
            "capabilities": {
                "textDocument": {
                    "documentSymbol": {"hierarchicalDocumentSymbolSupport": True},
                    "definition": {"linkSupport": True},
                    "references": {},
                    "hover": {"contentFormat": ["markdown", "plaintext"]},
                    "callHierarchy": {}
                }
            }
        })
        if result:
            self._send_notification("initialized", {})
            return True
        return False
    
    def open_file(self, file_path: Path, language: str):
        """Notify server that a file is open."""
        self._send_notification("textDocument/didOpen", {
            "textDocument": {
                "uri": f"file://{file_path}",
                "languageId": language,
                "version": 1,
                "text": file_path.read_text(errors="ignore")
            }
        })
    
    def get_document_symbols(self, file_path: Path) -> list:
        """Get all symbols in a document."""
        result = self._send_request("textDocument/documentSymbol", {
            "textDocument": {"uri": f"file://{file_path}"}
        })
        return result or []
    
    def get_references(self, file_path: Path, line: int, char: int) -> list:
        """Get all references to a symbol."""
        result = self._send_request("textDocument/references", {
            "textDocument": {"uri": f"file://{file_path}"},
            "position": {"line": line, "character": char},
            "context": {"includeDeclaration": False}
        })
        return result or []
    
    def get_hover(self, file_path: Path, line: int, char: int) -> Optional[str]:
        """Get hover information (type info, docs)."""
        result = self._send_request("textDocument/hover", {
            "textDocument": {"uri": f"file://{file_path}"},
            "position": {"line": line, "character": char}
        })
        if result and "contents" in result:
            contents = result["contents"]
            if isinstance(contents, str):
                return contents
            if isinstance(contents, dict):
                return contents.get("value", "")
            if isinstance(contents, list):
                return "\n".join(c.get("value", c) if isinstance(c, dict) else c for c in contents)
        return None

# ============================================================================
# Fallback Analyzers (No LSP)
# ============================================================================

def analyze_python_file(file_path: Path) -> FileInfo:
    """Analyze Python file using AST."""
    import ast
    
    info = FileInfo(path=str(file_path), language="python")
    content = file_path.read_text(errors="ignore")
    
    try:
        tree = ast.parse(content)
    except SyntaxError:
        return info
    
    for node in ast.walk(tree):
        # Imports
        if isinstance(node, ast.Import):
            for alias in node.names:
                info.imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                info.imports.append(node.module)
        
        # Classes
        elif isinstance(node, ast.ClassDef):
            sym = Symbol(
                name=node.name,
                kind="class",
                file=str(file_path),
                line=node.lineno,
                end_line=node.end_lineno or node.lineno,
                docstring=ast.get_docstring(node) or ""
            )
            # Methods
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    sym.children.append(Symbol(
                        name=item.name,
                        kind="method",
                        file=str(file_path),
                        line=item.lineno,
                        end_line=item.end_lineno or item.lineno,
                        docstring=ast.get_docstring(item) or ""
                    ))
            info.symbols.append(sym)
        
        # Functions (top-level)
        elif isinstance(node, ast.FunctionDef) and not any(
            isinstance(p, ast.ClassDef) for p in ast.walk(tree) 
            if hasattr(p, 'body') and node in getattr(p, 'body', [])
        ):
            info.symbols.append(Symbol(
                name=node.name,
                kind="function",
                file=str(file_path),
                line=node.lineno,
                end_line=node.end_lineno or node.lineno,
                docstring=ast.get_docstring(node) or ""
            ))
    
    return info

def analyze_typescript_file(file_path: Path) -> FileInfo:
    """Analyze TypeScript/JavaScript file using regex patterns."""
    info = FileInfo(path=str(file_path), language="typescript")
    content = file_path.read_text(errors="ignore")
    lines = content.split("\n")
    
    # Imports
    for match in re.finditer(r'import\s+.*?\s+from\s+[\'"](.+?)[\'"]', content):
        info.imports.append(match.group(1))
    
    # Exports
    for match in re.finditer(r'export\s+(?:default\s+)?(?:class|function|const|interface|type)\s+(\w+)', content):
        info.exports.append(match.group(1))
    
    # Classes
    for match in re.finditer(r'(?:export\s+)?class\s+(\w+)', content):
        line_num = content[:match.start()].count("\n") + 1
        info.symbols.append(Symbol(
            name=match.group(1),
            kind="class",
            file=str(file_path),
            line=line_num,
            end_line=line_num  # Simplified
        ))
    
    # Functions
    for match in re.finditer(r'(?:export\s+)?(?:async\s+)?function\s+(\w+)', content):
        line_num = content[:match.start()].count("\n") + 1
        info.symbols.append(Symbol(
            name=match.group(1),
            kind="function",
            file=str(file_path),
            line=line_num,
            end_line=line_num
        ))
    
    # Arrow functions assigned to const
    for match in re.finditer(r'(?:export\s+)?const\s+(\w+)\s*=\s*(?:async\s+)?\([^)]*\)\s*(?::\s*\w+)?\s*=>', content):
        line_num = content[:match.start()].count("\n") + 1
        info.symbols.append(Symbol(
            name=match.group(1),
            kind="function",
            file=str(file_path),
            line=line_num,
            end_line=line_num
        ))
    
    # Interfaces
    for match in re.finditer(r'(?:export\s+)?interface\s+(\w+)', content):
        line_num = content[:match.start()].count("\n") + 1
        info.symbols.append(Symbol(
            name=match.group(1),
            kind="interface",
            file=str(file_path),
            line=line_num,
            end_line=line_num
        ))
    
    # Types
    for match in re.finditer(r'(?:export\s+)?type\s+(\w+)', content):
        line_num = content[:match.start()].count("\n") + 1
        info.symbols.append(Symbol(
            name=match.group(1),
            kind="type",
            file=str(file_path),
            line=line_num,
            end_line=line_num
        ))
    
    return info

def analyze_go_file(file_path: Path) -> FileInfo:
    """Analyze Go file using regex patterns."""
    info = FileInfo(path=str(file_path), language="go")
    content = file_path.read_text(errors="ignore")
    
    # Imports
    for match in re.finditer(r'import\s+"([^"]+)"', content):
        info.imports.append(match.group(1))
    for match in re.finditer(r'import\s+\((.*?)\)', content, re.DOTALL):
        for line in match.group(1).split("\n"):
            if '"' in line:
                pkg = re.search(r'"([^"]+)"', line)
                if pkg:
                    info.imports.append(pkg.group(1))
    
    # Functions
    for match in re.finditer(r'func\s+(\w+)\s*\(', content):
        line_num = content[:match.start()].count("\n") + 1
        info.symbols.append(Symbol(
            name=match.group(1),
            kind="function",
            file=str(file_path),
            line=line_num,
            end_line=line_num
        ))
    
    # Methods
    for match in re.finditer(r'func\s+\([^)]+\)\s+(\w+)\s*\(', content):
        line_num = content[:match.start()].count("\n") + 1
        info.symbols.append(Symbol(
            name=match.group(1),
            kind="method",
            file=str(file_path),
            line=line_num,
            end_line=line_num
        ))
    
    # Structs
    for match in re.finditer(r'type\s+(\w+)\s+struct', content):
        line_num = content[:match.start()].count("\n") + 1
        info.symbols.append(Symbol(
            name=match.group(1),
            kind="struct",
            file=str(file_path),
            line=line_num,
            end_line=line_num
        ))
    
    # Interfaces
    for match in re.finditer(r'type\s+(\w+)\s+interface', content):
        line_num = content[:match.start()].count("\n") + 1
        info.symbols.append(Symbol(
            name=match.group(1),
            kind="interface",
            file=str(file_path),
            line=line_num,
            end_line=line_num
        ))
    
    return info

# ============================================================================
# Main Analyzer
# ============================================================================

EXCLUDE_DIRS = {
    "node_modules", "venv", ".venv", "__pycache__", ".git", 
    "dist", "build", ".next", "target", "vendor", ".idea", ".vscode"
}

LANGUAGE_EXTENSIONS = {
    "python": [".py"],
    "typescript": [".ts", ".tsx"],
    "javascript": [".js", ".jsx", ".mjs"],
    "go": [".go"],
    "rust": [".rs"],
    "java": [".java"],
    "cpp": [".cpp", ".hpp", ".c", ".h", ".cc", ".cxx"]
}

def find_source_files(root: Path, language: str) -> list[Path]:
    """Find all source files for the given language."""
    extensions = LANGUAGE_EXTENSIONS.get(language, [])
    if language == "typescript":
        extensions = LANGUAGE_EXTENSIONS["typescript"] + LANGUAGE_EXTENSIONS["javascript"]
    
    files = []
    for ext in extensions:
        for f in root.rglob(f"*{ext}"):
            if not any(ex in f.parts for ex in EXCLUDE_DIRS):
                files.append(f)
    return sorted(files)

def find_entry_points(root: Path, language: str) -> list[str]:
    """Identify likely entry points."""
    entry_patterns = {
        "python": ["main.py", "app.py", "__main__.py", "cli.py", "manage.py"],
        "typescript": ["index.ts", "main.ts", "app.ts", "server.ts", "index.tsx", "App.tsx"],
        "javascript": ["index.js", "main.js", "app.js", "server.js", "index.jsx", "App.jsx"],
        "go": ["main.go", "cmd/main.go"],
        "rust": ["main.rs", "lib.rs"],
        "java": ["Main.java", "Application.java"],
        "cpp": ["main.cpp", "main.c"]
    }
    
    patterns = entry_patterns.get(language, [])
    entries = []
    
    for pattern in patterns:
        for f in root.rglob(pattern):
            if not any(ex in f.parts for ex in EXCLUDE_DIRS):
                entries.append(str(f.relative_to(root)))
    
    return entries

def get_lsp_command(server: str) -> list[str]:
    """Get the command to start an LSP server."""
    commands = {
        "typescript-language-server": ["typescript-language-server", "--stdio"],
        "pylsp": ["pylsp"],
        "gopls": ["gopls", "serve"],
        "rust-analyzer": ["rust-analyzer"],
        "clangd": ["clangd"],
        "jdtls": ["jdtls"]
    }
    return commands.get(server, [])

def analyze_with_lsp(root: Path, language: str, server: str) -> list[FileInfo]:
    """Analyze project using LSP server."""
    cmd = get_lsp_command(server)
    if not cmd:
        return []
    
    client = LSPClient(cmd, root)
    if not client.start():
        print(f"[WARN] Could not start LSP server {server}, falling back to regex", file=sys.stderr)
        return []
    
    files = []
    try:
        source_files = find_source_files(root, language)
        for file_path in source_files:
            info = FileInfo(path=str(file_path.relative_to(root)), language=language)
            
            # Open file
            client.open_file(file_path, language)
            time.sleep(0.1)  # Give server time to process
            
            # Get symbols
            symbols = client.get_document_symbols(file_path)
            for sym in symbols:
                info.symbols.append(lsp_symbol_to_symbol(sym, file_path))
            
            files.append(info)
            
    finally:
        client.stop()
    
    return files

def lsp_symbol_to_symbol(lsp_sym: dict, file_path: Path) -> Symbol:
    """Convert LSP symbol to our Symbol dataclass."""
    kind_map = {
        1: "file", 2: "module", 3: "namespace", 4: "package",
        5: "class", 6: "method", 7: "property", 8: "field",
        9: "constructor", 10: "enum", 11: "interface", 12: "function",
        13: "variable", 14: "constant", 15: "string", 16: "number",
        17: "boolean", 18: "array", 19: "object", 20: "key",
        21: "null", 22: "enummember", 23: "struct", 24: "event",
        25: "operator", 26: "typeparameter"
    }
    
    range_info = lsp_sym.get("range", lsp_sym.get("location", {}).get("range", {}))
    start = range_info.get("start", {})
    end = range_info.get("end", {})
    
    sym = Symbol(
        name=lsp_sym.get("name", ""),
        kind=kind_map.get(lsp_sym.get("kind", 0), "unknown"),
        file=str(file_path),
        line=start.get("line", 0) + 1,
        end_line=end.get("line", 0) + 1,
        detail=lsp_sym.get("detail", "")
    )
    
    # Process children recursively
    for child in lsp_sym.get("children", []):
        sym.children.append(lsp_symbol_to_symbol(child, file_path))
    
    return sym

def analyze_with_fallback(root: Path, language: str) -> list[FileInfo]:
    """Analyze project using regex-based fallback."""
    files = []
    source_files = find_source_files(root, language)
    
    for file_path in source_files:
        if language == "python":
            info = analyze_python_file(file_path)
        elif language in ("typescript", "javascript"):
            info = analyze_typescript_file(file_path)
        elif language == "go":
            info = analyze_go_file(file_path)
        else:
            info = FileInfo(path=str(file_path), language=language)
        
        info.path = str(file_path.relative_to(root))
        files.append(info)
    
    return files

def get_dependencies(root: Path, language: str) -> dict:
    """Extract project dependencies."""
    deps = {"runtime": [], "dev": []}
    
    if language in ("typescript", "javascript"):
        pkg_path = root / "package.json"
        if pkg_path.exists():
            pkg = json.loads(pkg_path.read_text())
            deps["runtime"] = list(pkg.get("dependencies", {}).keys())
            deps["dev"] = list(pkg.get("devDependencies", {}).keys())
    
    elif language == "python":
        req_path = root / "requirements.txt"
        if req_path.exists():
            for line in req_path.read_text().split("\n"):
                line = line.strip()
                if line and not line.startswith("#"):
                    pkg = re.split(r'[<>=!]', line)[0].strip()
                    deps["runtime"].append(pkg)
        
        pyproj = root / "pyproject.toml"
        if pyproj.exists():
            content = pyproj.read_text()
            # Simple TOML parsing for dependencies
            in_deps = False
            for line in content.split("\n"):
                if "[project.dependencies]" in line or "dependencies = [" in line:
                    in_deps = True
                elif in_deps:
                    if line.startswith("[") or line.strip() == "]":
                        in_deps = False
                    else:
                        match = re.search(r'"([^"]+)"', line)
                        if match:
                            deps["runtime"].append(match.group(1).split(">=")[0].split("==")[0])
    
    elif language == "go":
        mod_path = root / "go.mod"
        if mod_path.exists():
            for line in mod_path.read_text().split("\n"):
                if line.strip() and not line.startswith("module") and not line.startswith("go "):
                    parts = line.strip().split()
                    if parts:
                        deps["runtime"].append(parts[0])
    
    return deps

def build_call_graph(files: list[FileInfo]) -> dict:
    """Build a simplified call graph from analyzed files."""
    graph = {}
    all_symbols = {}
    
    # First pass: collect all symbols
    for f in files:
        for sym in f.symbols:
            key = f"{f.path}:{sym.name}"
            all_symbols[sym.name] = key
            all_symbols[key] = key
    
    # Note: Full call graph requires LSP callHierarchy or deeper analysis
    # This is a placeholder for the structure
    
    return graph

def analyze_project(root: Path, use_lsp: bool = True) -> ProjectAnalysis:
    """Main entry point: analyze a project."""
    root = root.resolve()
    language, server, framework = detect_project_type(root)
    
    print(f"[INFO] Detected: {language}" + (f" ({framework})" if framework else ""), file=sys.stderr)
    
    # Try LSP first, fallback to regex
    files = []
    if use_lsp and server:
        files = analyze_with_lsp(root, language, server)
    
    if not files:
        print(f"[INFO] Using fallback analyzer for {language}", file=sys.stderr)
        files = analyze_with_fallback(root, language)
    
    # Build analysis result
    analysis = ProjectAnalysis(
        name=root.name,
        root=str(root),
        language=language,
        framework=framework,
        entry_points=find_entry_points(root, language),
        files=[asdict(f) for f in files],
        dependencies=get_dependencies(root, language),
        call_graph=build_call_graph(files)
    )
    
    return analysis

# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Analyze codebase using LSP")
    parser.add_argument("path", help="Path to project root")
    parser.add_argument("--output", "-o", help="Output JSON file (default: stdout)")
    parser.add_argument("--no-lsp", action="store_true", help="Skip LSP, use fallback only")
    args = parser.parse_args()
    
    root = Path(args.path)
    if not root.exists():
        print(f"Error: {root} does not exist", file=sys.stderr)
        sys.exit(1)
    
    analysis = analyze_project(root, use_lsp=not args.no_lsp)
    result = asdict(analysis)
    
    if args.output:
        Path(args.output).write_text(json.dumps(result, indent=2))
        print(f"[INFO] Analysis saved to {args.output}", file=sys.stderr)
    else:
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
