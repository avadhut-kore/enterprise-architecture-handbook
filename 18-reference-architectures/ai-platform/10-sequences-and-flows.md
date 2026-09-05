# Sequence Flows & Failure Recovery: Enterprise AI Platform

## 1. End-to-End RAG Query Execution Sequence

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant Gateway as AI Gateway
    participant Cache as Semantic Cache (Redis)
    participant RAG as RAG Orchestrator
    participant Qdrant as Vector DB
    participant LLM as Model Backend (vLLM)

    User->>Gateway: POST /v1/chat/completions (Query)
    Gateway->>Gateway: Sanitize Input & Mask PII
    Gateway->>Cache: Check Cosine Similarity (threshold: 0.95)
    alt Cache Hit
        Cache-->>Gateway: Return Cached Completion
        Gateway-->>User: Stream Cached SSE Tokens
    else Cache Miss
        Gateway->>RAG: Forward Query with User ACLs
        RAG->>Qdrant: Hybrid Search (Dense Vector + BM25)
        Qdrant-->>RAG: Return Top-50 Chunks
        RAG->>RAG: Rerank to Top-5 Chunks
        RAG->>LLM: Dispatch Augmented Prompt with Context
        loop Streaming Response
            LLM-->>Gateway: SSE Token Chunk
            Gateway-->>User: SSE Token Chunk
        end
        Gateway->>Cache: Asynchronously Store Embedding & Response
    end
```

---

## 2. Failure Recovery Flow: Frontier Model Rate Limit (HTTP 429)
When external API returns HTTP 429:
1. Circuit breaker trips immediately.
2. Request is automatically downgraded and routed to self-hosted vLLM fallback pool within 150ms.
3. User receives complete response without disruption.
