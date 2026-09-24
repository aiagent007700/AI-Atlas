---
id: packet-core-ai-use-cases
title: "AI use cases in Packet Core"
sidebar_label: "AI use cases in Packet Core"
description: "A practical framework for selecting AI use cases in 5G Core operations and separating assistance from autonomous control."
---

# AI use cases in Packet Core

## Start with the decision, not the model

A good use-case description begins with an operational decision:

* detect a degradation
* explain a change in behavior
* forecast demand
* recommend capacity or placement
* optimize policy under constraints
* automate a reversible remediation

Only then should the team choose a model. A large language model may help summarize evidence or translate an operator question. A time-series model may forecast load. A graph model may rank likely dependencies. A constrained optimizer may allocate resources. One system can combine them, but the interfaces and evaluation criteria should remain explicit.

## Use-case matrix

| Decision | Useful evidence | Candidate technique | Safety boundary |
|---|---|---|---|
| Detect signaling degradation | request rates, latency, errors, dependency health | anomaly detection | alert first; no automatic change from one signal |
| Forecast demand | historical load, events, mobility, seasonality | time-series forecasting | confidence interval and capacity budget |
| Explain session failures | traces, procedure outcomes, policy versions | retrieval and causal investigation | cite evidence and show uncertainty |
| Recommend UPF placement | topology, latency, capacity, resilience | constrained optimization | preserve redundancy and rollback |
| Tune policy | QoS outcomes, subscriptions, traffic class | policy analysis | hard limits and approval gates |
| Remediate a known fault | runbook, health signals, change history | workflow automation | idempotence and post-change verification |

The table is intentionally conservative. The most valuable early systems often improve diagnosis and decision quality before they control the network.

## RAG for network operations

A network operations assistant can retrieve procedure documents, topology context, change records, runbooks and recent incidents. The retrieval system should preserve time, scope and provenance. A procedure from an old software version should not silently outrank a current operational policy.

A useful answer format is:

1. observed facts
2. likely hypotheses
3. missing evidence
4. recommended next check
5. permitted action
6. verification plan

This structure prevents a fluent narrative from being mistaken for a completed diagnosis.

## Forecasting and capacity

Forecasting systems should be evaluated across the conditions in which they will be used: ordinary days, planned events, sudden shifts and partial telemetry loss. Average error is not enough. Tail error, calibration, lead time and operational cost matter.

If a forecast drives scaling, include the cost of false positives and false negatives. A model that is statistically better can still be operationally worse if it produces decisions that are expensive, slow or difficult to reverse.

## From recommendation to control

Use a graduated autonomy path:

* **Observe:** model produces analysis only.
* **Assist:** model recommends an action to an operator.
* **Guarded act:** system executes a narrow reversible action under policy.
* **Closed loop:** system executes, verifies and learns within a bounded domain.
* **Adaptive autonomy:** system can update its strategy, but only through controlled change management.

Moving upward requires evidence, not enthusiasm. Each level should define exit criteria, incident handling and a way to disable the automation.

## Exercise

Choose one Packet Core use case. Define:

* the decision owner
* the observation window
* the minimum evidence set
* the action space
* the cost of a false positive
* the cost of a false negative
* the verification signal
* the safe fallback

Then decide whether the first release should be a dashboard, an assistant, a workflow or a closed loop.

## Further reading

* [3GPP specifications](https://www.3gpp.org/DynaReport/): normative specifications for system architecture, procedures and management.
* [ITU-T ML5G deliverables](https://www.itu.int/en/ITU-T/focusgroups/ml5g/Documents/ML5G-delievrables.pdf): architectural material for ML in future networks.
