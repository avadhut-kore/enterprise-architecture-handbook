# Foundation Model Selection Framework (`model-selection/`)

## Executive Summary

Selecting a foundation model is one of the most consequential architectural decisions in enterprise AI engineering. Choosing the wrong model class leads to **severe cost inflation, unacceptable latency violations, data sovereignty breaches, or catastrophic task failure rates**.

This module establishes the multi-dimensional criteria used to objectively evaluate and select foundation models.

---

## Directory Catalog

* **[Model Selection Framework](model-selection-framework.md)** — Comprehensive scorecard evaluating reasoning capability, latency, context size, cost, and hosting options.
* **[Open vs. Closed Models](open-vs-closed-models.md)** — Architectural trade-offs between proprietary hosted APIs (OpenAI, Anthropic) and open-weights models (Llama, Mistral).
* **[Parameter Scale Trade-Offs](parameter-scale-tradeoffs.md)** — Comparing Small Language Models (3B–8B) vs. Medium (14B–32B) vs. Large (70B–405B).
* **[Model Licensing & Intellectual Property Risk](model-licensing-and-ip-risk.md)** — Commercial use restrictions, training data provenance, indemnification, and patent grants.
