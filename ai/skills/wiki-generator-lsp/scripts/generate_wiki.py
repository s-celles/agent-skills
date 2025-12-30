#!/usr/bin/env python3
"""
Generate WIKI.md documentation from LSP analysis output.
Creates comprehensive documentation with Mermaid diagrams.
"""

import json
import sys
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
from collections import defaultdict

# ============================================================================
# Template Sections
# ============================================================================

WIKI_HEADER = """# {name} Documentation

> Auto-generated documentation using LSP-based code analysis

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture Overview](#architecture-overview)
- [Project Structure](#project-structure)
- [Core Components](#core-components)
- [Data Flow](#data-flow)
- [Data Model](#data-model)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Getting Started](#getting-started)
- [Development Guide](#development-guide)

---
"""

# ============================================================================
# Mermaid Diagram Generators
# ============================================================================

def generate_architecture_diagram(files: list, framework: str) -> str:
    """Generate architecture flowchart from file structure."""
    
    # Group files by directory
    dirs = defaultdict(list)
    for f in files:
        path = Path(f["path"])
        if len(path.parts) > 1:
            dirs[path.parts[0]].append(path.name)
        else:
            dirs["root"].append(path.name)
    
    # Build diagram
    lines = ["```mermaid", "flowchart TB"]
    
    # Add framework-specific structure
    if framework in ("React", "Next.js", "Vue"):
        lines.append("    subgraph Frontend")
        lines.append("        UI[UI Components]")
        lines.append("        State[State Management]")
        lines.append("        API[API Layer]")
        lines.append("    end")
        lines.append("    UI --> State")
        lines.append("    State --> API")
    
    elif framework in ("Express", "FastAPI", "Flask", "Fastify"):
        lines.append("    subgraph Backend")
        lines.append("        Routes[Routes/Controllers]")
        lines.append("        Services[Services/Logic]")
        lines.append("        Models[Data Models]")
        lines.append("        DB[(Database)]")
        lines.append("    end")
        lines.append("    Routes --> Services")
        lines.append("    Services --> Models")
        lines.append("    Models --> DB")
    
    else:
        # Generic structure based on directories
        node_id = 0
        for dir_name, files_list in dirs.items():
            if dir_name in ("root", "__pycache__", "node_modules"):
                continue
            lines.append(f"    subgraph {dir_name.title()}")
            for fname in files_list[:5]:  # Limit to 5 files per dir
                safe_name = fname.replace(".", "_").replace("-", "_")
                lines.append(f"        {safe_name}_{node_id}[{fname}]")
                node_id += 1
            lines.append("    end")
    
    lines.append("```")
    return "\n".join(lines)

def generate_sequence_diagram(entry_points: list, framework: str) -> str:
    """Generate sequence diagram for main workflows."""
    
    lines = ["```mermaid", "sequenceDiagram"]
    
    if framework in ("React", "Next.js", "Vue"):
        lines.extend([
            "    participant User",
            "    participant Component",
            "    participant State",
            "    participant API",
            "    participant Server",
            "",
            "    User->>Component: Interaction",
            "    Component->>State: Update State",
            "    State->>API: Fetch Data",
            "    API->>Server: HTTP Request",
            "    Server-->>API: Response",
            "    API-->>State: Update",
            "    State-->>Component: Re-render",
            "    Component-->>User: Display"
        ])
    
    elif framework in ("Express", "FastAPI", "Flask", "Fastify"):
        lines.extend([
            "    participant Client",
            "    participant Router",
            "    participant Controller",
            "    participant Service",
            "    participant Database",
            "",
            "    Client->>Router: HTTP Request",
            "    Router->>Controller: Route Handler",
            "    Controller->>Service: Business Logic",
            "    Service->>Database: Query",
            "    Database-->>Service: Result",
            "    Service-->>Controller: Data",
            "    Controller-->>Router: Response",
            "    Router-->>Client: HTTP Response"
        ])
    
    else:
        lines.extend([
            "    participant User",
            "    participant Main",
            "    participant Module",
            "    participant Data",
            "",
            "    User->>Main: Input",
            "    Main->>Module: Process",
            "    Module->>Data: Read/Write",
            "    Data-->>Module: Result",
            "    Module-->>Main: Output",
            "    Main-->>User: Display"
        ])
    
    lines.append("```")
    return "\n".join(lines)

