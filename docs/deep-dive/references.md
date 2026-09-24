---
id: deep-dive-references
title: Reference shelves and source-quality policy
description: How the tutorial selects external links and keeps them useful.
sidebar_label: Reference policy
---
# Reference shelves and source-quality policy

External links are part of the tutorial's teaching surface. They should help a reader move from explanation to primary evidence or a working implementation without turning every page into a link directory.

## Reference tiers

* **Primary:** standards, specifications, original research papers, official project documentation, and official governance material.
* **Implementation:** maintained repositories and official SDKs with documentation, examples, tests, and a visible license.
* **Practice:** engineering guides, textbooks, courses, and technical reports that explain how to apply the ideas.
* **Community:** useful experiments or collections that are clearly labeled as non-canonical.

## Acceptance checklist

Before adding a link, check:

* Is the source discoverable from its publisher or maintainer?
* Does it state its scope and version or publication date?
* Is the claim being supported actually present in the source?
* Is the project maintained enough for the intended use?
* Does the source have a license or reuse statement where code is involved?
* Is there a more primary source that should be linked first?
* Would a learner understand why the link is useful?

## Link metadata

A reference entry should include the title, publisher or maintainer, category, last-checked date, and a one-sentence reason to follow it. For fast-moving repositories, include the documentation landing page rather than an unstable deep link unless a particular version or commit matters.

## What the daily pipeline may do

The automated pipeline may discover candidate sources, detect link changes, identify duplicates, and propose additions. It should not silently promote a community repository to a canonical reference. New references that affect claims, security advice, standards interpretation, or production recommendations should enter review.

## Link health

Run a broken-link check on every build. Also review semantic freshness: a page can still return HTTP 200 while its content has moved, its version is obsolete, or its recommendation no longer matches the tutorial's claim.

## Starter shelf

* [arXiv computer science](https://arxiv.org/list/cs.AI/recent) — current research discovery; verify important claims against published or official versions.
* [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — risk and governance.
* [OWASP GenAI Security Project](https://genai.owasp.org/) — security guidance and threat references.
* [Hugging Face documentation](https://huggingface.co/docs) — model, dataset, and evaluation implementation material.
* [PyTorch documentation](https://pytorch.org/docs/stable/index.html) — model development and inference primitives.
* [Kubernetes documentation](https://kubernetes.io/docs/home/) — deployment and control-plane concepts.
* [ETSI ZSM](https://www.etsi.org/committee/zsm) — network and service management automation.
* [TM Forum Autonomous Networks](https://www.tmforum.org/oda/autonomous-networks/) — telecom autonomy guidance.
* [3GPP specifications](https://www.3gpp.org/DynaReport/TSG-WG--SA5.htm) — management and orchestration standards.
* [O-RAN Alliance specifications](https://www.o-ran.org/specifications) — intelligent RAN architecture.

*Last checked: 2026-09-24.*
