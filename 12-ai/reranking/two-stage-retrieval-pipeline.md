# Two-Stage Retrieval Pipeline Architecture

## 1. High-Precision Retrieval Topology

```mermaid
flowchart TD
    Query["User Query"] --> Stage1["Stage 1: High-Recall Retrieval (Fast / Coarse)\n- Parallel BM25 + Vector Search\n- Searches 10,000,000 documents in 25ms\n- Retrieves Top 50 Candidates"]
    
    Stage1 --> Top50["Top 50 Raw Candidates"]
    
    Top50 --> Stage2["Stage 2: High-Precision Reranking (Deep / Fine)\n- Cross-Encoder Neural Reranker (Cohere / BGE)\n- Evaluates full query-document token interactions in 60ms\n- Selects Top 5 Highly Relevant Chunks"]
    
    Stage2 --> Top5["Top 5 Clean Chunks"]
    Top5 --> LLM["LLM Synthesis (Concise, Noise-Free Context)"]
```

---

## 2. Performance & Quality Impact
Empirical testing across enterprise datasets demonstrates that introducing a second-stage Cross-Encoder reranker **boosts RAG answer accuracy by 25%–35%** while keeping total retrieval latency under $100\text{ms}$.
