---
id: sprint-04
title: "Sprint 04: the AI systems layer"
sidebar_position: 4
description: New modules connecting model mechanics to production systems, evaluation, safety, and operations.
---

# Sprint 04: the AI systems layer

This sprint connects model capability to production reality.

## New learning path

* [Transformers: the engine behind modern AI](../models/transformers)
* [The model lifecycle](../systems/model-lifecycle)
* [Inference and serving](../systems/inference-and-serving)
* [Evaluation design](../evaluation/evaluation-design)
* [Trustworthy AI](../safety/trustworthy-ai)
* [Visual AI system map](../visual/ai-system-map)

## Editorial question

> When an AI system fails, which layer should receive the blame: the model, the data, the workflow, the permissions, or the organization that connected them?

## Suggested exercise

Choose one AI feature and draw its complete path from user request to operational outcome. Mark every place where the system can:

* lose context
* introduce unsupported information
* exceed a permission boundary
* become too slow or expensive
* fail without an observable signal

That map is often more valuable than another model comparison table.
