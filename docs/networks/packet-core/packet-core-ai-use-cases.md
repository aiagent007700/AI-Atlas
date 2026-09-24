---
id: packet-core-ai-use-cases
title: "AI use cases in Packet Core"
sidebar_label: "AI use cases in Packet Core"
description: "A decision-centric framework for selecting, evaluating and governing AI use cases in Packet Core operations."
---

# AI use cases in Packet Core

## Start with the decision

A use case should name the operational decision before it names the model. Examples include:

- detect a degradation;
- explain a procedure failure;
- forecast demand;
- recommend capacity or placement;
- optimize policy under constraints;
- automate a known, reversible remediation.

The model follows the decision. A time-series model may forecast load. A graph method may rank dependencies. Retrieval may assemble procedure and change evidence. An optimizer may allocate capacity. An agent may coordinate tools, but it still needs an explicit action boundary.

## Decision matrix

| Decision | Evidence | Candidate approach | Initial autonomy level | Safety boundary |
|---|---|---|---|---|
| Detect signaling degradation | rates, latency, errors, dependency health | anomaly detection | observe | require corroboration |
| Explain session failures | traces, procedures, versions, policy | retrieval and investigation | explain | cite evidence and uncertainty |
| Forecast demand | load, mobility, events, seasonality | time-series forecasting | recommend | confidence interval and budget |
| Recommend UPF placement | topology, latency, capacity, resilience | constrained optimization | recommend | preserve redundancy |
| Tune policy | QoS outcomes, subscription and class | policy analysis | guarded act | hard limits and approval |
| Remediate known fault | runbook, health signals and change history | workflow automation | closed loop | idempotence and verification |

## A worked example: predictive capacity recommendation

Assume the system predicts that session-management capacity will become constrained during an event window.

### Evidence contract

The input set should include current load, historical comparable windows, recent changes, dependency health, topology, available capacity, placement constraints and the confidence interval. The system should reject the recommendation when key evidence is stale or missing.

### Decision contract

The proposal should state the target function, location, capacity delta, expected benefit, cost, redundancy impact, expiry time and rollback condition. A recommendation without an expiry can become an unintended permanent policy.

### Verification contract

After execution, measure the target latency, error rate, capacity headroom, dependency health and unaffected cohorts. Compare the observed result with the predicted range. If the benefit does not appear, stop and investigate rather than repeatedly increasing the action.

## RAG for operations

A network operations assistant may retrieve procedures, topology context, change records, runbooks, incident history and current policy. Retrieval must preserve scope, time and provenance. A procedure for an older software version should not silently outrank the current operational contract.

A useful response format is:

1. observed facts;
2. likely hypotheses;
3. missing evidence;
4. next diagnostic check;
5. permitted action;
6. verification plan.

This format makes a fluent narrative auditable.

## Evaluation beyond prediction accuracy

Evaluate the whole decision system:

- detection precision and recall;
- lead time and warning stability;
- forecast calibration and tail error;
- recommendation acceptance rate;
- avoided incidents or reduced toil;
- false-action cost;
- rollback frequency;
- time to recovery;
- fairness across services, regions or cohorts;
- operator trust and override behavior.

A model can improve a benchmark while making operations worse if its outputs are noisy, expensive or difficult to reverse.

## Maturity path

- **Observe:** analysis only.
- **Assist:** recommendation with evidence.
- **Guarded act:** narrow, reversible action under policy.
- **Closed loop:** execute, verify and stop within a bounded domain.
- **Adaptive autonomy:** strategy updates through controlled change management.

Moving upward requires evidence from realistic failure and recovery scenarios.

## Failure modes

- optimizing a proxy that is not the service objective;
- training on normal traffic and failing during events;
- confusing correlation with cause;
- acting on stale topology or policy;
- allowing one model to control multiple conflicting actuators;
- measuring the model but not the operational outcome.

## Exercise

Choose one Packet Core decision. Write its evidence, action space, constraints, expected benefit, false-positive cost, false-negative cost, verification signal and safe fallback. Decide whether the first release should be a dashboard, assistant, workflow or closed loop.

## Further reading

- [3GPP specifications](https://www.3gpp.org/DynaReport/)
- [ITU-T machine learning for future networks](https://www.itu.int/en/ITU-T/focusgroups/ml5g/pages/default.aspx)
- [ETSI ZSM](https://www.etsi.org/technical-groups/zsm/)
