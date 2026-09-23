---
id: trustworthy-ai-system-map
title: "Visual map: the trustworthy AI system"
sidebar_position: 7
---

# Visual map: the trustworthy AI system

The diagram separates capability from authority. The model can propose an answer or action, but policy, identity, and operational controls determine what may happen next.

```mermaid
flowchart LR
    U[User or event] --> I[Identity and intent]
    I --> P[Policy and authorization]
    P --> A[Application workflow]
    A --> M[Model and reasoning]
    A --> R[Retrieval and data]
    M --> D[Proposed answer or action]
    R --> D
    D --> G[Guardrails and validation]
    G --> H{High impact?}
    H -->|No| X[Constrained execution]
    H -->|Yes| V[Approval or human review]
    V --> X
    X --> O[External side effect]
    O --> L[Logs, monitoring, and incident response]
    L --> P
```

## How to read it

- Identity and policy establish authority.
- Retrieval supplies evidence but does not grant permission.
- The model proposes; validation constrains.
- High-impact actions receive stronger friction.
- Monitoring closes the loop by turning incidents into changed controls.

## Design prompt

For the AI system you are studying, mark every point where untrusted content can enter and every point where a side effect can occur. The distance between those points is where many useful controls can be placed.
