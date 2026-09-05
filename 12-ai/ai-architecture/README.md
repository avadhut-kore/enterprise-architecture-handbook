# AI Architecture Foundations (`ai-architecture/`)

## Executive Summary

The `ai-architecture/` module codifies the foundational architectural principles, system boundaries, and workload classifications governing modern artificial intelligence within enterprise software systems.

Architects must recognize that AI components introduce fundamentally distinct operational and engineering realities compared to traditional software: **non-deterministic outputs, probabilistic state transitions, non-linear compute latency, asymmetric memory scaling (KV caching), and novel vulnerability surfaces (prompt injection, data poisoning)**.

---

## Core Directory Index

* **[AI System Boundaries](ai-system-boundaries.md)** — Defining the architectural boundary between deterministic enterprise systems and probabilistic AI runtimes.
* **[AI Workloads Taxonomy](ai-workloads-taxonomy.md)** — Architectural classification of predictive ML, analytical AI, generative systems, and autonomous agents.
* **[Predictive vs. Generative vs. Agentic Systems](predictive-vs-generative-vs-agentic.md)** — Comparative architecture, latency profiles, failure modes, and execution models.
* **[Traditional to AI-Native Architectural Evolution](traditional-to-ai-native-evolution.md)** — The 5-stage evolutionary path from classical software to AI-native systems.
