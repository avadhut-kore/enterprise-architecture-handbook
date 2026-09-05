# Short-Term vs. Long-Term AI Memory Architecture

## 1. Memory Tiering Taxonomy

```mermaid
flowchart TD
    subgraph ShortTerm ["1. Short-Term Working Memory (Session-Scoped)"]
        M1["In-Context Sliding Window (Redis)\n- Scope: Active conversation (last 10 minutes)\n- Latency: < 5ms\n- Storage: RAM / In-Memory Key-Value"]
    end

    subgraph LongTerm ["2. Long-Term Memory (User / Entity-Scoped)"]
        M2["Semantic Entity Store (PostgreSQL JSONB)\n- User facts: 'Prefers TypeScript', 'Account: Platinum'\n- Deterministic key-value retrieval"]
        M3["Episodic Vector Store (Qdrant / pgvector)\n- Summarized past conversation episodes\n- Retrieved via cosine similarity"]
    end

    UserPrompt["Inbound User Prompt"] --> M1 & M2 & M3
    M1 & M2 & M3 --> Assembler["Prompt Context Assembler"]
    Assembler --> LLM["Foundation Model Execution"]
```

---

## 2. Memory Eviction Policies
* **Short-Term Memory**: Automatic TTL eviction after 24 hours of user inactivity.
* **Long-Term Memory**: Hierarchical decay algorithm. High-frequency facts maintain high retention weights; ephemeral one-off statements are decayed and purged after 90 days.
