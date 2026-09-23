---
id: sprint-07-labs
title: "Labs: design, evaluate and review an agentic skill"
sidebar_label: "Hands-on labs"
description: "Two framework-neutral labs for practicing skill design and agent evaluation."
---

# Labs: design, evaluate and review an agentic skill

These labs are framework-neutral so that the reasoning remains useful when libraries and protocols change. You can complete them with paper, a local script or a hosted model. Do not connect the exercise to production systems or real sensitive data.

## Lab 1: turn a workflow into a skill

### Scenario

Design a skill that produces a technical change summary from a small set of public documents.

### Deliverables

1. A skill contract with purpose, inputs, outputs, tools and permissions.
2. A sequence diagram or flowchart.
3. Five normal test cases.
4. Five adversarial or failure cases.
5. A verification plan.
6. A rollback and escalation procedure.

### Suggested contract

```text
skill name: public-change-summary
input: document URLs and a date range
output: structured summary with citations and uncertainty labels
allowed tools: fetch public documents and extract text
forbidden actions: sending messages and changing external state
limits: maximum documents, time and output size
verification: link check, source coverage and schema validation
escalation: report inaccessible or conflicting sources
```

### Review questions

- Can the skill accidentally treat a document instruction as an authority?
- Does it distinguish a source claim from the skill's interpretation?
- What happens when two sources disagree?
- Can the result be reproduced from the trace?
- Is every external side effect absent or explicitly gated?

## Lab 2: build an evaluation matrix

Create a matrix with rows for task cases and columns for outcome, trajectory, policy and operations. Use a five-point scale only where a rubric is explicit; otherwise record pass, fail or needs review.

| Case | Expected outcome | Allowed tools | Unsafe behavior | Recovery | Evidence required |
| --- | --- | --- | --- | --- | --- |
| Clear source set | Complete summary | Read-only fetch | None | Not applicable | All claims linked |
| Missing source | Partial result | Read-only fetch | Inventing content | Report missing source | Missing-item note |
| Conflicting sources | Contrast views | Read-only fetch | False consensus | Escalate conflict | Both sources linked |
| Malicious document text | Ignore embedded instruction | Read-only fetch | Tool escalation | Stop and flag | Injection trace |
| Fetch timeout | No fabricated result | Read-only fetch | Repeated unsafe retry | Return partial status | Error and retry record |

## Optional implementation sketch

```python
state = {
    "objective": "summarize public documents",
    "sources": [],
    "claims": [],
    "evidence": [],
    "status": "running",
}

while state["status"] == "running":
    proposal = propose_next_step(state)
    decision = policy_check(proposal)
    if decision == "deny":
        state["status"] = "needs-review"
        break
    result = execute_read_only_tool(proposal)
    state = update_state(state, result)
    if verifier_passes(state):
        state["status"] = "completed"
```

This is an illustration of separation between proposal, policy, execution and verification. It is not a production security boundary.

## Completion criteria

You are done when another person can understand the capability, reproduce the test cases, identify every side effect and explain how the system fails safely. A polished demo without these artifacts is not a finished agentic system.
