---
title: "Learning systems reference shelf"
sidebar_label: "Reference shelf"
sidebar_position: 9
description: "Canonical books, courses, papers, documentation, and maintained implementations for learning systems."
---

# Learning systems reference shelf

These references are starting points, not endorsements of every claim made by their authors. Prefer primary sources, inspect publication dates and versions, and verify that an implementation still matches the concept being studied.

## Foundations and deep learning

* [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) — practical orientation to supervised learning, data, neural networks, and production considerations. **Type:** official course. **Stability:** maintained.
* [Deep Learning](https://www.deeplearningbook.org/) — Goodfellow, Bengio, and Courville. A broad technical reference for representation learning and optimization. **Type:** textbook. **Stability:** canonical.
* [Dive into Deep Learning](https://d2l.ai/) — interactive, code-oriented treatment of deep-learning concepts. **Type:** open textbook. **Stability:** maintained.
* [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) — classical learning algorithms, preprocessing, evaluation, and practical pitfalls. **Type:** official documentation. **Stability:** maintained.
* [PyTorch Tutorials](https://pytorch.org/tutorials/) — implementation patterns for training, profiling, and deployment. **Type:** official documentation. **Stability:** maintained.

## Reinforcement learning

* [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html) — Sutton and Barto. The canonical conceptual reference for RL. **Type:** textbook. **Stability:** canonical.
* [Spinning Up in Deep RL](https://spinningup.openai.com/en/latest/) — algorithms, terminology, and implementation-oriented explanations. **Type:** educational documentation. **Stability:** maintained reference; check project status before relying on tooling.
* [CleanRL](https://github.com/vwxyzjn/cleanrl) — single-file implementations designed for readability and reproducibility. **Type:** GitHub implementation. **Stability:** maintained; verify commit and environment before use.
* [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) — maintained environment API for reinforcement-learning experimentation. **Type:** GitHub project. **Stability:** maintained; review release notes.

## Continual and federated learning

* [Avalanche](https://avalanche.continualai.org/) — library and examples for continual-learning research. **Type:** official documentation. **Stability:** maintained; verify compatibility.
* [Flower](https://flower.ai/docs/) — framework and documentation for federated learning experiments and deployments. **Type:** official documentation. **Stability:** maintained.
* [TensorFlow Federated](https://www.tensorflow.org/federated) — framework for machine-learning and federated-computation research. **Type:** official documentation. **Stability:** maintained; check supported versions.

## Research and evaluation

* [Papers with Code](https://paperswithcode.com/) — useful index for papers, tasks, datasets, and implementations. **Type:** research index. **Stability:** verify links against the original paper and repository.
* [MLflow Documentation](https://mlflow.org/docs/latest/ml/tracking/) — experiment tracking and lifecycle concepts. **Type:** official documentation. **Stability:** maintained.

## How to use references

Start with one canonical explanation, one implementation, and one evaluation guide. Do not treat a repository star count as evidence of correctness. Record the version or commit used in a lab, preserve the environment, and note any divergence between the reference implementation and your system.

## Source quality policy

* Canonical standards and textbooks define concepts, but may not describe current production practice.
* Official documentation is useful for interfaces and supported behavior, but may present an optimistic path.
* GitHub repositories are implementation evidence, not proof that a technique works in every environment.
* Research papers establish reported results under stated conditions; reproduce or qualify claims before generalizing them.
