---
id: standards-map
title: "Standards and ecosystem map"
sidebar_label: "Standards map"
description: "How major telecom, networking and AI standards communities contribute to autonomous-network design."
---

# Standards and ecosystem map

## No single standard defines an autonomous network

Autonomous-network architecture crosses several boundaries. One body may define system behavior, another management interfaces, another operational maturity, and another deployment or interoperability mechanisms. The tutorial should therefore treat standards as a map of responsibilities, not as a single stack with one owner.

| Community | Primary lens | Questions it helps answer |
|---|---|---|
| 3GPP | mobile system architecture and procedures | What network functions exist and how do they interact? |
| ETSI ZSM | zero-touch management | How can management domains coordinate closed loops? |
| ETSI ENI | experiential and AI-driven networking | How can goals, context and intelligence influence network behavior? |
| TM Forum | business and operational transformation | How is autonomy measured and connected to service outcomes? |
| O-RAN Alliance | open and intelligent RAN | How can RAN components and intelligent applications interoperate? |
| ITU-T | global architectural and policy guidance | How should ML functions and interfaces be described in future networks? |
| IETF | Internet protocols and data models | How can systems be configured, exposed and automated using interoperable protocols? |
| CNCF and Kubernetes | cloud-native platform operation | How are workloads deployed, reconciled, observed and recovered? |

## How to read a specification

Do not begin with the acronym list. Start with the scope and status. Identify whether the document is normative, informative, a requirements document, an architecture, a data model or an implementation guide. Then ask which behavior is mandatory, which is optional and which is merely recommended.

For AI-enabled operations, record:

* decision or interface being standardized
* data and semantic assumptions
* lifecycle and versioning rules
* security and authorization model
* observability and conformance expectations
* relationship to adjacent standards

## Why this matters for tutorial readers

A system can be technically impressive and still fail interoperability because it ignores naming, data models, lifecycle semantics or authorization boundaries. Standards literacy is therefore an engineering skill, not a compliance afterthought.

## Reference shelf

* [3GPP specifications](https://www.3gpp.org/DynaReport/): the primary portal for 3GPP technical specifications and reports.
* [ETSI ZSM](https://www.etsi.org/technical-groups/zsm/): zero-touch network and service management.
* [ETSI ENI](https://www.etsi.org/technical-groups/eni/): experiential networked intelligence.
* [TM Forum Autonomous Networks](https://www.tmforum.org/missions/autonomous-networks): autonomous-network maturity and business framing.
* [O-RAN Alliance](https://www.o-ran.org/): open and intelligent RAN ecosystem.
* [O-RAN Native AI architecture](https://www.o-ran.org/research-reports/o-ran-native-ai-architecture-description): AI architecture material for RAN.
* [ITU-T ML5G focus group](https://www.itu.int/en/ITU-T/focusgroups/ml5g/pages/default.aspx): ML architecture for future networks.
* [IETF network management research](https://datatracker.ietf.org/meeting/106/materials/slides-106-nmrg-sessb-22d-itu-updates-for-ml-in-5g-vishnu): public material connecting ML-in-networking architecture with standards work.

## Thought experiment

Two automation platforms both claim to support intent-based networking. One defines intent as a business objective with assurance evidence; the other defines it as a configuration template. Can they interoperate without a shared semantic model? What would a conformance test need to prove?
