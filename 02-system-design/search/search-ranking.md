# Search Ranking & Multi-Stage Re-Ranking

## 1. Two-Stage Retrieval Pipeline
Evaluating complex machine learning models across 100 million documents is computationally impossible in $<100\text{ ms}$.

```mermaid
flowchart LR
    Query[User Query] --> L1[Stage 1: Fast BM25 Retrieval -> Top 1,000 Candidates in 10ms]
    L1 --> L2[Stage 2: Machine Learning GBDT / Deep Model -> Top 20 Ranked in 30ms]
    L2 --> Results[Final Search Result Page]
```
