# Guardrail Frameworks Architectural Comparison

## 1. Framework Evaluation Matrix

| Framework | Architecture Type | Latency Overhead | Integration Model | Ideal Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **NVIDIA NeMo Guardrails** | Programmable dialog rails (Colang) + neural models. | Medium ($50\text{ms} - 150\text{ms}$). | Python library / Sidecar container. | Complex conversational flows requiring rigid topical guardrails. |
| **Meta Llama Guard 3** | Dedicated fine-tuned 8B parameter safety classifier. | Low ($30\text{ms} - 60\text{ms}$ on GPU). | Standard LLM endpoint / vLLM. | High-throughput content moderation and jailbreak detection. |
| **Guardrails AI** | Schema-driven output validators (Pydantic / Regex). | Ultra-low ($2\text{ms} - 10\text{ms}$). | Python runtime package. | Strict JSON schema compliance and structural data extraction. |
| **Azure AI Content Safety** | Managed cloud SaaS API. | Medium ($40\text{ms} - 80\text{ms}$). | External HTTPS REST call. | Turnkey cloud deployments across Azure ecosystem. |
