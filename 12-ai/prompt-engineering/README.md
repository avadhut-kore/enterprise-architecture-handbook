# Prompt Engineering & Management Architecture (`prompt-engineering/`)

## Executive Summary

In enterprise systems, **prompts are executable production code**. Treating prompts as informal strings scattered across application files is an operational failure. 

This module establishes the architectural standards for managing prompts as version-controlled software artifacts subject to automated testing, CI/CD deployment pipelines, and defensive security hardening.

---

## Directory Catalog

* **[Prompts as Code & Architecture](prompts-as-code.md)** — Decoupling prompts from application codebases, declarative templating, and prompt registries.
* **[Prompt Versioning & CI/CD Pipelines](prompt-versioning-and-cicd.md)** — Semantic versioning (SemVer) for prompts, automated regression testing, and canary prompt rollouts.
* **[Few-Shot & In-Context Learning](few-shot-and-in-context-learning.md)** — Optimal few-shot selection, dynamic exemplar retrieval, and formatting patterns.
* **[System Instruction Architecture](system-instruction-architecture.md)** — Layered system instructions, behavioral boundaries, and tone/style enforcement.
* **[Prompt Injection Defense in Prompt Design](prompt-injection-defense-in-prompts.md)** — Delimiter engineering, instruction-data separation, and defensiveness patterns.