def generate_class_diagram(files: list) -> str:
    """Generate class diagram from symbols."""
    
    classes = []
    for f in files:
        for sym in f.get("symbols", []):
            if sym.get("kind") in ("class", "interface", "struct"):
                classes.append({
                    "name": sym["name"],
                    "kind": sym["kind"],
                    "methods": [c["name"] for c in sym.get("children", []) if c.get("kind") == "method"],
                    "properties": [c["name"] for c in sym.get("children", []) if c.get("kind") in ("property", "field")]
                })
    
    if not classes:
        return "_No classes detected in codebase._"
    
    lines = ["```mermaid", "classDiagram"]
    
    for cls in classes[:10]:  # Limit to 10 classes
        safe_name = cls["name"].replace("-", "_")
        lines.append(f"    class {safe_name} {{")
        
        for prop in cls.get("properties", [])[:5]:
            lines.append(f"        +{prop}")
        
        for method in cls.get("methods", [])[:5]:
            lines.append(f"        +{method}()")
        
        lines.append("    }")
    
    lines.append("```")
    return "\n".join(lines)

def generate_er_diagram(files: list, language: str) -> str:
    """Generate entity relationship diagram from data models."""
    
    entities = []
    for f in files:
        # Look for model files
        path_lower = f["path"].lower()
        is_model = any(x in path_lower for x in ["model", "schema", "entity", "type"])
        
        for sym in f.get("symbols", []):
            if sym.get("kind") in ("class", "interface", "struct", "type"):
                if is_model or sym["name"].endswith(("Model", "Entity", "Schema", "Type")):
                    entities.append({
                        "name": sym["name"],
                        "fields": [c["name"] for c in sym.get("children", []) 
                                  if c.get("kind") in ("property", "field")]
                    })
    
    if not entities:
        return "_No data models detected. Add models in a `models/` or `schemas/` directory._"
    
    lines = ["```mermaid", "erDiagram"]
    
    for entity in entities[:8]:  # Limit to 8 entities
        safe_name = entity["name"].replace("-", "_")
        lines.append(f"    {safe_name} {{")
        for field in entity.get("fields", [])[:6]:
            safe_field = field.replace("-", "_")
            lines.append(f"        string {safe_field}")
        lines.append("    }")
    
    lines.append("```")
    return "\n".join(lines)

# ============================================================================
# Section Generators
# ============================================================================

def generate_project_overview(analysis: dict) -> str:
    """Generate project overview section."""
    
    deps = analysis.get("dependencies", {})
    runtime_deps = deps.get("runtime", [])[:10]
    dev_deps = deps.get("dev", [])[:10]
    
    return f"""## Project Overview

### Purpose

{analysis['name']} is a {analysis['language'].title()} project{' built with ' + analysis['framework'] if analysis.get('framework') else ''}.

### Tech Stack

| Category | Technology |
|----------|------------|
| Language | {analysis['language'].title()} |
| Framework | {analysis.get('framework') or 'N/A'} |
| Files | {len(analysis.get('files', []))} source files |

### Key Dependencies

**Runtime:**
{chr(10).join(f'- `{d}`' for d in runtime_deps) if runtime_deps else '- _None detected_'}

**Development:**
{chr(10).join(f'- `{d}`' for d in dev_deps[:5]) if dev_deps else '- _None detected_'}

---
"""

def generate_architecture_section(analysis: dict) -> str:
    """Generate architecture overview section."""
    
    diagram = generate_architecture_diagram(
        analysis.get("files", []),
        analysis.get("framework", "")
    )
    
    return f"""## Architecture Overview

### High-Level Architecture

{diagram}

### Design Patterns

Based on the codebase structure, the following patterns are observed:

| Pattern | Evidence |
|---------|----------|
| {"MVC/MVVM" if analysis.get("framework") in ("React", "Vue", "Next.js") else "Layered Architecture"} | Separation of concerns in directory structure |
| Module Pattern | Organized file structure with clear imports |

### Core Principles

- **Separation of Concerns**: Logic is divided into distinct modules
- **Single Responsibility**: Each file/module handles specific functionality
- **DRY (Don't Repeat Yourself)**: Shared utilities and components

---
"""

