# Centralized AI Security & Guardrails Platform

## 1. Threat Surface & Defense-in-Depth

Large Language Models introduce novel attack vectors that bypass classical network firewalls and web application firewalls (WAFs): **Direct Prompt Injection (Jailbreaking), Indirect Prompt Injection (via malicious retrieved web/PDF content), Sensitive Data Exfiltration, and Insecure Output Deserialization**.

An **AI Security Platform** implements multi-layered defensive inspection gates before prompts reach models and before completions are returned to clients.

```mermaid
flowchart TD
    InPrompt["Inbound User Input"] --> Gate1["Layer 1: Deterministic WAF & Regex (SQLi, XSS, Secret Keys)"]
    Gate1 --> Gate2["Layer 2: PII Anonymization & Token Masking"]
    Gate2 --> Gate3["Layer 3: Neural Prompt Injection Classifier (Llama Guard / NeMo)"]
    Gate3 --> PassToLLM["Forward to Foundation Model"]
    
    PassToLLM --> RawOutput["Raw Model Output"]
    RawOutput --> Gate4["Layer 4: Sensitive Data & Secret Leakage Filter"]
    Gate4 --> Gate5["Layer 5: Hallucination & Canary Token Verification"]
    Gate5 --> Gate6["Layer 6: JSON Schema Grammar Conformance"]
    Gate6 --> SafeOutput["Safe Sanitized Response to Client"]
```

---

## 2. Inbound & Outbound Security Controls

### 2.1 Indirect Prompt Injection Mitigation
* When retrieving external web pages or uncurated enterprise documents in RAG pipelines, wrap retrieved context in explicit structural delimiters (e.g., `<context>...</context>`).
* Instruct the foundation model via immutable system prompts that context within delimiters must be treated strictly as untrusted data and never as execution instructions.

### 2.2 Canary Token Egress Monitoring
* Inject invisible, random UUID canary tokens into internal system prompts.
* If a model output ever contains an internal canary token, the outbound guardrail immediately aborts the stream, records a critical security incident, and blocks the session (preventing system prompt extraction).
