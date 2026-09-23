---
id: production-ai-system-map
title: Production AI system map
sidebar_label: Production AI system map
---

# Production AI system map

This map shows why production AI is a system problem. The model is important, but it is one component in a loop that includes data, runtime controls, evaluation, and feedback.

```mermaid
flowchart TB
    subgraph Build[Build]
        D[Data contract]
        P[Prompt or model change]
        E[Evaluation set]
        G[Release gate]
        D --> E
        P --> E
        E --> G
    end

    subgraph Run[Run]
        I[Input]
        X[Context and retrieval]
        M[Model]
        U[Tools and policies]
        O[Output]
        I --> X --> M --> U --> O
    end

    subgraph Learn[Learn]
        T[Traces]
        F[Feedback]
        C[Corrections]
        T --> F --> C
    end

    G --> Run
    O --> T
    C --> D
    C --> P
    C --> E
```

## How to read it

* The build loop defines what should happen.
* The run loop executes the behavior.
* The learning loop reveals what actually happened.
* A mature system connects the three without allowing uncontrolled changes to reach users.

## Question

Where would you place a human reviewer in this map? The answer depends on risk, reversibility, and the cost of waiting.
