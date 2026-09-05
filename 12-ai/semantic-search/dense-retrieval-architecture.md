# Dense Retrieval Architecture & Semantic Search Pipelines

## 1. The Dual-Encoder Pattern

In dense retrieval, documents and queries are projected into the same high-dimensional embedding space using a **Bi-Encoder neural network**:

```mermaid
flowchart TD
    subgraph Offline ["Offline Indexing Pipeline"]
        Doc["Document Text"] --> DocEncoder["Bi-Encoder Document Model"]
        DocEncoder --> DocVec["Dense Document Vector\n(d = 1024)"]
        DocVec --> VecIndex[("Vector Index (HNSW)")]
    end

    subgraph Online ["Online Query Pipeline"]
        Query["User Search Query"] --> QueryEncoder["Bi-Encoder Query Model"]
        QueryEncoder --> QueryVec["Dense Query Vector\n(d = 1024)"]
        QueryVec --> SearchEngine["ANN Search Engine"]
        VecIndex -.-> SearchEngine
        SearchEngine --> TopK["Top-K Semantically Similar Documents (sub-20ms)"]
    end
```

---

## 2. Limitations of Pure Dense Retrieval
While dense retrieval understands abstract concepts, it suffers from two major enterprise blindspots:
1. **Exact Identifier Blindness**: Fails when searching for exact alphanumeric product codes, serial numbers, or error strings (`ERR-4091-B`).
2. **Out-of-Domain Failure**: Degrades significantly when exposed to specialized enterprise jargon not present in the embedding model's pretraining corpus.
