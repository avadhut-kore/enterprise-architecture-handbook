# ADR-0007: Deterministic Rule Engine vs LLM for Compliance Evaluation

---
**Metadata**:
* **ADR ID**: ADR-0007
* **Title**: Evaluation Engine — Deterministic Rules vs Generative LLM Pipeline
* **Status**: Accepted
* **Date**: 2026-04-01
* **Decision Owners**: Chief Compliance Architect, AI Platform Lead
---

## 1. Context & Problem Statement
Evaluate whether to use an LLM pipeline or a deterministic rule engine (Drools / JSON Schema engine) for evaluating trade compliance against federal sanction lists.

## 2. Decision & Rationale
Adopt a **Deterministic Rule Engine** with cryptographic hash verification.
Regulatory compliance demands 100% mathematical reproducibility, zero hallucination tolerance, and transparent explainability under subpoena. Generative LLM pipelines are non-deterministic and introduce unacceptable regulatory and legal liabilities for strict binary compliance decisions. LLMs will only be used in an advisory capacity for preliminary text summarization.
