---
id: sprint-07-multi-agent
title: "Multi-agent systems: delegation without chaos"
sidebar_label: "Multi-agent systems"
description: "Patterns, trade-offs and failure modes for systems that delegate work among agents."
---

# Multi-agent systems: delegation without chaos

Multiple agents can make a system easier to organize, but they do not automatically make it more capable. Splitting one difficult task into several conversations adds coordination, serialization, identity and recovery costs. A multi-agent design is justified when specialization or isolation produces measurable value.

## Common patterns

| Pattern | Strength | Typical risk |
| --- | --- | --- |
| Supervisor and specialists | Centralized routing and review | Supervisor bottleneck |
| Sequential handoff | Clear stage boundaries | Context loss between stages |
| Parallel specialists | Faster independent analysis | Conflicting results and higher cost |
| Debate or critique | Exposes alternative reasoning | Performative disagreement |
| Swarm or peer delegation | Flexible discovery | Difficult accountability |
| Hierarchical planning | Handles larger decomposition | Deep failure cascades |

## A coordination contract

Every delegation should answer four questions:

1. What is the remote agent responsible for?
2. What information may it receive?
3. What result must it return?
4. What happens if it is late, wrong or unavailable?

A result should include evidence and status, not only prose. Use typed task states such as `accepted`, `running`, `needs-input`, `completed`, `failed` and `cancelled`.

## Avoiding emergent ambiguity

Ambiguity grows when several agents can modify the same shared state. Prefer ownership rules:

- One agent owns a resource at a time.
- Writes are serialized or transactionally guarded.
- Read and write permissions are separate.
- Every mutation has a causal trace.
- Conflicting proposals go to a resolver with explicit policy.

Shared memory is not automatically shared truth. Record provenance, freshness and authority for every persistent item.

## Cost model

Suppose a single agent run makes `n` model calls. Adding `k` specialists can produce more than `k` calls because each specialist needs context, the coordinator needs summaries, and failed branches may be retried. Measure total task cost and latency, not only the quality of the best sub-answer.

A useful baseline is the simplest single-agent or deterministic workflow. Compare the multi-agent design against that baseline on the same evaluation set.

## Example: architecture review

A supervisor can ask separate specialists to inspect reliability, security and operability. Each specialist returns findings with evidence and severity. A deterministic merger groups duplicate findings, checks that every claim has evidence and produces a review packet. A human approves any recommendation that changes production architecture.

The specialists do not need to debate indefinitely. Their contract defines a bounded number of passes and a clear escalation path for disagreement.

## Thought experiment

If three agents independently produce the same incorrect answer, has the system gained confidence or only correlated error? Independence must be tested, not assumed. Shared model versions, prompts, retrieval sources and memory can make apparently separate agents behave as one system.

## Further reading

- [Google ADK multi-agent documentation](https://adk.dev/) — a maintained framework reference for composition patterns.
- [LangGraph repository](https://github.com/langchain-ai/langgraph) — graph-based orchestration implementation.
- [A2A project repository](https://github.com/a2aproject/A2A) — agent-to-agent interoperability implementation reference.
