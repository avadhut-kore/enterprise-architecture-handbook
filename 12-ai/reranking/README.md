# Search Reranking Architecture (`reranking/`)

## Executive Summary

First-stage retrieval (vector search and BM25) is optimized for **recall**: fetching the top 50 to 100 candidate documents from a corpus of millions in under 30ms.

Second-stage **Reranking** is optimized for **precision**: analyzing the top candidate documents using cross-attention neural models to discard irrelevant noise and order the top 5 chunks with extreme accuracy before injecting them into the LLM context.

---

## Directory Catalog

* **[Cross-Encoder Reranking Architecture](cross-encoder-reranking-architecture.md)** — Cross-attention transformer rerankers (Cohere Rerank, BGE-Reranker), latency vs. precision.
* **[Two-Stage Retrieval Pipeline](two-stage-retrieval-pipeline.md)** — Sizing candidate pools, batch inference windows, and latency budgets.
