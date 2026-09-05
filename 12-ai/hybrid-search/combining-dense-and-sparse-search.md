# Combining Dense & Sparse Search Architecture

## 1. The Hybrid Search Pipeline

```mermaid
flowchart TD
    UserQuery["User Query: 'Replace alternator on Model X ERR-409'"] --> Fork["Parallel Query Fork"]
    
    subgraph ParallelEngines ["Parallel Execution Tier"]
        Fork --> SparseBranch["1. Lexical BM25 Search (Sparse)\n- Matches exact tokens: 'alternator', 'ERR-409'\n- Catches IDs, codes, exact acronyms"]
        Fork --> DenseBranch["2. Dense Vector Search (HNSW)\n- Matches semantic concepts: 'vehicle power generator failure'\n- Catches synonyms and intent"]
    end

    SparseBranch --> ListA["Ranked List A (BM25 Scores)"]
    DenseBranch --> ListB["Ranked List B (Cosine Scores)"]
    
    ListA & ListB --> FusionEngine["Rank Fusion Engine (RRF / Convex Combination)"]
    FusionEngine --> FinalList["Fused High-Relevance Results"]
```

---

## 2. Why Hybrid Search is Mandatory in the Enterprise
In a legal, financial, or engineering context, users constantly search with mixed queries: *"What does clause 4.2 say about indemnification liability?"*
* BM25 matches `"clause 4.2"` perfectly but fails on semantic variations of `"indemnification liability"`.
* Dense vector search understands the legal concept of liability but fails to locate `"clause 4.2"`.
* **Hybrid search retrieves the exact clause with 100% reliability**.
