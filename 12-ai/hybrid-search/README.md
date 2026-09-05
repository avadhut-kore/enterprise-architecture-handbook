# Hybrid Search Architecture (`hybrid-search/`)

## Executive Summary

Neither pure lexical keyword search (BM25) nor pure semantic dense vector search is sufficient for enterprise production. 

**Hybrid Search** combines the exact-match precision of sparse lexical search with the conceptual understanding of dense vector retrieval, fusing results using rank aggregation algorithms.

---

## Directory Catalog

* **[Combining Dense & Sparse Search](combining-dense-and-sparse-search.md)** — Architectural topologies for executing parallel BM25 and vector queries.
* **[Reciprocal Rank Fusion (RRF)](reciprocal-rank-fusion.md)** — Mathematical formulations, scale-invariant score normalization, and ranking fusion.
