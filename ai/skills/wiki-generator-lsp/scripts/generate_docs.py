#!/usr/bin/env python3
"""
One-shot wiki generator: analyze project and generate WIKI.md in one command.
Usage: python generate_docs.py /path/to/project [--output WIKI.md]
"""

import sys
import json
import argparse
import tempfile
from pathlib import Path

# Import from sibling scripts
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from lsp_analyzer import analyze_project
from generate_wiki import generate_wiki
from dataclasses import asdict

def main():
    parser = argparse.ArgumentParser(
        description="Generate WIKI.md documentation for a codebase"
    )
    parser.add_argument("path", help="Path to project root")
    parser.add_argument("--output", "-o", default="WIKI.md", help="Output file path")
    parser.add_argument("--no-lsp", action="store_true", help="Skip LSP, use fallback analyzer")
    parser.add_argument("--save-analysis", help="Also save analysis JSON to this path")
    args = parser.parse_args()
    
    project_path = Path(args.path).resolve()
    
    if not project_path.exists():
        print(f"Error: {project_path} does not exist", file=sys.stderr)
        sys.exit(1)
    
    print(f"[1/2] Analyzing {project_path}...", file=sys.stderr)
    analysis = analyze_project(project_path, use_lsp=not args.no_lsp)
    analysis_dict = asdict(analysis)
    
    # Optionally save analysis
    if args.save_analysis:
        Path(args.save_analysis).write_text(json.dumps(analysis_dict, indent=2))
        print(f"      Analysis saved to {args.save_analysis}", file=sys.stderr)
    
    print(f"[2/2] Generating documentation...", file=sys.stderr)
    wiki_content = generate_wiki(analysis_dict)
    
    # Write output
    output_path = Path(args.output)
    output_path.write_text(wiki_content)
    
    print(f"\n✓ Generated {output_path}", file=sys.stderr)
    print(f"  - Language: {analysis.language}", file=sys.stderr)
    if analysis.framework:
        print(f"  - Framework: {analysis.framework}", file=sys.stderr)
    print(f"  - Files analyzed: {len(analysis.files)}", file=sys.stderr)

if __name__ == "__main__":
    main()
