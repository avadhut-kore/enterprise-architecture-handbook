# Agentic Workflows & Durable Automation (`agentic-workflows/`)

## Executive Summary

A critical architectural law: **Prefer deterministic workflows when the process is deterministic.** 

Autonomous, free-form agents should never be used to execute standard, well-defined business processes. **Agentic Workflows** combine the rigid guarantees of deterministic state machines with targeted AI reasoning at specific steps requiring unstructured synthesis or ambiguity resolution.

---

## Directory Catalog

* **[Deterministic vs. Agentic Workflows](deterministic-vs-agentic-workflows.md)** — Architectural decision matrix: when to use code, workflow engines, or autonomous agents.
* **[Human-in-the-Loop Architecture](human-in-the-loop-architecture.md)** — Asynchronous approval gates, escalation workflows, and confidence-based routing.
* **[Long-Running Agentic Workflows](long-running-agentic-workflows.md)** — Managing stateful execution over days/weeks with durable execution runtimes (Temporal).
* **[Failure Recovery & Compensation](failure-recovery-and-compensation.md)** — Sagas, compensating transactions, and graceful degradation in AI pipelines.
