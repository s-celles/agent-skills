# Contributing to Agent Skills

Thank you for your interest in contributing! This document provides guidelines for contributing new skills or improving existing ones.

## Table of Contents

- [Getting Started](#getting-started)
- [Skill Structure](#skill-structure)
- [Creating a New Skill](#creating-a-new-skill)
- [SKILL.md Format](#skillmd-format)
- [Reference Templates](#reference-templates)
- [Quality Checklist](#quality-checklist)
- [Pull Request Process](#pull-request-process)

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your contribution
4. Make your changes
5. Submit a pull request

## Skill Structure

Each skill follows this directory structure:

```
skill-name/
├── SKILL.md              # Required: Skill definition and instructions
├── references/           # Optional: Reference templates and guides
│   ├── template-1.md
│   └── template-2.md
└── scripts/              # Optional: Executable scripts
    ├── script.py
    └── README.md
```

## Creating a New Skill

### 1. Choose a Name

- Use `kebab-case` (lowercase with hyphens)
- Be descriptive but concise
- Examples: `license-advisor`, `wiki-generator-lsp`, `thesis-assistant`

### 2. Create the Directory

```bash
mkdir -p skill-name/references
```

### 3. Write the SKILL.md

See [SKILL.md Format](#skillmd-format) below.

### 4. Add Reference Templates (Optional)

Create markdown files in `references/` for templates, guides, or examples.

### 5. Add Scripts (Optional)

If your skill uses executable scripts:
- Place them in `scripts/`
- Include a `scripts/README.md` with usage instructions
- Add a `requirements.txt` if there are dependencies

## SKILL.md Format

Every SKILL.md must include YAML frontmatter:

```yaml
---
name: skill-name
version: "1.0.0"
description: "Comprehensive description of what the skill does and when to use it."
keywords: [keyword1, keyword2, keyword3]
category: documentation | legal | academic | development | other
status: tested | experimental
languages: [en] | [fr] | [multilingual]
related: [related-skill-1, related-skill-2]  # Optional
---
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier (kebab-case) |
| `version` | Yes | Semantic version (e.g., "1.0.0") |
| `description` | Yes | When and how to use the skill |
| `keywords` | Yes | Array of searchable keywords |
| `category` | Yes | Skill category |
| `status` | Yes | `tested` or `experimental` |
| `languages` | Yes | Supported languages |
| `related` | No | Related skill names |

### Content Sections

After the frontmatter, include:

1. **Title** - H1 heading with skill name
2. **Introduction** - Brief overview
3. **Instructions** - How the skill works (questionnaire, templates, workflow)
4. **Reference Guide** - List of templates and when to use them
5. **Tips** - Best practices and advice

## Reference Templates

Templates in `references/` should:

- Have descriptive names with `-template.md` suffix
- Include clear section headings
- Provide guidance in brackets: `[Describe your methodology here]`
- Be standalone and reusable
- Include examples where helpful

## Quality Checklist

Before submitting, verify:

### SKILL.md
- [ ] YAML frontmatter includes all required fields
- [ ] Description is clear and explains when to use the skill
- [ ] Keywords are relevant and searchable
- [ ] Status is appropriate (`experimental` if not thoroughly tested)
- [ ] Instructions are complete and actionable

### Reference Templates
- [ ] Each template has a clear purpose
- [ ] Templates are well-structured with headings
- [ ] Guidance is provided for each section
- [ ] Templates are listed in SKILL.md

### Scripts (if applicable)
- [ ] Scripts are documented with docstrings
- [ ] Dependencies are listed in `requirements.txt`
- [ ] A README explains installation and usage
- [ ] Error handling is implemented

### General
- [ ] No typos or grammatical errors
- [ ] Consistent formatting
- [ ] Links are valid
- [ ] Sensitive information is excluded

## Pull Request Process

1. **Title**: Use format `Add skill: skill-name` or `Improve: skill-name`

2. **Description**: Include:
   - What the skill does
   - Why it's useful
   - Any testing performed
   - Related issues (if any)

3. **Review**: Maintainers will review for:
   - Adherence to structure guidelines
   - Quality of content
   - Completeness
   - Potential overlap with existing skills

4. **Status**: New skills start as `experimental` unless thoroughly tested

## Questions?

Open an issue if you have questions about contributing.

---

Thank you for contributing!
