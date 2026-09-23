---
id: transformers
slug: /models/transformers
title: "Transformers: the engine behind modern AI"
sidebar_position: 1
description: Why attention changed the way models represent context, and what the mechanism does not solve.
---

# Transformers: the engine behind modern AI

A transformer is often described as an architecture. A more useful description is a **programmable way to allocate attention across a sequence**.

That distinction matters. A transformer can learn powerful representations, but it does not automatically know what is true, what matters, or what action should be taken next.

## The opening puzzle

> If attention lets a model connect every token to every other token, why does the model still lose track of the user’s goal?

The answer is that **context access is not the same as understanding**. The architecture supplies a mechanism; training, data, objectives, memory design, and evaluation determine what that mechanism becomes.

## The core mechanism

```mermaid
flowchart LR
    A[Text or multimodal input] --> B[Tokenization]
    B --> C[Embeddings + position information]
    C --> D[Self-attention]
    D --> E[Feed-forward transformation]
    E --> F[Repeated transformer blocks]
    F --> G[Output probabilities or representations]
    G --> H[Generation, classification, retrieval, or action]
```

At a high level, each token produces three learned projections:

* a **query**: what this token is looking for
* a **key**: what this token can be matched on
* a **value**: what information this token contributes

The attention calculation compares queries with keys, turns the scores into weights, and mixes the values. Multiple attention heads allow different relationships to be represented at the same time.

$$
\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

The equation is compact; the engineering consequences are not. Memory use, sequence length, numerical precision, hardware topology, and batching strategy all affect whether the model is practical.

## Three different jobs

A transformer family can support very different jobs depending on its training objective:

| Job | Typical behavior | Common use |
|---|---|---|
| Encoder-style representation | Reads a sequence and produces contextual representations | Classification, search, embeddings |
| Decoder-style generation | Predicts the next token repeatedly | Text generation, code, agents |
| Encoder-decoder transformation | Reads one sequence and produces another | Translation, summarization, structured transformation |

The architecture is not the product. The product is the combination of architecture, data, objective, post-training, runtime, interface, and controls.

## What scaling changes—and what it does not

More parameters, data, and compute can improve capability, but scaling does not eliminate:

* ambiguous requirements
* poor or contaminated data
* weak retrieval
* unsafe tools
* misaligned incentives
* evaluation blind spots
* latency and cost constraints

A large model may be better at producing a plausible answer while remaining poor at knowing when it should abstain.

## Industry and research signals

* The original transformer paper introduced attention-based sequence transformation without relying on recurrence: [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
* The scaling-law literature made compute, data, and parameter allocation explicit design variables: [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361).
* Chinchilla-style results highlighted that model size and training-token budget must be considered together: [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556).

These are not recipes for “bigger is always better.” They are reminders that capability is produced by a system of coupled choices.

## Engineering reality

When evaluating a transformer-based system, ask:

* What is the unit of context: tokens, images, audio frames, events, or graph nodes?
* Which information must be preserved exactly?
* What is the acceptable latency and cost per request?
* Does the model need to generate, classify, retrieve, or control?
* What happens when the input is outside the training distribution?
* Can the system show evidence or an uncertainty signal?

## Think deeper

A model can attend to a fact without using it correctly. What additional mechanism—retrieval, verification, planning, tool use, or human review—should be responsible for closing that gap?
