# AI Config

A collection of AI/LLM configuration files and [agent skills](https://agentskills.io/) for various tools and platforms.

## Documentation

Full documentation is available at **[s-celles.github.io/ai-config](https://s-celles.github.io/ai-config/)**

- [Standards for Sharing Agents and Skills](https://s-celles.github.io/ai-config/docs/)
- [Available Skills](https://s-celles.github.io/ai-config/docs/skills/)

## Repository Structure

```
ai-config/
├── ai/
│   ├── agents/      # Agent configurations
│   ├── commands/    # Command definitions
│   └── skills/      # Agent skills (SKILL.md files)
├── site/            # Hugo website source
└── AGENTS.md        # Instructions for AI coding agents
```

## Quick Start

To use a skill, copy its directory to your skills folder or reference it in your configuration:

```bash
# Example: copy the license-advisor skill
cp -r ai/skills/license-advisor ~/.claude/skills/
```

## License

MIT
