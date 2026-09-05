# Checklist 12: Generative AI & LLMOps Observability Readiness

## 1. Overview
Provides AI/ML engineering teams with a readiness checklist for monitoring enterprise Large Language Model (LLM) applications, RAG pipelines, and vector databases.

---

## 2. Verification Rubric

| LLMOps Area | Inspection Criteria | Status |
| :--- | :--- | :--- |
| **Token Cost Tracking** | Every LLM call records `prompt_tokens`, `completion_tokens`, and calculated dollar cost. | [ ] |
| **Latency Breakdown** | Tracing isolates exact breakdown: Tokenizer ms + Vector Search ms + Time-to-First-Token (TTFT) ms. | [ ] |
| **Vector Retrieval SLI** | Cosine similarity / distance metric recorded for retrieved RAG chunks; alerts on drift $< 0.75$. | [ ] |
| **Prompt Logging Privacy**| Inbound user prompts sanitized to prevent internal customer PII from leaking into telemetry. | [ ] |
| **Hallucination Scoring** | Asynchronous evaluation pipeline samples completions and scores Faithfulness / Answer Relevance. | [ ] |
| **Rate Limit / Quota** | Prometheus tracks upstream LLM provider API rate-limit utilization (tokens-per-minute remaining). | [ ] |
| **Security Guardrails** | Automated telemetry counters record prompt injection attempts and blocked toxic responses. | [ ] |
