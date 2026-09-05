# Bi-Encoders vs. Cross-Encoders in Search Architecture

## 1. The Fundamental Trade-Off: Speed vs. Interaction

```mermaid
flowchart TD
    subgraph BiEncoder ["1. Bi-Encoder (Dense Retrieval)"]
        Q1["Query"] --> E1["Encoder"] --> V1["Vector Q"]
        D1["Document"] --> E2["Encoder"] --> V2["Vector D"]
        V1 & V2 --> Sim["Cosine Similarity (Dot Product)"]
        Note1["Vectors computed INDEPENDENTLY.\nPrecompute millions of document vectors offline.\nQuery speed: 5ms - 20ms across millions of docs."]
    end

    subgraph CrossEncoder ["2. Cross-Encoder (Reranker)"]
        QD["Combined Input: [CLS] Query [SEP] Document"] --> FullTransformer["Full Transformer Self-Attention Layers\n(Every query token attends to every document token)"]
        FullTransformer --> Score["Relevance Score [0.0 - 1.0]"]
        Note2["No precomputation possible!\nMust run full transformer for every candidate pair.\nQuery speed: 50ms for just 20 documents."]
    end
```

---

## 2. Architectural Conclusion: The Two-Stage Pipeline
Never use Cross-Encoders for initial retrieval across a full database. Always use a **Bi-Encoder** to rapidly retrieve the top 50 candidates from millions of documents, then use a **Cross-Encoder** as a second-stage reranker on those 50 candidates.
