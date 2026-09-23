---
id: privacy-and-data
title: "Privacy, provenance, and data governance"
sidebar_position: 4
---

# Privacy, provenance, and data governance

AI systems make data governance operational. A document that was harmless in storage may become sensitive when it is embedded, retrieved, summarized, logged, or used to trigger an action.

## Four questions for every data path

1. **Permission** — is the system allowed to use this data for this purpose?
2. **Provenance** — where did the data come from and what transformations occurred?
3. **Purpose** — what decision or capability does the data support?
4. **Persistence** — where will the data remain after the request ends?

These questions apply to prompts, embeddings, caches, traces, evaluation sets, fine-tuning corpora, and model outputs.

## Embeddings are not automatically anonymous

An embedding is a transformed representation, not a magic privacy boundary. It may still encode sensitive information, be linked to an identity, or expose content through retrieval behavior. The correct control depends on the data, threat model, access pattern, and retention policy.

## Minimum metadata for a governed source

Track, where appropriate:

- Source owner and lawful or contractual basis
- Collection date and version
- Sensitivity classification
- Allowed purposes and audiences
- Retention and deletion rule
- Transformation history
- Access policy
- Evaluation and incident history

## Practical controls

- Enforce authorization before retrieval, not after generation.
- Filter or partition indexes by tenant and sensitivity.
- Redact or tokenize secrets before they enter prompts or logs.
- Keep retention periods explicit for traces and feedback data.
- Make deletion requests propagate to derived stores where required.
- Test whether outputs can reveal memorized or retrieved sensitive content.

## Industry and standards perspective

Risk frameworks and management-system standards help organizations assign ownership and document controls. They do not turn every data use into an approved use. Governance is a decision process, not a label attached after deployment.

## Think deeper

If a user can access a document through the search interface, does that automatically mean an agent may quote it into a different workflow? Access and permitted use are related, but they are not always identical.
