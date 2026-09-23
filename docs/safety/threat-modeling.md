---
id: threat-modeling
title: "Threat modeling AI systems"
sidebar_position: 2
---

# Threat modeling AI systems

Traditional application threat models ask what an attacker can access and what they can change. AI systems add another question:

> What can the system be persuaded to believe, reveal, or do?

## Start with assets and authority

List the assets before listing attacks:

- Sensitive data and secrets
- User identity and permissions
- Model weights, prompts, and evaluation data
- Retrieved context and tool outputs
- Business decisions and external side effects
- Availability, latency, and cost budgets
- Evidence needed for audit or dispute resolution

Then list the authority available at each step. Reading a document, recommending an action, executing a transaction, and changing a policy are different risk levels.

## A practical threat-model worksheet

For each capability, record:

| Field | Question |
| --- | --- |
| Actor | Who can invoke or influence this path? |
| Asset | What could be exposed, changed, or degraded? |
| Trust boundary | Where does untrusted data enter? |
| Action | What can the system actually do? |
| Control | What prevents, detects, or limits misuse? |
| Evidence | How will we know the control worked? |
| Recovery | How do we stop, reverse, or learn from failure? |

## AI-specific attack surfaces

- **Instruction confusion** — system, developer, user, retrieved, and tool text compete for influence.
- **Data poisoning** — training or retrieval data changes the behavior of the system.
- **Sensitive disclosure** — prompts, context, logs, or outputs reveal information beyond the caller's authority.
- **Tool misuse** — a valid tool is used with an unsafe argument or at an unsafe time.
- **Resource abuse** — recursive calls, oversized context, or repeated retries create cost or availability failures.
- **Evaluation gaming** — the system optimizes the measured score while avoiding the intended outcome.

## Design rule

Treat retrieved text and tool output as data, not as authority. Authority should come from a separately controlled policy layer.

## Industry input

Security catalogues such as OWASP Top 10 for LLM Applications and MITRE ATLAS are useful because they turn vague concern into named attack patterns. Their limitation is equally important: a catalogue helps you ask better questions, but it does not tell you the actual exposure of your deployment.

## Think deeper

If an agent has no permission to delete data, but can call a tool that triggers a workflow which deletes data, where is the real permission boundary?
