# Dedicated Vector Databases vs. Relational Extensions

## 1. The Operational Reality of New Datastores

Adopting a dedicated vector database (Pinecone, Qdrant, Milvus, Chroma) introduces significant enterprise overhead: new security reviews, new IAM credentials, separate backup procedures, compliance audits, and data synchronization workers.

Architects should **default to existing enterprise databases (e.g., PostgreSQL with `pgvector`)** unless specific scale or latency thresholds demand a dedicated engine.

---

## 2. When to Transition to a Dedicated Vector Engine
Transition to a dedicated vector database if and only if:
1. **Scale Exceeds 2 Million Vectors**: PostgreSQL `pgvector` HNSW indexes begin consuming massive shared memory buffers, competing with relational cache hit ratios.
2. **Strict Sub-10ms P99 Latency at 1,000+ QPS**: Dedicated vector engines utilize C++ and Rust vector kernels optimized for AVX-512 and GPU-accelerated nearest neighbor search.
3. **Advanced Filtering Topologies**: Dedicated engines feature hardware-level pre-filtering that prunes vector search graphs dynamically during traversal.
