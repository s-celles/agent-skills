---
title: "Agent Ignore Files"
linkTitle: "Agent Ignore"
weight: 15
description: "The fragmented landscape of AI agent ignore files and the push for standardization."
---

## The Problem: Fragmented Ignore Files

Different AI coding tools have introduced their own ignore file formats, creating a fragmented ecosystem:

| File | Tool | Format |
|------|------|--------|
| `.geminiignore` | Google Gemini CLI | gitignore syntax |
| `.cursorignore` | Cursor | gitignore syntax |
| `.codeiumignore` | Codeium | gitignore syntax |
| `.aiexclude` | Various | gitignore syntax |
| `.aiignore` | Various | gitignore syntax |

All of these follow the same `.gitignore` syntax, but having multiple files creates problems:

- **Maintenance burden** - Keeping multiple files in sync is error-prone
- **Project clutter** - Multiple ignore files pollute the repository root
- **Security risk** - Switching agents may expose secrets if the new tool's ignore file is missing

## The Proposed Solution: `.agentignore`

A [community proposal](https://github.com/tourcoder/agentignore) aims to unify these into a single `.agentignore` standard.

### Specification

The `.agentignore` file uses the same syntax as `.gitignore`:

```gitignore
# Secrets and credentials
.env
.env.*
*.pem
credentials.json

# Sensitive directories
secrets/
private/

# Large files that shouldn't be in context
*.log
node_modules/
dist/
```

### How It Works

1. **File Discovery**: When an AI agent is activated, it looks for `.agentignore` starting from the current directory and traversing up to the project root
2. **Rule Combination**: Rules from all found `.agentignore` files are combined
3. **Matching**: Files matching any pattern are excluded from agent processing

### Implementation Requirements

For tool developers implementing `.agentignore` support:

- Parse the file line by line
- Trim whitespace, ignore empty lines and lines starting with `#`
- Support standard glob patterns (`*`, `**`, `?`)
- Replicate `.gitignore` matching behavior for consistency

## Current Tool-Specific Approaches

Until `.agentignore` becomes standard, each tool has its own method:

### Claude Code

Uses `.claude/settings.json` with deny rules:

```json
{
  "permissions": {
    "deny": [
      ".env",
      "secrets/**",
      "*.pem"
    ]
  }
}
```

### Cursor

Uses `.cursor/rules` directory with version-controlled rule files.

### Gemini CLI

Uses `.geminiignore` with gitignore syntax:

```gitignore
# Gemini-specific ignore
.env
secrets/
```

## Why Standardization Matters

### The Risk of Secret Leakage

AI coding agents can inadvertently expose secrets in several ways:

| Risk | Description |
|------|-------------|
| **Reading secrets** | Agent reads `.env` or credential files and includes them in context |
| **Exposing in output** | Agent includes secrets in generated code, commits, or explanations |
| **Logging to providers** | Conversations containing secrets may be logged by AI providers |
| **Cross-tool exposure** | Switching tools may expose secrets if ignore files aren't synchronized |

### Real-World Issues

The Claude Code community has documented several concerns related to file access and secrets:

- [Issue #5616](https://github.com/anthropics/claude-code/issues/5616) - Claude Code loads and exports .env on startup, even with read permissions denied
- [Issue #4570](https://github.com/anthropics/claude-code/issues/4570) - Deny rules configuration failure in Claude Code CLI
- [Issue #112](https://github.com/anthropics/claude-code/issues/112) - Potential security risk: Claude Code accessing local .env file environment variables
- [Issue #79](https://github.com/anthropics/claude-code/issues/79) - How to tell Claude CLI agent to ignore directories (is there a ".claudeignore"?)

These issues highlight that:
- Users frequently need to protect secrets from AI agents
- Current mechanisms are tool-specific and inconsistent
- A standardized approach would benefit the entire ecosystem

### Scenario: Cross-Tool Exposure

```
Developer uses Cursor, then switches to Claude Code

Without standardization:
- Cursor respects .cursorignore (has .env listed)
- Claude Code doesn't read .cursorignore
- Secrets may be exposed to Claude

With .agentignore:
- Both tools read the same file
- Consistent protection across tools
```

### Developer Experience

| Aspect | Multiple Files | Single `.agentignore` |
|--------|----------------|----------------------|
| Maintenance | Update N files for N tools | Update 1 file |
| Onboarding | Learn each tool's format | Learn once |
| Code review | Check multiple files | Check one file |
| Security audit | Verify each file | Verify one file |

## Best Practices (Current State)

Until standardization is complete:

### 1. Use Your Tool's Native Format

Follow your primary tool's ignore mechanism:
- Claude Code: `.claude/settings.json`
- Cursor: `.cursorignore`
- Gemini: `.geminiignore`

### 2. Document Your Approach

Add to your `README.md` or `AGENTS.md`:

```markdown
## AI Agent Configuration

This project uses `.cursorignore` to prevent AI agents from accessing:
- Environment files (.env*)
- Credentials (*.pem, credentials.json)
- Build artifacts (dist/, node_modules/)
```

### 3. Consider Creating Multiple Files

If your team uses multiple tools, maintain ignore files for each:

```bash
# Create consistent ignore files
cp .gitignore .cursorignore
cp .gitignore .geminiignore
# Then add tool-specific entries
```

### 4. Protect Secrets at Multiple Levels

Don't rely solely on ignore files:
- Use `.gitignore` to prevent committing secrets
- Use environment variables instead of files when possible
- Use secret management tools (Vault, AWS Secrets Manager)

## The Path Forward

### Open Issues and Discussions

- [Gemini CLI Issue #4688](https://github.com/google-gemini/gemini-cli/issues/4688) - Push for `.agentignore` standard
- [tourcoder/agentignore](https://github.com/tourcoder/agentignore) - Community specification proposal

### What Would Help

1. **Tool vendors adopting `.agentignore`** as a fallback when tool-specific files don't exist
2. **AAIF consideration** of agent ignore as part of the agentic AI standards ecosystem
3. **Community convergence** on a single format

## Comparison with Related Standards

| Standard | Purpose | Scope |
|----------|---------|-------|
| `.gitignore` | Exclude files from version control | Git |
| `.dockerignore` | Exclude files from Docker builds | Docker |
| `.npmignore` | Exclude files from npm packages | npm |
| `.agentignore` | Exclude files from AI agents | All AI tools (proposed) |

## Further Reading

### Standards and Proposals

- [tourcoder/agentignore Proposal](https://github.com/tourcoder/agentignore) - Community specification proposal - Verified on 2025-12-28
- [Gemini CLI Standardization Issue](https://github.com/google-gemini/gemini-cli/issues/4688) - Push for `.agentignore` standard - Verified on 2025-12-28
- [Claude Code Deny Rules](https://docs.anthropic.com/en/docs/claude-code) - Official Claude Code documentation - Verified on 2025-12-28

### Claude Code Issues

- [Issue #5616](https://github.com/anthropics/claude-code/issues/5616) - Claude Code loads and exports .env on startup - Verified on 2025-12-28
- [Issue #4570](https://github.com/anthropics/claude-code/issues/4570) - Deny rules configuration failure - Verified on 2025-12-28
- [Issue #112](https://github.com/anthropics/claude-code/issues/112) - Security risk: accessing local .env file - Verified on 2025-12-28
- [Issue #79](https://github.com/anthropics/claude-code/issues/79) - How to ignore directories (".claudeignore"?) - Verified on 2025-12-28

---

> **Note**: The `.agentignore` standard is still a proposal. Check your specific tool's documentation for the currently supported ignore mechanism.
