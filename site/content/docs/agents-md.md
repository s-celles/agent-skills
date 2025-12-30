---
title: "AGENTS.md Specification"
linkTitle: "AGENTS.md"
weight: 10
description: "The open standard for guiding AI coding agents, now governed by the Agentic AI Foundation."
---

## What Is AGENTS.md?

AGENTS.md is a simple, open format for guiding AI coding agents. Think of it as a **README for agents**: a dedicated, predictable place to provide context and instructions to help AI coding agents work effectively on your project.

## History and Governance

- **August 2025**: Released by OpenAI as an open standard
- **December 2025**: Donated to the [Agentic AI Foundation (AAIF)](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) under the Linux Foundation
- **Adoption**: Over 60,000 open source projects

The AAIF was co-founded by Anthropic, Block, and OpenAI, with platinum members including AWS, Bloomberg, Cloudflare, Google, and Microsoft.

## Why AGENTS.md?

| File | Audience | Purpose |
|------|----------|---------|
| `README.md` | Humans | Quick starts, project descriptions, contribution guidelines |
| `AGENTS.md` | AI Agents | Build steps, tests, conventions, development environment details |

AGENTS.md separates agent-specific guidance from human-focused documentation. It contains detailed context that might clutter a README or isn't relevant to human contributors.

## Format and Structure

- **Format**: Standard Markdown with no required fields
- **Location**: Root of repository (or nested within subdirectories for monorepos)
- **Precedence**: The closest AGENTS.md to edited files takes precedence; user prompts override all

## Common Sections

Recommended topics to include:

| Section | Description |
|---------|-------------|
| **Project overview** | What the project does and key architecture |
| **Setup/build commands** | How to install dependencies and build |
| **Test instructions** | How to run tests |
| **Code style** | Formatting, linting, conventions |
| **Security considerations** | Sensitive files, environment variables |
| **Development environment** | Tools, versions, configurations |
| **PR/commit guidelines** | Commit message format, branch naming |

## Example

```markdown
# AGENTS.md

## Setup commands
- Install deps: `pnpm install`
- Start dev server: `pnpm dev`
- Run tests: `pnpm test`

## Code style
- TypeScript strict mode
- Single quotes, no semicolons
- Use Prettier for formatting

## Testing
- Run `pnpm test` before committing
- Coverage threshold: 80%

## Security
- Never commit `.env` files
- Use environment variables for secrets
```

## Key Features

### Cross-Platform Compatibility

Your single AGENTS.md file works across multiple agent platforms:

| Agent/Tool | Vendor |
|------------|--------|
| Codex | OpenAI |
| Jules | Google |
| Cursor | Cursor |
| VS Code Copilot | GitHub/Microsoft |
| Devin | Cognition |
| Amp | Sourcegraph |
| Factory | Factory |
| Gemini CLI | Google |

### Monorepo Support

For monorepos, place AGENTS.md files at multiple levels:

```
project/
├── AGENTS.md              # Root-level instructions
├── packages/
│   ├── frontend/
│   │   └── AGENTS.md      # Frontend-specific instructions
│   └── backend/
│       └── AGENTS.md      # Backend-specific instructions
```

Agents automatically read the nearest file in the directory tree, so the closest one takes precedence.

### Automatic Execution

Agents attempt to execute listed commands and fix failures automatically. This makes AGENTS.md a powerful way to ensure consistent development practices.

## AGENTS.md vs CLAUDE.md

Some projects use `CLAUDE.md` specifically for Claude Code. The relationship:

| File | Scope | Recommendation |
|------|-------|----------------|
| `AGENTS.md` | All AI coding agents | Use for universal agent instructions |
| `CLAUDE.md` | Claude Code only | Use for Claude-specific configurations |

You can use both files if you need platform-specific instructions alongside universal ones.

## Related Standards

AGENTS.md is one of several standards now governed by the Agentic AI Foundation:

| Standard | Purpose | Original Author |
|----------|---------|-----------------|
| **AGENTS.md** | Project guidance for coding agents | OpenAI |
| **MCP** | Model Context Protocol for tool integration | Anthropic |
| **Goose** | Open source agent framework | Block |

## Best Practices

1. **Keep it focused** - Include only information relevant to AI agents
2. **Be specific** - Provide exact commands, not vague descriptions
3. **Update regularly** - Keep instructions current with project changes
4. **Test commands** - Ensure all listed commands actually work
5. **Consider security** - Document what agents should NOT access

## Further Reading

- [AGENTS.md Official Site](https://agents.md) - Verified on 2025-12-28
- [AGENTS.md GitHub Repository](https://github.com/agentsmd/agents.md) - Verified on 2025-12-28
- [Linux Foundation AAIF Announcement](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) - Verified on 2025-12-28
- [OpenAI AAIF Announcement](https://openai.com/index/agentic-ai-foundation/) - Verified on 2025-12-28
- [Anthropic MCP Donation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) - Verified on 2025-12-28

---

> **Note**: AGENTS.md provides guidance to AI agents, but agents may not follow all instructions perfectly. Always review agent-generated changes before committing.
