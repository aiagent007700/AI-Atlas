---
id: sprint-07-index
title: "Sprint 7: Agents, skills and protocols"
sidebar_label: "Sprint 7: Agents and skills"
description: "A deeper tutorial on agentic systems, reusable skills, tools, protocols, evaluation and recovery."
---

# Sprint 7: Agents, skills and protocols

## From impressive answers to dependable action

A language model can produce a convincing answer without having a reliable way to observe the world, use a tool, remember a decision, or recover from a failure. An agentic system adds those capabilities, but it also adds a larger failure surface.

The central question for this sprint is:

> When a system can choose actions, how do we make its behavior useful, inspectable and bounded?

This sprint treats agents as engineered systems rather than magical personalities. You will move from definitions to architecture, then to reusable skills, interoperability, multi-agent design, evaluation, security and recovery.

## Learning path

| Chapter | What you will learn | Design question |
| --- | --- | --- |
| Agent or workflow | How to choose deterministic and model-driven control | Where is autonomy actually useful? |
| The agent loop | How perception, planning, action and verification interact | What happens when the loop is wrong? |
| Skills | How to package reusable expertise and constraints | Is a skill an instruction, a tool or a product? |
| Protocols | How tools and agents interoperate | Which boundary should be standardized? |
| Multi-agent systems | When delegation helps and when it creates overhead | Does more agency create more intelligence? |
| Evaluation and observability | How to test outcomes and trajectories | Can we measure a process, not only an answer? |
| Security and recovery | How to bound actions and recover from failure | What must never be left to model judgment? |
| Labs | How to design and critique a small system | Can you prove the system is ready? |

## What this sprint is not

It is not a vendor comparison, a promise of general intelligence, or a recommendation to make every workflow autonomous. The examples are intentionally generic and use public references. Frameworks and protocols change quickly, so the reference shelf records what each source is useful for and what it does not prove.

## Recommended sequence

1. Read **Agent or workflow** and classify a real workflow.
2. Trace the **agent loop** on paper before selecting a framework.
3. Design a **skill contract** with permissions and acceptance tests.
4. Compare **MCP and A2A** as different interoperability boundaries.
5. Study **multi-agent patterns** only after understanding the single-agent baseline.
6. Build the evaluation and observability plan before adding more autonomy.
7. Use the labs to produce a design review, not merely a demo.

## Thought experiment

Suppose an agent completes a task correctly but takes three unnecessary actions, exposes data to a tool it did not need, and cannot explain why it chose its route. Is that success? Define your answer before reading the evaluation chapter.

## External reference policy

References are grouped as canonical, implementation, or practical. A link is evidence of what a project or organization documents; it is not evidence that a technique works in every environment. Always check the version, license, maintenance activity, security posture and fit for your use case.
