---
id: governance-and-standards
title: "Governance, standards, and regulation"
sidebar_position: 5
---

# Governance, standards, and regulation

Governance is often presented as paperwork around a technical system. A better view is that governance defines the conditions under which a technical system may operate.

## Three kinds of instruments

- **Standards** describe agreed practices, terminology, or management controls.
- **Regulation** creates legal obligations that depend on jurisdiction and use case.
- **Guidance** helps practitioners interpret risk and choose controls but may not be legally binding.

A project can satisfy a checklist and still fail its users. The relevant question is whether the evidence supports the claims being made about the system.

## A useful governance record

For each material AI capability, record:

- Intended purpose and excluded uses
- Responsible owner and escalation path
- User population and affected parties
- Data sources and permissions
- Known limitations and failure modes
- Evaluation results and test coverage
- Human oversight and appeal path
- Monitoring, incident response, and rollback
- Change history and review date

## Evidence over declarations

Prefer evidence that can be inspected:

- Test cases and results
- Trace samples with sensitive data removed
- Access-control tests
- Red-team findings and remediation
- Drift and quality monitoring
- User feedback and incident records
- Release approvals and exceptions

## Public reference points

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [ISO and IEC AI standards committee](https://www.iso.org/committee/6794475.html)
- [OWASP GenAI Security Project](https://owasp.org/www-project-generative-ai-security-project/)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [European Commission AI policy and regulation](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

## Debate

A universal AI checklist is attractive because it is portable. But risk is contextual. A control that is proportionate for a writing assistant may be inadequate for a system that changes a customer's eligibility, controls infrastructure, or executes a financial action.

## Thought experiment

What is the smallest piece of evidence that would change your decision to release the system? If the answer is “nothing,” the governance process is ceremonial.
