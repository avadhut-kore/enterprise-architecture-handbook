# Vector Storage & Search Infrastructure (`vector-databases/`)

## Executive Summary

Vector databases provide specialized storage and indexing for high-dimensional numerical vectors, executing Approximate Nearest Neighbor (ANN) search across millions or billions of items in sub-50ms latency.

This module provides the architectural foundation for evaluating, sizing, sharding, and operating vector datastores within enterprise ecosystems.

---

## Directory Catalog

* **[Vector Storage Decision Framework](vector-storage-decision-framework.md)** — Decision matrices comparing dedicated vector engines, relational extensions (pgvector), and enterprise search clusters.
* **[Dedicated vs. Relational Vector Databases](dedicated-vs-relational-vector-databases.md)** — Architectural trade-offs between Pinecone/Qdrant/Milvus and PostgreSQL/Elasticsearch.
* **[Approximate Nearest Neighbor (ANN) Algorithms](approximate-nearest-neighbor-algorithms.md)** — Hierarchical Navigable Small World (HNSW), Inverted File Index (IVF), and Product Quantization (PQ).
* **[Scaling & Sharding Vector Indexes](scaling-and-sharding-vector-indexes.md)** — Memory mapping, horizontal partitioning, distributed routing, and high-availability replication.
