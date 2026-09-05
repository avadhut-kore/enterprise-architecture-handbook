# Data Architecture: RAG Pipelines & Vector Storage

## 1. Document Ingestion & Hybrid Indexing Topology

```
[Raw Files: PDF, DOCX, HTML] ──► [Extraction Pipeline (Unstructured / Tika)]
                                                │
                                                ▼
                                    [Context-Aware Chunking]
                                    ├── Sliding Window (512 tokens, 10% overlap)
                                    └── Semantic Boundary / Heading Detection
                                                │
                                                ▼
                                    [Embedding Generation]
                                    (text-embedding-3-large / BAAI/bge-large)
                                                │
                               ┌────────────────┴────────────────┐
                               ▼                                 ▼
                     [Dense Vector Index]              [Sparse Keyword Index]
                     (HNSW / Cosine Metric)            (BM25 Token Inverted Index)
                               │                                 │
                               └────────────────┬────────────────┘
                                                ▼
                                    [Hybrid Reciprocal Rank Fusion (RRF)]
                                                │
                                                ▼
                                    [Cross-Encoder Reranker]
                                    (bge-reranker-large)
```

---

## 2. Vector Index Schema (Qdrant Example)
- **Collection Name**: `enterprise_knowledge_base`
- **Vector Dimension**: 1536 (Normalized Euclidean / Cosine)
- **HNSW Parameters**: `m = 16`, `ef_construct = 128`
- **Payload Schema**:
  - `doc_id` (UUID): Source document identifier.
  - `tenant_id` (String): Multi-tenant isolation partition key.
  - `acl_groups` (Array of Strings): Active Directory group SIDs authorized to view chunk.
  - `chunk_text` (String): Raw textual content.
  - `created_at` (Timestamp): Modification date for recency filtering.
