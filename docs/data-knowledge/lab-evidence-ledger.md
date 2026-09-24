---
title: "Lab: build an evidence ledger"
sidebar_label: "Lab: build an evidence ledger"
sidebar_position: 10
---

# Lab: build an evidence ledger

This lab turns a retrieval or RAG system into an inspectable experiment. You can complete it with a small public corpus and a local or hosted model.

## Objective

Measure where an answer pipeline succeeds and fails by tracing each output back through source coverage, retrieval, context assembly, generation, and policy.

## Materials

* A corpus of 20 to 100 public documents
* Ten ordinary questions
* Five ambiguous questions
* Five adversarial or insufficient-evidence questions
* A retrieval configuration to evaluate
* A spreadsheet or JSON file for the ledger

## Ledger fields

```text
case_id
question
expected_behavior
source_versions
retrieved_ids
retrieval_rankings
context_summary
model_configuration
claims
supporting_evidence
unsupported_claims
citation_correctness
policy_result
latency_ms
estimated_cost
failure_category
reviewer_notes
```

## Procedure

1. Freeze the corpus and record source versions.
2. Write expected behavior before running the system.
3. Run each question without editing the output.
4. Record retrieved items and the exact context supplied.
5. Split the answer into claims.
6. Link each claim to supporting evidence or mark it unsupported.
7. Assign one primary failure category.
8. Repeat with one controlled retrieval change.
9. Compare failure distributions, not only average scores.
10. Write a short release recommendation.

## Suggested analysis

Create a matrix with failure categories as rows and question types as columns. Look for patterns. If ambiguous questions fail because query rewriting removes constraints, a better generator may not help. If the corpus lacks authoritative sources, retrieval tuning cannot solve the problem.

## Exit criteria

You are finished when another person can reproduce the experiment, inspect the evidence behind each judgment, and understand why the recommended change should improve the intended user outcome.

## Extension

Add a freshness event: update or revoke one source, rerun the affected cases, and verify that indexes, caches, citations, and logs reflect the change. Then add an access-control case and confirm that restricted evidence is excluded before generation.

## Reference tools

* [BEIR](https://github.com/beir-cellar/beir) for retrieval evaluation datasets.
* [RAGAS](https://github.com/explodinggradients/ragas) for RAG evaluation components.
* [OpenLineage](https://openlineage.io/) for lineage concepts.
