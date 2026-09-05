# Vector Embeddings Architecture (`embeddings/`)

## Executive Summary

Vector embeddings transform unstructured human text, code, audio, and images into dense numerical vectors in high-dimensional continuous mathematical spaces ($\mathbb{R}^d$), enabling semantic search and nearest-neighbor discovery.

This module details embedding model selection, dimensional scaling, distance metric selection, and the critical operational challenge of embedding migrations.

---

## Directory Catalog

* **[Embedding Models & Dimensions](embedding-models-and-dimensions.md)** — Comparing model families, parameter sizes, vector dimensions ($384$ to $3,072$), and MTEB benchmarks.
* **[Distance Metrics & Semantic Similarity](distance-metrics-and-similarity.md)** — Cosine similarity, inner dot product, Euclidean distance ($L_2$), and Manhattan distance ($L_1$).
* **[Re-Embedding & Versioning Migration Architecture](re-embedding-and-versioning-migration.md)** — Operational playbooks for upgrading embedding models across billions of vectors without production downtime.
