---
id: assurance-in-practice
title: "Assurance in practice"
sidebar_position: 6
---

# Assurance in practice

Assurance is the disciplined argument that a system is appropriate for a defined use, supported by evidence, with known residual risk and a plan for what happens when assumptions fail.

## Build an assurance case

A compact assurance case has five parts:

1. **Claim** — what the system is expected to do safely.
2. **Context** — where, for whom, and under which constraints.
3. **Argument** — why the controls support the claim.
4. **Evidence** — tests, observations, reviews, and records.
5. **Residual risk** — what remains uncertain and who accepted it.

## Example claim pattern

> For a defined user group and a bounded set of tasks, the assistant will not execute high-impact actions without an authorized approval signal.

Supporting evidence might include authorization tests, adversarial tests, tool-call logs, approval records, and rollback exercises. A general statement such as “the model is aligned” is not evidence for this claim.

## Release gates

A practical release gate can ask:

- Are the intended and excluded uses written down?
- Are permissions tested at the retrieval and action boundaries?
- Are representative and adversarial evaluations complete?
- Is uncertainty visible where it changes the decision?
- Can an operator stop or reverse the system?
- Are logs sufficient for investigation without creating a new privacy problem?
- Is there an owner for every unresolved high-severity risk?

## Monitor the assumptions

The assurance case should identify signals that invalidate it:

- New data sources or tools
- Changes in user population
- Quality or safety drift
- New attack patterns
- Increased autonomy or action scope
- Regulatory or contractual changes
- Incident trends or repeated overrides

## Final question

A model can be safe in isolation and unsafe in a workflow. The unit of assurance should therefore be the deployed system and its operating context, not only the model artifact.
