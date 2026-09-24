---
id: closed-loop-lab
title: "Lab: design a bounded closed loop"
sidebar_label: "Lab: design a bounded closed loop"
description: "A paper and simulation exercise for designing, evaluating and governing a safe network automation loop."
---

# Lab: design a bounded closed loop

## Objective

Design a small loop that responds to a rising service symptom without turning a forecast into an uncontrolled production change. The lab is conceptual and can be completed with a spreadsheet or a short script.

## Scenario

A service region shows increasing session-establishment latency during a recurring demand window. You have time-series measurements, instance saturation, dependency health, recent changes, available capacity and a small set of historical incidents.

Your loop may recommend or execute one action: add capacity in a bounded scope. It must preserve redundancy, avoid repeated oscillation and stop when evidence is insufficient.

## Step 1: define the objective

Write the target in observable terms. For example:

- target metric: 95th-percentile session-establishment latency;
- scope: one region and one service class;
- window: the next demand interval;
- constraint: preserve minimum zone redundancy;
- budget: maximum capacity increase;
- expiry: the recommendation becomes invalid after the demand window.

Do not use “improve performance” as the objective.

## Step 2: define the evidence contract

List the minimum evidence required before a decision:

| Evidence | Freshness | Why it matters |
|---|---|---|
| target latency | short | confirms the symptom |
| request rate | short | distinguishes demand from dependency failure |
| error and timeout rate | short | identifies impact |
| instance saturation | short | tests capacity hypothesis |
| dependency health | short | avoids scaling the wrong component |
| topology and redundancy | current | constrains placement |
| recent changes | current | tests change-related cause |

If a critical field is missing, the loop should explain or escalate instead of acting.

## Step 3: define the action contract

Specify the exact action, scope, budget, duration, authorization and rollback. Make the action idempotent: repeating the same request should not create unbounded capacity.

## Step 4: add a guardrail

Use a simple policy such as:

- act only when the target symptom persists across two windows;
- require dependency health to be within bounds;
- cap the capacity delta;
- preserve at least two healthy zones;
- allow only one action per dwell period;
- roll back when the target does not improve or a side effect crosses a threshold.

The guardrail is intentionally deterministic.

## Step 5: define verification

Measure the target outcome and side effects:

- target latency;
- error and timeout rates;
- capacity headroom;
- zone and instance health;
- unaffected service classes;
- cost or resource impact.

Compare the result with the predicted range. Do not call the action successful merely because the metric moved in the desired direction.

## Step 6: write the loop

```text
observe evidence
if critical evidence is missing:
    explain missing evidence and escalate
else if symptom is not persistent:
    continue observing
else if constraints are not satisfied:
    recommend investigation
else:
    propose bounded action
    pass through authorization gate
    execute idempotent change
    verify target and side effects
    rollback or escalate when verification fails
```

## Step 7: evaluate it

Create at least four test cases:

1. normal demand with no action;
2. genuine capacity pressure where action helps;
3. dependency failure where scaling is the wrong action;
4. missing telemetry where the loop must abstain.

For each case, record the decision, evidence, action, result and safe fallback.

## Reflection

What would make you move this loop from recommendation to guarded act? Which failure would be most dangerous: a false positive, a false negative, a delayed action or an action that cannot be reversed?

## Extension

Replace the deterministic detector with a forecasting model. Keep the policy gate and verification unchanged. Compare the operational behavior, not only forecast accuracy.
