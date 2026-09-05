# AI Orchestration Engines & State Graphs (`ai-orchestration/`)

## Executive Summary

Connecting LLMs, vector search engines, deterministic business logic, and human approval gates requires specialized orchestration runtimes.

This module evaluates application-level orchestration, stateful graph engines (LangGraph), durable workflow orchestrators (Temporal), and automated compensation patterns.

---

## Directory Catalog

* **[Orchestration Engines Comparison](orchestration-engines-comparison.md)** — Architectural trade-offs: Plain Application Code vs. Workflow Engines (Temporal) vs. State Graphs (LangGraph).
* **[State Graphs & Cyclic Execution](state-graphs-and-cyclic-execution.md)** — Modeling multi-agent loops, state checkpointing, and branch pruning with directed graphs.
* **[Compensation Patterns for AI](compensation-patterns-for-ai.md)** — Reversing partial mutations when downstream AI reasoning or schema validation fails.
