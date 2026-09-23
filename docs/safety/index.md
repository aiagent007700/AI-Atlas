---
id: index
title: "Trust, security, and governance"
sidebar_position: 1
---

# Trust, security, and governance

AI systems do not become dependable merely because a model is accurate on a benchmark. They become dependable when the surrounding system has explicit assumptions, controlled authority, observable behavior, recovery paths, and accountable owners.

This module asks a practical question:

> What would have to be true before you let an AI system make this decision without you?

## The layer map

Think about trust as a stack:

1. **Model behavior** — capability, uncertainty, bias, and failure modes.
2. **Data behavior** — provenance, permissions, retention, and contamination.
3. **Application behavior** — prompts, retrieval, tools, workflows, and interfaces.
4. **Operational behavior** — monitoring, rollback, incident response, and change control.
5. **Organizational behavior** — ownership, policy, auditability, and redress.

A control at one layer cannot compensate automatically for a missing control at another. A prompt filter cannot repair an over-privileged tool. A model card cannot prove that production data is being handled lawfully.

## What this module covers

- Threat modeling for AI applications
- Prompt injection and indirect instruction attacks
- Privacy, data governance, and provenance
- Assurance cases and evidence-based release decisions
- Standards, regulatory frameworks, and industry guidance

## Evidence anchors

Use the following public references as starting points, not as substitutes for system-specific analysis:

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — a risk-management vocabulary and lifecycle perspective.
- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — an application-security threat catalogue.
- [MITRE ATLAS](https://atlas.mitre.org/) — an adversary-behavior knowledge base for machine-learning systems.
- [ISO and IEC AI management-system standards](https://www.iso.org/committee/6794475.html) — a standards context for organizational controls.
- [European Commission AI policy and regulation](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) — a public regulatory reference point.

## A thought experiment

Suppose an agent can read every internal document and call a production API. Which matters more: improving its answer quality by five percent, or reducing the damage from one unauthorized action by ninety percent?

The answer depends on the use case, but the question reveals a general principle: capability and authority should be designed together.
