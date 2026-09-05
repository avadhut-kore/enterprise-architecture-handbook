# Model Licensing, Governance & Intellectual Property Risk

## 1. The Legal Complexity of Open-Weights Licenses

Not all "open source" AI models are truly open source according to Open Source Initiative (OSI) definitions. Many modern open-weights models are distributed under **permissive commercial licenses with restrictive behavioral clauses or user thresholds**.

Architects must audit model licenses with corporate legal counsel before embedding models into commercial software products.

```mermaid
flowchart TD
    License["Model License Audit"] --> Type{"License Classification"}
    
    Type -->|Pure OSI Open Source (Apache 2.0 / MIT)| Open["Full Commercial Freedom\n- Mistral 7B (Apache 2.0)\n- Permissive modification & redistribution"]
    Type -->|Community Commercial with Restrictions| Comm["Commercial with Thresholds\n- Meta Llama 3 Community License\n- Free commercial use up to 700M monthly active users\n- Cannot use outputs to train competing models"]
    Type -->|Research Only / Non-Commercial| Restrict["Strictly Banned for Commercial Products\n- CC-BY-NC (Non-Commercial)\n- Research-only checkpoints"]
```

---

## 2. Copyright & Intellectual Property Indemnification
* **Model Training Data Risk**: If a foundation model was trained on copyrighted text or code without proper authorization, enterprise users could face vicarious infringement claims.
* **Enterprise Indemnification**: Major cloud providers (Microsoft Azure OpenAI, Google Cloud, AWS) offer **IP Indemnification Clauses** in enterprise enterprise agreements, legally protecting the enterprise if model outputs generate copyrighted content, provided the customer uses built-in guardrails and content filters.
