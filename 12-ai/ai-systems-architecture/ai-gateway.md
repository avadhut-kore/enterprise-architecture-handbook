# Enterprise AI Gateway Architecture

## 1. Executive Summary & Core Responsibilities

An **AI Gateway** is a specialized API reverse proxy optimized specifically for Large Language Models and Generative AI traffic. Unlike traditional API gateways (Kong, Apigee, AWS API Gateway)—which focus primarily on routing static REST endpoints—an AI Gateway manages **token budgets, prompt security, streaming connections, semantic caching, model fallback cascades, and LLM provider abstractions**.

```mermaid
flowchart TD
    Req["Inbound Client Request"] --> AuthN["1. AuthN & Tenant Identification (JWT / API Key)"]
    AuthN --> RateLimit["2. Token Rate Limiting & Budget Check"]
    RateLimit --> InGuard["3. Inbound Security (Prompt Injection & PII Masking)"]
    InGuard --> Cache{"4. Semantic Cache Check"}
    Cache -->|Hit (Similarity > 0.95)| CacheResp["Serve Cached Response (10ms)"]
    Cache -->|Miss| Router["5. Dynamic Model Router & Load Balancer"]
    Router --> PrimaryModel["Primary Model (e.g., Azure OpenAI)"]
    PrimaryModel -.->|5xx Error / Rate Limited| FallbackModel["Fallback Model (e.g., Bedrock / vLLM)"]
    PrimaryModel --> OutGuard["6. Outbound Guardrails & Schema Enforcer"]
    FallbackModel --> OutGuard
    OutGuard --> Stream["7. Chunked Streaming Response (SSE)"]
```

---

## 2. Inbound Pipeline Architecture

1. **Authentication & Authorization**: Validates incoming OAuth 2.0 / JWT tokens, resolves tenant membership, and checks model access permissions.
2. **Token Rate Limiting**: Unlike traditional requests-per-minute (RPM) limiters, AI Gateways enforce **Tokens-Per-Minute (TPM)** limiters using distributed sliding-window algorithms in Redis.
3. **PII Masking**: Automatically detects SSNs, credit cards, and email addresses using high-speed regex and lightweight NER models, replacing sensitive entities with anonymized placeholders before forwarding to third-party providers.
4. **Fallback & Circuit Breaking**: If an upstream model provider returns HTTP 429 (Rate Limit Exceeded) or HTTP 503 (Overloaded), the gateway transparently reroutes the request to an alternative cloud provider or local open-weights cluster within 150ms.
