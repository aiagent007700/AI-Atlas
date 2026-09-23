---
id: sprint-07-references
title: "Reference shelf: agents, skills and protocols"
sidebar_label: "Reference shelf"
description: "Curated external references for learning and implementing agentic systems."
---

# Reference shelf: agents, skills and protocols

This shelf favors primary specifications, official documentation and maintained repositories. Links are organized by purpose rather than popularity. A project being listed here does not mean it is secure, production-ready or suitable for every use case.

## Canonical and protocol references

| Resource | Type | Why it is useful | Caveat |
| --- | --- | --- | --- |
| [Model Context Protocol specification](https://modelcontextprotocol.io/specification/2026-07-28) | Specification | Defines a tool and context integration boundary | Check the current specification version |
| [MCP getting started guide](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro) | Official documentation | Gives the conceptual host, client and server model | Examples may evolve with the protocol |
| [Google A2A announcement](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) | Official industry input | Explains the goal of agent-to-agent interoperability | An announcement is not a conformance test |
| [A2A project](https://github.com/a2aproject/A2A) | Open-source repository | Tracks implementation and specification work | Review releases and governance before adoption |

## Orchestration and implementation

| Resource | Type | Why it is useful | Caveat |
| --- | --- | --- | --- |
| [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) | Official documentation | Explains stateful graphs, durable execution and human review | Framework concepts are not universal standards |
| [LangGraph repository](https://github.com/langchain-ai/langgraph) | Maintained repository | Provides a concrete graph-orchestration implementation | Inspect license, releases and security advisories |
| [Google ADK](https://adk.dev/) | Official documentation | Provides code-first agent and multi-agent examples | Optimized integrations may reflect its ecosystem |
| [Google ADK API reference](https://adk.dev/api-reference/) | API reference | Useful for precise implementation details | API details can change between versions |

## Evaluation, telemetry and security

| Resource | Type | Why it is useful | Caveat |
| --- | --- | --- | --- |
| [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) | Open observability reference | Helps structure model and agent telemetry | Instrumentation does not guarantee good governance |
| [OWASP AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) | Security guidance | Catalogues practical agent risks and controls | Apply controls to the actual threat model |
| [OWASP Agent Observability Standard](https://owasp.org/www-project-agent-observability-standard-2/) | Security and observability project | Connects instrumentability with agent oversight | Check project maturity and version status |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | Open-source implementation | Useful for tracing and evaluation experiments | Treat it as an implementation option, not a standard |
| [NVIDIA agent evaluation guide](https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/) | Practical technical article | Discusses tool calls and task completion | Vendor-authored guidance should be compared with other sources |
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | Government framework | Provides broader risk-management context | It is a framework, not a substitute for engineering controls |

## How to assess a new reference

Before adding a project or article to the shelf, check:

- Is the publisher identifiable?
- Is the source close to the original work?
- Is the repository active enough for the proposed use?
- Are releases, license and security practices visible?
- Does the source distinguish evidence from marketing?
- Can a reader reproduce the relevant claim?
- Is there a more authoritative source that should be linked first?

**Last checked:** 2026-09-23. Recheck links and versions when this sprint is refreshed.
