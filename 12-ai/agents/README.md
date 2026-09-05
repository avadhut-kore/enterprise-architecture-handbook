# Autonomous AI Agents Architecture (`agents/`)

## Executive Summary

An **AI Agent** is an autonomous or semi-autonomous software entity that combines a foundation model reasoning core with planning capabilities, short/long-term memory, environmental perception, and tool invocation to accomplish multi-step objectives.

This module details the architectural engineering of agents, focusing on deterministic loop control, cognitive planning, state persistence, and hard guardrails that prevent runaway execution.

---

## Directory Catalog

* **[Agent Foundations & The ReAct Loop](agent-foundations-and-react-loop.md)** — Reasoning and Acting (ReAct) paradigm, observation integration, and environmental feedback.
* **[Planning, Reasoning & Reflection](planning-reasoning-and-reflection.md)** — Plan-and-Solve architectures, tree of thoughts, and self-reflective correction loops.
* **[Agent State & Goal Management](agent-state-and-goal-management.md)** — Task decomposition, scratchpad management, goal fulfillment criteria, and persistent state machines.
* **[Agent Guardrails & Termination Criteria](agent-guardrails-and-termination-criteria.md)** — Circuit breakers, maximum iteration ceilings, token budget fences, and dead-loop detection.
