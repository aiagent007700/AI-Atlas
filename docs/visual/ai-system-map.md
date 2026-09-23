---
id: ai-system-map
slug: /visual/ai-system-map
title: "Visual map: an AI system is more than a model"
sidebar_position: 1
description: A visual reference for connecting models, data, retrieval, agents, controls, and operations.
---

# Visual map: an AI system is more than a model

Use this map whenever a conversation jumps directly from “which model?” to “how do we deploy it?” The missing layers are usually where the real design work lives.

```mermaid
flowchart TB
    subgraph Experience[Experience layer]
        U[User or application]
        W[Workflow and UX]
    end

    subgraph Intelligence[Intelligence layer]
        M[Foundation or specialist model]
        R[Retrieval and knowledge]
        A[Agent or workflow controller]
        T[Tools and external systems]
    end

    subgraph Control[Control layer]
        P[Policy and permissions]
        V[Validation and verification]
        H[Human review and escalation]
    end

    subgraph Operations[Operations layer]
        O[Observability]
        E[Evaluation]
        L[Lifecycle and release management]
    end

    U --> W --> A
    A --> M
    A --> R
    A --> T
    P --> A
    P --> T
    M --> V
    R --> V
    T --> V
    V --> W
    V --> H
    O -. telemetry .-> M
    O -. telemetry .-> A
    O -. telemetry .-> T
    E -. test and compare .-> M
    E -. test and compare .-> A
    L -. version and rollback .-> M
    L -. version and rollback .-> A
```

## How to read it

* The **experience layer** defines the user’s actual task.
* The **intelligence layer** supplies prediction, retrieval, planning, and action.
* The **control layer** limits what can happen and detects what went wrong.
* The **operations layer** makes the system changeable, observable, and accountable.

The layers are not strictly sequential. They form a feedback system.

## The design test

For any proposed AI feature, identify:

1. The user decision or workflow being improved
2. The model capability required
3. The data and retrieval path
4. The tools and permissions involved
5. The verification and escalation path
6. The metrics that determine whether to keep it

If any answer is missing, the feature is probably still a demo rather than a system design.
