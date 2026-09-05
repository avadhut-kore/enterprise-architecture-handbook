# Continuous AI Evaluation Architecture (`ai-evaluation/`)

## Executive Summary

Evaluation is the cornerstone of enterprise generative AI engineering. Without deterministic, automated evaluation, software teams cannot confidently upgrade models, modify prompts, adjust chunking algorithms, or refactor tool definitions.

This module details offline benchmark testing, online production sampling, LLM-as-a-Judge architectures, and evaluation-driven CI/CD deployment gates.

---

## Directory Catalog

* **[Offline vs. Online Evaluation Architecture](offline-vs-online-evaluation.md)** — Architectural comparison of pre-deployment golden dataset benchmarks vs. post-deployment live sampling.
* **[LLM-as-a-Judge Architecture](llm-as-a-judge-architecture.md)** — Using frontier models to evaluate application outputs: bias mitigation, rubrics, and consistency scoring.
* **[Golden Datasets Curation & Maintenance](golden-datasets-curation-and-maintenance.md)** — Synthetic data generation, edge-case curation, and test dataset lifecycle management.
* **[Eval-Driven Development & CI/CD Gates](eval-driven-development-and-ci-cd-gates.md)** — Blocking regressions in automated Git pull request pipelines.
* **[Enterprise AI Testing Strategy](ai-testing-strategy.md)** — Complete test pyramid: unit, prompt, retrieval, tool, evaluation, adversarial, and load testing.
