---
id: fine-tuning-and-adaptation
title: Model adaptation
sidebar_label: Model adaptation
description: Choosing between prompting retrieval fine-tuning and training.
---

# Model adaptation

Adaptation is a ladder, not a single technique. Start with the least expensive change that can reliably solve the task.

```mermaid
flowchart LR
    A[Clear task contract] --> B[Prompt and context]
    B --> C[Retrieval or tools]
    C --> D[Structured outputs]
    D --> E[Parameter efficient tuning]
    E --> F[Full fine tuning]
    F --> G[Pretraining or new model]
```

## A practical decision sequence

* Use prompting when the model already knows the task and the main problem is instruction clarity.
* Use retrieval when the problem is missing, private, or changing knowledge.
* Use tools when the system must calculate, query, transact, or observe the world.
* Use structured outputs when downstream software needs predictable fields.
* Use parameter efficient tuning when a repeatable style or behavior must be learned from examples.
* Consider full fine-tuning only when the expected gain justifies the data, evaluation, and serving burden.

The [Google fine-tuning guidance](https://cloud.google.com/use-cases/fine-tuning-ai-models) highlights the importance of representative data, validation, and regular evaluation. The important lesson is not that fine-tuning is always difficult. It is that fine-tuning turns a model change into a data and release-management problem.

## What tuning can and cannot do

Fine-tuning can shape behavior, format, style, and task execution patterns. It is not a reliable substitute for a current knowledge source. If facts change frequently, retrieval or a tool may be the more direct solution.

## Industry signal

The [NVIDIA LLMOps discussion](https://developer.nvidia.com/blog/fine-tuning-llmops-for-rapid-model-evaluation-and-ongoing-optimization/) connects adaptation with experiment tracking, evaluation, deployment, and ongoing optimization. That is a useful corrective to the idea that fine-tuning ends when the training job ends.

## Failure modes

* Training on examples that contain hidden policy or quality errors.
* Measuring only the target task and missing regressions in general capability.
* Treating a benchmark gain as proof of production value.
* Publishing a tuned model without a rollback path.
* Forgetting that a new model may change retrieval, tool selection, or safety behavior.

## Try this

For one task, write down the problem that each rung of the adaptation ladder solves. If two rungs solve the same problem, compare them using quality, latency, cost, data effort, and reversibility.
