---
title: "Documentation"
linkTitle: "Docs"
weight: 1
---

Welcome to the AI Config documentation. This section covers standards for sharing AI agents and skills, as well as the skills available in this collection.

## Standards for Sharing Agents and Skills

The AI ecosystem has several emerging standards for describing and sharing agents, skills, and context. In December 2025, the [Linux Foundation announced the Agentic AI Foundation (AAIF)](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) to govern several of these standards.

### Agent Standards

| Standard | Purpose | Format | Link |
|----------|---------|--------|------|
| **AGENTS.md** | Project-specific guidance for AI coding agents | Markdown | [AAIF](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) |
| **Agent Manifest** (ADS) | Describes autonomous AI agents capabilities, authentication, and execution | `manifest.json` | [agent-manifest.org](https://agent-manifest.org/) |
| **Open Agent Specification** | Framework-agnostic declarative agent specification | YAML/JSON | [Oracle Blog](https://blogs.oracle.com/ai-and-datascience/introducing-open-agent-specification) |
| **OASF** | Open Agentic Schema Framework for agent interoperability | JSON Schema | [AGNTCY](https://intuitionlabs.ai/articles/agentic-ai-foundation-open-standards) |

### Skill Standards

| Standard | Purpose | Format | Link |
|----------|---------|--------|------|
| **Agent Skills** (SKILL.md) | Human-readable skill instructions for AI assistants | Markdown + YAML | [agentskills.io](https://agentskills.io/) |
| **Skill Manifest** | Bot skills with endpoints, activities, and I/O schemas | `skills-manifest.json` | [Microsoft Bot Framework](https://learn.microsoft.com/en-us/azure/bot-service/skills-write-manifest) |
| **GPT Actions** | API integration for ChatGPT custom GPTs | OpenAPI 3.1.0 | [OpenAI Platform](https://platform.openai.com/docs/actions/introduction) |

### Context & Communication Protocols

| Standard | Purpose | Format | Link |
|----------|---------|--------|------|
| **MCP** | Model Context Protocol for agent-to-tool communication | JSON-RPC | [modelcontextprotocol.io](https://modelcontextprotocol.io/specification/2025-06-18) |
| **llms.txt** | Website content structured for LLM consumption | Markdown | [llmstxt.org](https://llmstxt.org/) |

### Knowledge Standards

Standards for sharing knowledge, data, and models between AI systems and agents.

| Standard | Purpose | Format | Link |
|----------|---------|--------|------|
| **IEEE 3404-2025** | Standard for data and model sharing between federated machine learning systems | Specification | [IEEE](https://standards.ieee.org/ieee/3404/11360/) |
| **A2A Protocol** | Agent-to-Agent protocol for agent discovery and knowledge exchange | JSON | [Google A2A](https://github.com/google/A2A) |
| **ISO/IEC 22989** | AI concepts and terminology standard | ISO Standard | [ISO](https://www.iso.org/standard/74296.html) |
| **ISO/IEC 42001** | AI management system requirements | ISO Standard | [ISO](https://www.iso.org/standard/81230.html) |
| **RAG Patterns** | Retrieval-Augmented Generation for knowledge integration | De facto practices | Various implementations |

### Summary

- **AGENTS.md** - OpenAI standard adopted by 60,000+ projects; provides project-specific agent guidance
- **Agent Skills / SKILL.md** - Anthropic standard adopted by Microsoft, OpenAI, Atlassian, Figma, Cursor, GitHub
- **MCP** - De facto standard for agent-to-tool communication with 97M+ monthly SDK downloads
- **GPT Actions** - OpenAI's OpenAPI-based format for ChatGPT integrations
- **llms.txt** - Emerging standard for making website content LLM-friendly

---

> **Note:** This documentation was created with AI assistance. Some content may be experimental or untested. Always verify information before use in production environments.
