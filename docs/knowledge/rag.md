---
title: Retrieval-augmented generation
sidebar_position: 1
description: How retrieval connects generative models to external knowledge.
---

# Retrieval-augmented generation

## The opening puzzle

If a language model can retrieve evidence before answering, why can it still produce a confident error?

RAG combines retrieval with generation. The system searches an external knowledge source, places selected context into the model input, and asks the model to produce an answer grounded in that context.

## The basic architecture

```mermaid
flowchart LR
    Q[Question] --> R[Retriever]
    R --> C[Relevant context]
    Q --> P[Prompt construction]
    C --> P
    P --> L[Language model]
    L --> A[Answer]
    A --> V[Verification]
```

## Main design choices

* Chunking: how documents are split
* Embeddings: how semantic similarity is represented
* Indexing: where and how content is stored
* Retrieval: vector, lexical, hybrid, graph, or filtered search
* Reranking: how candidate passages are reordered
* Context construction: how evidence is presented to the model
* Verification: how unsupported claims are detected

## Important variants

* Hybrid RAG combines lexical and vector retrieval.
* Graph RAG uses relationships between entities and concepts.
* Multimodal RAG retrieves text, images, tables, audio, or video.
* Corrective RAG evaluates retrieval quality and retries when needed.
* Agentic RAG lets an agent plan multiple searches or use tools.

## Failure modes

* The correct document is not retrieved.
* The wrong passage is ranked first.
* The context is too long or contradictory.
* The model ignores evidence.
* The evidence is outdated.
* The answer is technically supported but fails the user's intent.

## Thought experiment

Does adding more retrieved context necessarily improve reliability? Or can additional context increase ambiguity, distract the model, and make verification harder?

## Practical exercise

Take one question and compare answers produced with:

1. No retrieval
2. Vector retrieval
3. Hybrid retrieval
4. Retrieval plus explicit evidence citations

Record not only correctness, but also confidence, traceability, latency, and cost.
