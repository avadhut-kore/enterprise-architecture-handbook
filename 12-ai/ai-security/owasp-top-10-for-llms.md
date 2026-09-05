# OWASP Top 10 for LLM Applications: Architectural Mitigations

## 1. Threat Taxonomy & Architectural Defenses

| Vulnerability ID | Threat Name | Core Architectural Vulnerability | Enterprise Architectural Mitigation |
| :--- | :--- | :--- | :--- |
| **LLM01:2025** | **Prompt Injection** | Attacker manipulates model input via direct or indirect prompts to hijack execution flow. | Multi-tier guardrails; XML delimiters; instruction-data separation; least-privilege tools. |
| **LLM02:2025** | **Sensitive Information Disclosure** | Model inadvertently reveals private corporate data, PII, or system secrets in responses. | Inbound PII masking; outbound data loss prevention (DLP); Zero Data Retention cloud agreements. |
| **LLM03:2025** | **Supply Chain Vulnerabilities** | Compromised third-party models, poisoned fine-tuning datasets, or malicious Python packages. | Cryptographic model signing (Sigstore Cosign); CycloneDX SBOMs; private PyPI proxy mirrors. |
| **LLM04:2025** | **Data & Model Poisoning** | Malicious data injected into training corpora or RAG vector databases to introduce backdoors. | Cryptographic data provenance; strict source authority weighting; automated anomaly detection. |
| **LLM05:2025** | **Improper Output Handling** | Model output passed blindly to downstream shells, web browsers, or SQL interpreters. | Treat all LLM output as untrusted user input; strict JSON Schema validation; output HTML escaping. |
| **LLM06:2025** | **Excessive Agency** | Model granted autonomous write permissions to critical systems without human approval. | Granular tool authorization (ABAC); read-only replicas; mandatory human-in-the-loop for state mutations. |
| **LLM07:2025** | **System Prompt Leakage** | Attacker tricks the model into disclosing proprietary internal instructions or system prompts. | Egress canary token monitoring; strip sensitive business rules from system prompts into backend logic. |
| **LLM08:2025** | **Vector & Embedding Weaknesses** | Vector similarity exploited to retrieve unauthorized tenant chunks or bypass keyword filters. | Mandatory tenant pre-filtering in vector DB queries; cross-encoder reranking verification. |
| **LLM09:2025** | **Misinformation & Hallucination** | Model outputs factual falsehoods that cause financial, medical, or operational damage. | RAG retrieval grounding; citation validation; temperature = 0.0; automated faithfulness scoring. |
| **LLM10:2025** | **Unbounded Consumption** | Excessive input/output tokens causing severe denial-of-wallet (DoW) resource exhaustion. | Distributed sliding-window TPM/RPM rate limiting; hard token caps per session; semantic caching. |
