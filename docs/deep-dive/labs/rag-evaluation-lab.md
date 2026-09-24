---
id: rag-evaluation-lab
title: "Lab: build a RAG evidence ledger"
description: A model-agnostic exercise for separating retrieval quality from answer quality.
sidebar_label: "Lab: RAG evidence ledger"
---
# Lab: build a RAG evidence ledger

This lab is designed to be completed before selecting a framework or model. It turns a vague question—“Is our RAG system good?”—into a small evidence and evaluation dataset.

## Outcome

You will create a ledger that records whether a question is answerable, what evidence is required, what source should be authoritative, and how an answer should be judged.

## Step 1: choose a bounded corpus

Select a small public corpus such as a documentation set, a standards section, or a group of technical articles. Record the canonical URLs and the retrieval date. Do not mix sources with different authority levels without labeling them.

## Step 2: write the question set

Create at least 20 questions across these classes:

* Direct lookup
* Multi-hop synthesis
* Terminology ambiguity
* Time-sensitive fact
* Conflicting sources
* Unanswerable question
* Adversarial instruction embedded in source text

## Step 3: define the evidence ledger

For each question, record:

* Expected answer or answer properties
* Required source identifiers
* Minimum evidence needed
* Acceptable uncertainty or abstention
* Retrieval result and rank
* Generated claims
* Claim-to-evidence mapping
* Human judgment and reason

## Step 4: score separately

Score retrieval and generation separately. A response can be well written but unsupported. A retriever can find the right paragraph while the generator misstates it. Keep these failure classes distinct.

## Step 5: inspect the failures

For every failure, classify the cause as source quality, ingestion, chunking, query formulation, ranking, context assembly, generation, policy, or evaluation ambiguity. Choose one corrective action and rerun only the affected slice.

## Deliverable

Produce a short report with:

* The corpus contract
* The question taxonomy
* Retrieval results
* Claim-level evidence examples
* Five representative failures
* One proposed change and its expected effect

## Further reading

* [RAG foundational paper](https://arxiv.org/abs/2005.11401)
* [Ragas documentation](https://docs.ragas.io/)
* [TREC](https://trec.nist.gov/)
* [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
