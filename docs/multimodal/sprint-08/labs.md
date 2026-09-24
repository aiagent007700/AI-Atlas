---
id: labs
title: "Labs — reason about multimodal systems by building small experiments"
sidebar_label: "Labs"
description: "Practical exercises for testing multimodal representations, generation, and grounding."
---

# Labs — reason about multimodal systems by building small experiments

These labs are deliberately small. The goal is not to train a frontier model. It is to expose the assumptions hidden inside a multimodal pipeline.

## Lab 1 — Missing-modality evaluation

Create a question-answering task over a small set of images and captions. Run four conditions:

1. Image and text available.
2. Image unavailable.
3. Caption unavailable.
4. Image degraded or cropped.

Record whether the system answers, abstains, or hallucinates. Add a required missing-modality notice to the output contract. Compare user trust before and after the notice.

### Questions

- Does the system know which modality supported its answer?
- Does a longer answer make an unsupported answer appear more credible?
- Which failures are recoverable through clarification?

## Lab 2 — Diffusion control matrix

Use an existing diffusion pipeline or a hosted demonstration. Hold the prompt constant while varying seed, guidance, resolution, and structural control. Record:

- Semantic adherence.
- Composition stability.
- Identity consistency.
- Text rendering.
- Latency and memory use.

Do not evaluate from one sample. Use several seeds and define pass conditions before inspecting results.

## Lab 3 — Time-aligned audio evidence

Take a short recording with two speakers and one non-speech event. Produce a transcript with timestamps and speaker labels. Ask a model to summarize the event, but require every factual statement to cite a time interval.

Create adversarial cases:

- Overlapping speakers.
- A number spoken unclearly.
- Background audio that resembles speech.
- A correction made after the first statement.

## Lab 4 — Video sampling failure

Choose a video with a brief event. Compare uniform sampling, keyframe sampling, and a two-pass detector. Measure event recall, not only summary quality. Document what each sampler misses.

## Lab 5 — Embodied skill contract

Write a `SKILL.md`-style specification for a simulated physical task. Include preconditions, required observations, actions, termination, recovery, safety boundaries, and evidence of success. Ask another person to identify ambiguous or unsafe statements.

## Lab report template

For every lab, record:

- Hypothesis.
- Data and split.
- Model and version.
- Prompt or configuration.
- Metrics and slices.
- Surprising failure.
- Mitigation.
- What the experiment does not establish.

The final line matters. A small experiment can reveal a failure mode without proving that a production system will fail at the same rate.
