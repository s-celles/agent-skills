---
title: "Progressive Disclosure for Skills"
linkTitle: "Progressive Disclosure"
weight: 45
description: "How the SKILL.md specification uses progressive disclosure to optimize context window usage."
---

## What Is Progressive Disclosure?

Progressive disclosure is a design pattern where information is revealed incrementally, showing users only what they need at each stage. In the context of AI skills, this means providing minimal metadata upfront and loading detailed instructions only when needed.

## Why It Matters for AI Skills

The context window is a limited resource shared between:

- System prompts
- Conversation history
- Skill metadata
- User requests
- Tool outputs

Loading full skill instructions for every available skill would quickly exhaust the context window. Progressive disclosure solves this by loading instructions only when a skill is actually triggered.

## How SKILL.md Implements Progressive Disclosure

The [SKILL.md specification](https://agentskills.io/specification) uses a two-stage approach:

### Stage 1: Metadata (Always Loaded)

Only the YAML frontmatter is read to determine when a skill should be used:

```yaml
---
name: skill-name
description: "Clear description of what the skill does and when to use it"
---
```

This minimal metadata allows Claude to:
- Identify available skills
- Match user requests to appropriate skills
- Decide whether to trigger a skill

### Stage 2: Instructions (Loaded on Trigger)

The full Markdown body is loaded **only after** the skill is triggered:

```markdown
---
name: skill-name
description: "What the skill does"
---

# Skill Name

## Detailed Instructions

Full procedural guidance, workflows, examples...

## References

Links to bundled resources, scripts, assets...
```

## Benefits of This Approach

| Benefit | Description |
|---------|-------------|
| **Context efficiency** | Only active skills consume context window space |
| **Scalability** | Many skills can be available without overwhelming context |
| **Responsiveness** | Quick skill matching without loading unnecessary content |
| **Flexibility** | Skills can have extensive instructions without penalty until needed |

## Implications for Skill Design

### Frontmatter Design

The `description` field is critical because it's the **only information** Claude uses to decide whether to trigger a skill. It should be:

- **Comprehensive** - Cover all use cases when the skill applies
- **Clear** - Unambiguous about the skill's purpose
- **Concise** - Efficient use of always-loaded context

```yaml
# Good: Clear trigger conditions
description: "Guide for creating effective skills. Use when users want to create a new skill or update an existing skill."

# Bad: Too vague
description: "Helps with skills"
```

### Body Design

Since the body is only loaded when needed, it can be more extensive. However, the [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) guidance still recommends conciseness:

> "The context window is a public good. Only add context Claude doesn't already have."

### Using References for Large Content

For extensive documentation, use the `references/` directory:

```
skill-name/
├── SKILL.md
└── references/
    ├── detailed-guide.md
    └── api-docs.md
```

The SKILL.md can then instruct Claude to load references as needed, implementing a **third level** of progressive disclosure.

## Example: Three-Level Disclosure

```
skill-name/
├── SKILL.md
│   ├── Frontmatter (Level 1 - always loaded)
│   │   ├── name
│   │   └── description
│   └── Body (Level 2 - loaded on trigger)
│       └── Instructions referencing...
└── references/ (Level 3 - loaded on demand)
    └── detailed-docs.md
```

| Level | Content | When Loaded |
|-------|---------|-------------|
| 1 | Frontmatter (`name`, `description`) | Always - for skill matching |
| 2 | SKILL.md body | When skill is triggered |
| 3 | References directory | When Claude determines it's needed |

## Comparison with Other Patterns

### Traditional API Documentation

- Loads all documentation upfront
- Suitable for human readers with unlimited time
- Not context-efficient for AI

### Progressive Disclosure in SKILL.md

- Metadata always available for matching
- Instructions loaded on demand
- References loaded when specifically needed
- Optimized for limited context windows

## Best Practices

1. **Write descriptive frontmatter** - It's the only thing Claude sees until the skill triggers
2. **Keep SKILL.md focused** - Core procedures and workflows
3. **Use references for details** - API docs, schemas, extensive examples
4. **Avoid duplication** - Information should live in one place only
5. **Consider token cost** - Every piece of information should justify its context usage

## Further Reading

- [SKILL.md Specification](https://agentskills.io/specification) - Verified on 2025-12-28
- [skill-creator skill](https://github.com/anthropics/skills/tree/main/skills/skill-creator) - Official guidance on creating skills - Verified on 2025-12-28
- [AI-Generated Skills](../ai-generated-skills/) - How skills in this repository were created

---

> **Note**: Progressive disclosure is a key principle that makes the skill system scalable. Understanding it helps you create better skills and use existing skills more effectively.
