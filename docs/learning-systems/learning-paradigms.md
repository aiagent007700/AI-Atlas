---
title: "Learning paradigms: choosing the feedback loop"
sidebar_label: "Learning paradigms"
sidebar_position: 2
description: "A practical comparison of supervised, self-supervised, unsupervised, and reinforcement learning."
---

# Learning paradigms: choosing the feedback loop

The phrase “machine learning” hides a design choice: what signal tells the system that one behavior is better than another? The answer determines the data pipeline, the objective, the evaluation method, and the kinds of failure that are likely.

## Supervised learning

Supervised learning treats examples as pairs of inputs and target labels. A classifier learns a mapping from an observation to a category; a regressor learns a mapping to a numeric value.

The attractive feature is an explicit target. The difficult part is that the target may be expensive, subjective, delayed, or only loosely related to the decision we actually care about. A highly accurate label predictor can still be a poor decision aid if the labels encode historical bias or if the deployment distribution changes.

Typical questions:

* Who or what produced the label?
* What happens when the input is outside the training distribution?
* Is the cost of a false positive the same as the cost of a false negative?
* Does the label measure the outcome, or only a convenient proxy?

## Self-supervised learning

Self-supervised learning creates a training signal from the data itself. Masking tokens, predicting the next item, contrasting related views, or reconstructing corrupted inputs are ways to force a model to learn useful structure without a human label for every example.

The absence of manual labels does not mean the absence of design choices. The pretext task determines what information is rewarded. Next-token prediction encourages broad sequence modeling; contrastive objectives can encourage invariances; reconstruction can preserve details that a downstream task may not need.

## Unsupervised and exploratory learning

Clustering, density estimation, dimensionality reduction, and anomaly detection look for structure without a predefined target. These methods are valuable when the categories are unknown, but interpretation becomes part of the work. A cluster is not automatically a real-world segment, and an anomaly may be a sensor problem rather than a rare event.

## Reinforcement learning

Reinforcement learning uses interaction: an agent observes a state, selects an action, receives a reward or cost, and transitions to a new state. The signal is usually delayed, so the system must reason about consequences rather than only immediate correctness.

This makes RL attractive for scheduling, control, resource allocation, and other sequential problems. It also makes RL dangerous when exploration is unconstrained or when the reward is a poor proxy for the desired outcome.

## A comparison

| Paradigm | Feedback source | Strong fit | Typical risk |
|---|---|---|---|
| Supervised | Human or system labels | Prediction with stable targets | Label bias and distribution shift |
| Self-supervised | Structure in raw data | Representation learning | Pretext task mismatch |
| Unsupervised | Statistical regularities | Discovery and anomaly analysis | Over-interpreting structure |
| Reinforcement | Outcomes from actions | Sequential decisions | Reward hacking and unsafe exploration |

## Choosing a paradigm

Start from the decision and feedback loop, not from the fashionable algorithm. If you have reliable labels and a stable prediction target, supervised learning may be sufficient. If labels are scarce but raw data is abundant, self-supervision may reduce the labeling burden. If actions change the future and feedback is delayed, RL may be appropriate—but only with a safe environment, constrained exploration, and an evaluation plan that covers more than reward.

## Exercise

Take one operational problem and describe it four ways: as a supervised prediction, a self-supervised representation task, an anomaly-detection task, and a reinforcement-learning problem. Which information becomes visible in each formulation, and which assumptions become hidden?
