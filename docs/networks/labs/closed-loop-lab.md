---
id: closed-loop-lab
title: "Lab: design a safe closed loop"
sidebar_label: "Lab: safe closed loop"
description: "A practical exercise for designing, evaluating and governing an AI-assisted telecom control loop."
---

# Lab: design a safe closed loop

## Scenario

A hypothetical service experiences rising session-establishment failures during a planned regional event. You have access to procedure metrics, service latency, capacity data, topology, deployment history and recent operator changes. Your team wants an AI-assisted system that can detect the issue, recommend a response and eventually automate a bounded action.

The exercise is intentionally model-agnostic. The goal is to design the operating loop before choosing an algorithm.

## Part 1: define the outcome

Write a service-level objective for the event. Include:

* population and geography
* measurement window
* success threshold
* acceptable latency and availability
* resilience requirement
* cost or capacity boundary

Avoid “optimize the network” as an objective. It is not measurable enough to govern an action.

## Part 2: define evidence

List the signals needed to distinguish:

* genuine demand growth
* a control-plane bottleneck
* a user-plane path issue
* a policy or configuration change
* a telemetry problem

For each signal, record its owner, freshness, expected delay, known gaps and whether it is authoritative or corroborating.

## Part 3: define the action space

Separate actions into three groups:

* read-only analysis
* reversible automated actions
* actions requiring approval

For each action, specify preconditions, blast radius, rollback method, verification signal and maximum duration.

## Part 4: choose an intelligence pattern

Select one or more patterns:

* rules for hard boundaries
* anomaly detection for candidate events
* retrieval for procedures and change history
* forecasting for near-term load
* optimization for constrained resource decisions
* an agentic workflow for evidence collection and handoffs

Explain why the pattern fits the decision deadline and evidence quality.

## Part 5: design the evaluation

Define offline and operational metrics:

* detection precision and recall
* forecast calibration and lead time
* recommendation acceptance rate
* false-action rate
* time to recovery
* customer-impact reduction
* rollback frequency
* operator workload

Do not use model accuracy as the only success criterion. The system exists to improve a service outcome under constraints.

## Part 6: define the rollout

Use progressive autonomy:

1. shadow mode
2. operator-facing recommendation
3. approval-gated execution
4. bounded automatic execution
5. periodic policy and model review

Define a kill switch, an escalation path and the evidence required to advance between stages.

## Deliverable

Produce a one-page design containing:

* loop diagram
* intent and constraints
* evidence map
* action matrix
* evaluation plan
* rollout gates
* failure and recovery plan

Compare your design with the [closed-loop automation](../autonomy/closed-loop-automation), [Packet Core AI use cases](../packet-core/packet-core-ai-use-cases) and [AIOps and SRE](../operations/aiops-and-sre) chapters.
