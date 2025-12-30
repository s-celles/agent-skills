---
title: "AI Limitations and Best Practices"
linkTitle: "AI Limitations"
weight: 50
description: "Understanding AI limitations and how to use AI-generated content responsibly."
---

## AI Systems Can Make Mistakes

Large Language Models (LLMs) like Claude, GPT, and others are powerful tools, but they have inherent limitations that users should understand:

### Common AI Limitations

| Limitation | Description |
|------------|-------------|
| **Hallucinations** | AI can generate plausible-sounding but factually incorrect information |
| **Outdated information** | Training data has a cutoff date; AI may not know recent developments |
| **Lack of real-time access** | Without tools, AI cannot verify current facts or access live data |
| **Context window limits** | Very long conversations or documents may exceed processing capacity |
| **Reasoning errors** | Complex multi-step reasoning can produce incorrect conclusions |
| **Bias** | Training data biases can affect outputs |

### Why This Matters for AI Config

The skills and agents in this repository were created with AI assistance. While we strive for accuracy, the content may contain:

- Incorrect or outdated information about licenses, standards, or procedures
- Oversimplified guidance that doesn't account for edge cases
- References to resources that have moved or changed
- Recommendations that may not apply to your specific jurisdiction or context

## Best Practices for Using AI-Generated Content

### 1. Always Verify Critical Information

Before making important decisions based on AI-generated content:

- **Cross-reference** with authoritative sources
- **Consult professionals** for legal, medical, financial, or academic matters
- **Test thoroughly** before using in production environments

### 2. Authoritative Sources by Domain

| Domain | Authoritative Sources |
|--------|----------------------|
| **Open Source Licensing** | [OSI](https://opensource.org/licenses), [FSF](https://www.gnu.org/licenses/), [SPDX](https://spdx.org/licenses/) |
| **Creative Commons** | [Creative Commons Official](https://creativecommons.org/licenses/) |
| **French Legal Context** | [Légifrance](https://www.legifrance.gouv.fr/), [CNIL](https://www.cnil.fr/) |
| **Academic Standards (France)** | [Ministère de l'Enseignement Supérieur](https://www.enseignementsup-recherche.gouv.fr/) |
| **AI Standards** | [ISO/IEC JTC 1/SC 42](https://www.iso.org/committee/6794475.html), [IEEE](https://standards.ieee.org/) |
| **API Documentation** | Always prefer official documentation over AI summaries |

### 3. Report Errors

If you find inaccuracies in this repository:

1. [Open an issue](https://github.com/s-celles/ai-config/issues) on GitHub
2. Provide the correct information with authoritative sources
3. We will review and update the content

## AI Transparency Metadata for Skills

The official [Agent Skills specification](https://agentskills.io/specification) only requires `name` and `description` fields. However, this repository uses extended metadata for AI transparency.

> **Note:** We have proposed these extended metadata fields to the official specification in [anthropics/skills#180](https://github.com/anthropics/skills/issues/180).

```yaml
---
# Required by specification
name: skill-name
description: "What the skill does"

# Extended metadata (optional, used in this repository)
version: "1.0.0"                 # Semantic Versioning (MAJOR.MINOR.PATCH)
status: tested | experimental    # Indicates testing level
author: "Name or handle"         # Human author/maintainer
generated_by: "Claude Opus 4.5"  # AI model used for generation
license: MIT                     # License for the skill itself
disclaimer: "This skill provides informational guidance only and does not constitute professional advice."
---
```

| Field | Required | Purpose |
|-------|----------|---------|
| `name` | Yes | Skill identifier |
| `description` | Yes | What the skill does |
| `version` | No | [Semantic Versioning](https://semver.org/) format (MAJOR.MINOR.PATCH) |
| `status` | No | `tested` or `experimental` - indicates reliability level |
| `author` | No | Human responsible for the skill |
| `generated_by` | No | AI model used to create/assist with the skill |
| `license` | No | License under which the skill is shared |
| `disclaimer` | No | Skill-specific disclaimer about limitations and appropriate use |

This extended metadata helps users understand the provenance and reliability of each skill.

## Understanding AI Transparency

This repository follows transparency principles:

- **Disclosure**: All content created with AI assistance is clearly marked
- **Model identification**: We specify which AI model was used (Claude Opus 4.5)
- **Limitations acknowledged**: We don't claim AI-generated content is error-free
- **Human oversight**: Content is reviewed but may still contain errors

## Further Reading

For more information about AI limitations and responsible use:

- [Anthropic's Claude Documentation](https://docs.anthropic.com/) - Verified on 2025-12-28
- [OpenAI's Usage Policies](https://openai.com/policies/usage-policies) - Verified on 2025-12-28
- [EU AI Act](https://artificialintelligenceact.eu/) - Verified on 2025-12-28
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Verified on 2025-12-28

---

> **Remember**: AI is a tool to augment human capabilities, not replace human judgment. Always apply critical thinking when using AI-generated content.
