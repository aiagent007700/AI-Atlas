---
id: sprint-08
title: "Sprint 8 — Multimodal and generative AI"
sidebar_label: "Sprint 8 overview"
description: "A systems tutorial on vision, speech, diffusion, video, grounding, world models, and embodied AI."
---

# Sprint 8 — Multimodal and generative AI

Language models are only one part of the AI landscape. Real environments arrive as images, audio, video, sensor streams, documents, and actions. A useful AI system must decide how to represent those signals, how to align them, and how to turn uncertain perception into safe decisions.

This sprint studies the layer beyond text-only systems. It is not a catalogue of model names. It is a way to reason about the design choices that recur across computer vision, speech, image generation, video understanding, world models, and robotics.

## The central question

> Does adding more modalities make a system more intelligent, or does it create more ways for errors to hide?

The answer depends on the whole pipeline: sensors, representations, alignment data, model architecture, grounding, evaluation, and the action policy around the model.

## What you will learn

- How multimodal systems represent and align different signals.
- Why vision, speech, and video need different evaluation strategies.
- How diffusion models turn noise into structured samples.
- Why generation quality is not the same as factuality or controllability.
- How grounding links a model's output to observations, tools, or the physical world.
- What world models and embodied AI add beyond perception and generation.
- How to choose between a unified model, a routed system, and a pipeline of specialists.

## Learning route

1. Read [Multimodal foundations](./multimodal-foundations) to establish the common vocabulary.
2. Compare [computer vision](./computer-vision) and [speech and audio](./speech-and-audio) as two different sensing problems.
3. Study [diffusion and generation](./diffusion-and-generation) and [video and temporal models](./video-and-temporal-models).
4. Use [grounding and evaluation](./grounding-and-evaluation) to examine whether a system is actually reliable.
5. Finish with [world models and embodied AI](./world-models-and-embodied-ai) and [production patterns](./production-patterns).
6. Complete the [labs](./labs), then use the [reference shelf](./references) to go deeper.

## A system view

```mermaid
flowchart LR
    A[World and sensors] --> B[Perception]
    B --> C[Representations]
    C --> D[Cross-modal alignment]
    D --> E[Reasoning and generation]
    E --> F[Grounding and verification]
    F --> G[Human or machine action]
    G --> H[Feedback and new observations]
    H --> B
```

The loop matters. A model can generate a visually convincing image while misunderstanding the scene. A speech model can transcribe fluently while missing an important speaker. An embodied agent can plan coherently while its sensors or actuators are poorly calibrated.

## Thought experiments

- If a model can describe an image but cannot identify which pixels support its answer, is it seeing or merely associating?
- If a generated video looks physically plausible for two seconds and violates conservation of motion on the third, what should a benchmark reward?
- When a robot learns from demonstrations, which part of the skill belongs to the policy and which part belongs to the environment?
- Is a unified multimodal model simpler in production, or does it merely move complexity into data, routing, and evaluation?

## References and evidence

This sprint favors primary papers, official project pages, and maintained implementations. See [References](./references) for a tiered shelf including the Vision Transformer paper, DDPM, Latent Diffusion, Whisper, Diffusers, Segment Anything, World Models, DreamerV3, Habitat, and Open X-Embodiment.