def generate_project_structure(analysis: dict) -> str:
    """Generate project structure section."""
    
    files = analysis.get("files", [])
    
    # Build tree structure
    tree_lines = []
    dirs_seen = set()
    
    for f in sorted(files, key=lambda x: x["path"]):
        path = Path(f["path"])
        parts = path.parts
        
        # Add directories
        for i, part in enumerate(parts[:-1]):
            dir_path = "/".join(parts[:i+1])
            if dir_path not in dirs_seen:
                indent = "    " * i
                tree_lines.append(f"{indent}├── {part}/")
                dirs_seen.add(dir_path)
        
        # Add file
        indent = "    " * (len(parts) - 1)
        tree_lines.append(f"{indent}├── {path.name}")
    
    tree = "\n".join(tree_lines[:30])  # Limit output
    
    entry_points = analysis.get("entry_points", [])
    
    return f"""## Project Structure

### Directory Tree

```
{analysis['name']}/
{tree}
```

### Entry Points

{chr(10).join(f'- `{e}`' for e in entry_points) if entry_points else '- _No entry points detected_'}

### Key Directories

| Directory | Purpose |
|-----------|---------|
| `src/` | Main source code |
| `lib/` | Library code |
| `tests/` | Test files |
| `docs/` | Documentation |

---
"""

def generate_components_section(analysis: dict) -> str:
    """Generate core components section."""
    
    files = analysis.get("files", [])
    components = []
    
    for f in files:
        symbols = f.get("symbols", [])
        if symbols:
            main_symbols = [s for s in symbols if s.get("kind") in ("class", "function", "interface")]
            if main_symbols:
                components.append({
                    "file": f["path"],
                    "symbols": main_symbols[:5]
                })
    
    sections = []
    for comp in components[:10]:  # Limit to 10 components
        file_path = comp["file"]
        sections.append(f"### `{file_path}`\n")
        
        for sym in comp["symbols"]:
            kind = sym.get("kind", "unknown")
            name = sym.get("name", "")
            docstring = sym.get("docstring", "")
            
            sections.append(f"**{kind.title()}:** `{name}`\n")
            if docstring:
                sections.append(f"> {docstring[:200]}...\n" if len(docstring) > 200 else f"> {docstring}\n")
            
            # Methods
            children = sym.get("children", [])
            methods = [c for c in children if c.get("kind") == "method"]
            if methods:
                sections.append("\n| Method | Line |\n|--------|------|")
                for m in methods[:5]:
                    sections.append(f"| `{m['name']}()` | {m.get('line', 'N/A')} |")
                sections.append("")
        
        sections.append("")
    
    if not sections:
        sections = ["_No major components detected. Run with LSP enabled for better analysis._"]
    
    return f"""## Core Components

{chr(10).join(sections)}

---
"""

def generate_data_flow_section(analysis: dict) -> str:
    """Generate data flow section."""
    
    diagram = generate_sequence_diagram(
        analysis.get("entry_points", []),
        analysis.get("framework", "")
    )
    
    return f"""## Data Flow

### Main Request Flow

{diagram}

### Event Flow

The application follows these patterns:

1. **User Input** → Event handlers capture user actions
2. **State Update** → Application state is modified
3. **Side Effects** → API calls, storage updates
4. **Re-render** → UI updates to reflect new state

---
"""

def generate_data_model_section(analysis: dict) -> str:
    """Generate data model section."""
    
    class_diagram = generate_class_diagram(analysis.get("files", []))
    er_diagram = generate_er_diagram(
        analysis.get("files", []),
        analysis.get("language", "")
    )
    
    return f"""## Data Model

### Class Structure

{class_diagram}

### Entity Relationships

{er_diagram}

---
"""

def generate_api_section(analysis: dict) -> str:
    """Generate API reference section."""
    
    framework = analysis.get("framework", "")
    
    if framework in ("Express", "FastAPI", "Flask", "Fastify"):
        return """## API Reference

### Endpoints Overview

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/...` | Retrieve resources |
| POST | `/api/v1/...` | Create resources |
| PUT | `/api/v1/...` | Update resources |
| DELETE | `/api/v1/...` | Remove resources |

### Authentication

```
Authorization: Bearer <token>
```

### Request/Response Format

**Request:**
```json
{
  "field": "value"
}
```

**Response:**
```json
{
  "success": true,
  "data": {}
}
```

---
"""
    
    return """## API Reference

_API endpoints not detected. Add route handlers for automatic detection._

---
"""

