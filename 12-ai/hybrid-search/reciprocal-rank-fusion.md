# Reciprocal Rank Fusion (RRF) Architecture

## 1. The Normalization Problem

BM25 produces unbounded positive floating-point scores ($[0, \infty)$), while cosine similarity produces scores bounded between $[-1, 1]$. Linearly combining raw scores ($\alpha \cdot S_{\text{BM25}} + \beta \cdot S_{\text{dense}}$) requires brittle manual tuning that breaks whenever document lengths or index statistics change.

**Reciprocal Rank Fusion (RRF)** solves this by operating exclusively on **ordinal ranks** rather than arbitrary numerical scores.

---

## 2. Mathematical Formulation

For any document $d$ appearing in candidate rankings across multiple search engines:
$$\text{RRF\_Score}(d) = \sum_{m \in M} \frac{1}{k + r_m(d)}$$
Where:
* $M$ is the set of search systems (e.g., BM25 and Vector Search).
* $r_m(d)$ is the rank position of document $d$ in system $m$ (1-indexed: $1, 2, 3 \dots$).
* $k$ is a smoothing constant (standard industry default $k = 60$) that prevents top-ranked items from dominating the score excessively.

```python
def reciprocal_rank_fusion(dense_results, sparse_results, k=60):
    rrf_scores = {}
    for rank, doc_id in enumerate(dense_results, start=1):
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    for rank, doc_id in enumerate(sparse_results, start=1):
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    
    # Sort documents in descending order of fused score
    return sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)
```
