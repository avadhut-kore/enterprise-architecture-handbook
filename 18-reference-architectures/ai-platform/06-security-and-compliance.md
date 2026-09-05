# Security, AI Safety & Compliance Architecture

## 1. Defense-in-Depth AI Guardrails
- **Prompt Injection Defense**: Multi-stage classification. System instructions are signed with cryptographic HMAC tokens; user input is sanitized and enclosed in strict XML delimiters (`<user_query>...</user_query>`).
- **PII Scrubbing**: Presidio analyzer detects named entities, SSNs, and credit cards, replacing them with reversible encrypted tokens (`[TOKEN_SSN_1]`). The modern response decrypts tokens only for authorized callers.
- **Model Poisoning Mitigation**: All training datasets and RAG repositories require cryptographic signing and provenance validation.

---

## 2. Compliance Framework Control Mapping

| Regulatory Framework | Technical Control Implementation |
| :--- | :--- |
| **EU AI Act (High-Risk AI)** | Immutable audit logging of all prompts, model versions, temperatures, and generated outputs to WORM S3 storage. |
| **NIST AI RMF 1.0** | Automated continuous evaluation of model toxicity, bias, and hallucination scores using synthetic benchmarking suites. |
| **GDPR / CCPA** | Vector database partitions tagged by `tenant_id` and `user_id`; automated cascade deletion workflows. |
| **SOC 2 Type II** | Zero-trust mTLS 1.3 encryption across all gateway-to-model and gateway-to-vector hops; HashiCorp Vault secrets. |
