---
title: "Supervised and self-supervised learning in practice"
sidebar_label: "Supervised and self-supervised learning"
sidebar_position: 3
description: "From labels and objectives to representation learning and data-centric iteration."
---

# Supervised and self-supervised learning in practice

A training dataset is not a neutral mirror of reality. It is a designed measurement system. The choice of examples, labels, exclusions, sampling rate, and time window determines what the model can learn and what it will systematically miss.

## The data contract

Before training, write down a data contract:

* **Unit of observation:** what does one row, sequence, image, or event represent?
* **Prediction time:** what information is available when the decision is made?
* **Target definition:** what exactly is being predicted, and over what horizon?
* **Exclusions:** which cases are missing, filtered, or impossible to label?
* **Splitting rule:** how will train, validation, and test data respect time, users, sites, or devices?
* **Action link:** what decision will consume the prediction?

The prediction-time question is especially important. A feature that is available after an incident is resolved can make a retrospective model look excellent while being unusable in real time. This is leakage, and it often survives random train-test splits.

## Labels are measurements

Labels can be noisy in several ways:

* **Random noise:** annotators disagree or sensors fluctuate.
* **Systematic noise:** one group or region is labeled differently from another.
* **Selection bias:** only difficult or high-value cases receive labels.
* **Temporal drift:** the meaning of a label changes over time.
* **Policy feedback:** the model changes which cases are observed or escalated.

A robust data program measures label quality instead of assuming it. Track disagreement, missingness, correction rates, and the time between an event and its final label.

## Self-supervised representations

Self-supervised learning is often used before supervised adaptation. A representation model learns from a large corpus, then a smaller task-specific model or head uses those representations. The benefit is not magic; it is a change in where the data and compute are spent.

Representation quality should be tested with more than one downstream task. A representation that is excellent for retrieval may be poor for calibration, anomaly detection, or causal analysis. Probe tasks can reveal what information is present, but they do not establish that the representation is appropriate for a high-stakes decision.

## Data-centric iteration

When a model fails, changing the architecture is only one possible response. Other interventions may be more valuable:

* Add examples for rare but consequential cases.
* Correct inconsistent labels.
* Revisit the target definition.
* Change the split to reflect deployment.
* Add drift slices and subgroup analysis.
* Remove features that encode post-outcome information.
* Improve the feedback process instead of only increasing model capacity.

## Worked example: incident prediction

Imagine predicting whether a service event will require escalation within the next hour. A naive dataset may include the final severity code and the number of operator comments, both of which are created after escalation begins. A valid design would freeze features at the prediction timestamp, define the horizon, and evaluate separately by service, region, event type, and traffic regime.

The model output should also be calibrated. An operator deciding whether to wake an on-call engineer needs a probability with a meaningful interpretation, not only a ranking score.

## Exercise

Write a one-page data contract for a model you care about. Include the timestamp at which features are frozen, the target horizon, the split strategy, three likely leakage paths, and four slices on which performance must be reported.