def generate_config_section(analysis: dict) -> str:
    """Generate configuration section."""
    
    language = analysis.get("language", "")
    
    config_files = {
        "typescript": ["tsconfig.json", ".env", ".env.local"],
        "javascript": [".env", ".env.local", "config.js"],
        "python": ["pyproject.toml", ".env", "config.py", "settings.py"],
        "go": ["config.yaml", ".env"],
        "rust": ["Cargo.toml", ".env"]
    }
    
    files = config_files.get(language, [".env"])
    
    return f"""## Configuration

### Environment Variables

Create a `.env` file with required variables:

```env
# Application
APP_ENV=development
APP_DEBUG=true

# Database
DATABASE_URL=postgres://user:pass@localhost:5432/db

# API Keys
API_KEY=your-api-key
```

### Configuration Files

| File | Purpose |
|------|---------|
{chr(10).join(f'| `{f}` | Configuration |' for f in files)}

---
"""

def generate_getting_started(analysis: dict) -> str:
    """Generate getting started section."""
    
    language = analysis.get("language", "")
    framework = analysis.get("framework", "")
    
    install_cmds = {
        "typescript": "npm install",
        "javascript": "npm install",
        "python": "pip install -r requirements.txt",
        "go": "go mod download",
        "rust": "cargo build"
    }
    
    run_cmds = {
        "typescript": "npm run dev",
        "javascript": "npm start",
        "python": "python main.py",
        "go": "go run main.go",
        "rust": "cargo run"
    }
    
    if framework == "Next.js":
        run_cmds["typescript"] = "npm run dev"
    elif framework == "FastAPI":
        run_cmds["python"] = "uvicorn main:app --reload"
    elif framework == "Flask":
        run_cmds["python"] = "flask run"
    
    return f"""## Getting Started

### Prerequisites

- {language.title()} installed
- Package manager (npm/pip/cargo/etc.)
- Git

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd {analysis['name']}
```

2. Install dependencies:
```bash
{install_cmds.get(language, 'npm install')}
```

3. Set up environment:
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Running Locally

```bash
{run_cmds.get(language, 'npm start')}
```

---
"""

def generate_dev_guide(analysis: dict) -> str:
    """Generate development guide section."""
    
    return """## Development Guide

### Adding New Features

1. Create a new branch: `git checkout -b feature/name`
2. Add your code in the appropriate module
3. Write tests for new functionality
4. Run linting: `npm run lint` / `flake8` / `cargo clippy`
5. Submit a pull request

### Testing

```bash
# Run all tests
npm test  # or pytest, go test, cargo test

# Run specific test
npm test -- --grep "test name"
```

### Code Conventions

- Follow the existing code style
- Use meaningful variable/function names
- Add docstrings/comments for complex logic
- Keep functions small and focused

### Git Workflow

1. Always work on feature branches
2. Write descriptive commit messages
3. Squash commits before merging
4. Keep PRs focused and reviewable

---

_Generated by wiki-generator-lsp_
"""

# ============================================================================
# Main Generator
# ============================================================================

def generate_wiki(analysis: dict) -> str:
    """Generate complete WIKI.md from analysis."""
    
    sections = [
        WIKI_HEADER.format(name=analysis.get("name", "Project")),
        generate_project_overview(analysis),
        generate_architecture_section(analysis),
        generate_project_structure(analysis),
        generate_components_section(analysis),
        generate_data_flow_section(analysis),
        generate_data_model_section(analysis),
        generate_api_section(analysis),
        generate_config_section(analysis),
        generate_getting_started(analysis),
        generate_dev_guide(analysis)
    ]
    
    return "\n".join(sections)

# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Generate WIKI.md from analysis")
    parser.add_argument("analysis", help="Path to analysis JSON file")
    parser.add_argument("--output", "-o", default="WIKI.md", help="Output file")
    args = parser.parse_args()
    
    # Load analysis
    analysis_path = Path(args.analysis)
    if not analysis_path.exists():
        print(f"Error: {analysis_path} not found", file=sys.stderr)
        sys.exit(1)
    
    analysis = json.loads(analysis_path.read_text())
    
    # Generate wiki
    wiki_content = generate_wiki(analysis)
    
    # Write output
    output_path = Path(args.output)
    output_path.write_text(wiki_content)
    print(f"[INFO] Generated {output_path}", file=sys.stderr)

if __name__ == "__main__":
    main()
