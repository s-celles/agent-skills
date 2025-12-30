# Wiki Generator LSP Scripts

Python scripts for generating comprehensive codebase documentation using Language Server Protocol (LSP) analysis.

## Prerequisites

- Python 3.7+
- LSP server for your target language (optional, fallback available)

### LSP Server Installation

| Language | Install Command |
|----------|-----------------|
| TypeScript/JS | `npm install -g typescript-language-server typescript` |
| Python | `pip install python-lsp-server` |
| Go | `go install golang.org/x/tools/gopls@latest` |
| Rust | `rustup component add rust-analyzer` |
| C/C++ | `apt install clangd` or `brew install llvm` |
| Java | Download Eclipse JDT Language Server |

## Scripts Overview

### generate_docs.py

Main entry point for documentation generation.

```bash
python generate_docs.py /path/to/project [options]
```

**Options:**

| Option | Description | Default |
|--------|-------------|---------|
| `--output`, `-o` | Output file path | `WIKI.md` |
| `--timeout` | LSP request timeout (seconds) | `60` |
| `--verbose`, `-v` | Enable debug output | `false` |
| `--exclude` | Glob patterns to exclude | `node_modules,venv,.git` |

**Examples:**

```bash
# Basic usage
python generate_docs.py /home/user/my-project

# Custom output location
python generate_docs.py /home/user/my-project -o docs/ARCHITECTURE.md

# With debug output
python generate_docs.py /home/user/my-project -v

# Exclude test directories
python generate_docs.py /home/user/my-project --exclude "**/test/**,**/tests/**"
```

### lsp_analyzer.py

LSP client for extracting code information.

**Features:**
- Symbol extraction (classes, functions, methods, variables)
- Reference finding
- Call hierarchy analysis
- Type information retrieval
- Import/export detection

**Data Structures:**

```python
@dataclass
class Symbol:
    name: str
    kind: str        # class, function, method, variable, interface
    file: str
    line: int
    end_line: int
    detail: str
    children: list
    references: list
    calls: list
    called_by: list
    docstring: str

@dataclass
class ProjectAnalysis:
    name: str
    root: str
    language: str
    framework: str
    files: list[FileInfo]
    entry_points: list
    dependencies: dict
```

### generate_wiki.py

Transforms analysis results into formatted WIKI.md.

**Output Sections:**
1. Project Overview
2. Architecture (Mermaid flowchart)
3. Project Structure
4. Core Components
5. Data Flow (Mermaid sequence diagram)
6. Data Model (Mermaid class/ER diagrams)
7. API Reference
8. Configuration
9. Getting Started
10. Development Guide

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ generate_docs.py│────▶│ lsp_analyzer.py │────▶│ generate_wiki.py│
│   (entry point) │     │  (LSP client)   │     │  (formatter)    │
└─────────────────┘     └────────┬────────┘     └─────────────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │   LSP Server    │
                        │ (language-specific)
                        └─────────────────┘
```

## Fallback Mode

If no LSP server is available, scripts use fallback analyzers:

1. **AST parsing** for Python (using `ast` module)
2. **Regex patterns** for other languages
3. **Import statement analysis** for dependency graphs

Fallback mode provides approximately 70% of LSP accuracy.

## Troubleshooting

### "Could not start LSP server"

1. Verify the LSP server is installed: `which typescript-language-server`
2. Ensure it's in your PATH
3. Try running the server manually to check for errors

### "LSP request timed out"

1. Increase timeout: `--timeout 120`
2. Analyze smaller portions of the codebase
3. Check system resources (CPU, memory)

### "No symbols found"

1. Verify the project has recognized config files
2. Check file permissions
3. Run with `--verbose` to see which files are being processed

### Memory issues

For large codebases:
1. Analyze subdirectories separately
2. Use `--exclude` to skip non-essential files
3. Consider running on a machine with more RAM

## Output

The scripts generate a WIKI.md file with:

- Comprehensive project overview
- Mermaid diagrams for visualization
- Auto-generated API documentation
- Dependency graphs
- Getting started guide

See the parent [SKILL.md](../SKILL.md) for output section details.
