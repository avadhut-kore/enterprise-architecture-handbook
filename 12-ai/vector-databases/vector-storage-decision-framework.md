# Vector Storage Decision Framework

## 1. Architectural Selection Scorecard

```mermaid
flowchart TD
    Req["Vector Storage Requirement"] --> ScaleCheck{"Dataset Scale (# of Vectors)?"}
    
    ScaleCheck -->|< 500,000 Vectors| HasPostgres{"Existing Enterprise PostgreSQL Cluster?"}
    HasPostgres -->|Yes| AdoptPG["Adopt pgvector (Extension)\n- Zero new infrastructure to manage\n- ACID relational joins + vectors\n- Lowest operational overhead"]
    HasPostgres -->|No| SearchCheck{"Existing Elasticsearch / OpenSearch?"}
    
    ScaleCheck -->|500k to 50M Vectors| SearchCheck
    SearchCheck -->|Yes| AdoptSearch["Adopt OpenSearch / Elasticsearch Vector Engine\n- Native BM25 + Vector hybrid search\n- Existing enterprise logging/search clusters"]
    SearchCheck -->|No| LowLatency{"Sub-10ms P99 SLA & High QPS (> 500)?"}
    
    ScaleCheck -->|> 50M Vectors| Dedicated["Adopt Dedicated Vector Database\n(Qdrant / Milvus)\n- Distributed sharding & disk-backed quantization\n- Purpose-built vector performance"]
    LowLatency -->|Yes| Dedicated
    LowLatency -->|No| AdoptPG
```

---

## 2. Multi-Engine Comparative Matrix

| Dimension | PostgreSQL + `pgvector` | Elasticsearch / OpenSearch | Dedicated Vector DB (Qdrant / Milvus) |
| :--- | :--- | :--- | :--- |
| **Max Practical Scale** | Up to 1–2 Million vectors. | Up to 50 Million vectors. | Hundreds of Millions to Billions. |
| **Operational Overhead** | Zero (reuses existing DB). | Low (reuses search cluster). | Medium to High (new cluster, new SRE runbooks). |
| **Relational Joins** | **Native SQL Joins** (`WHERE user_id = ...`). | Filter context queries. | Metadata payload filtering only. |
| **Hybrid Search** | Requires manual text index combine. | **Native BM25 + Vector in one query**. | Requires reciprocal rank fusion middleware. |
| **P99 Query Latency** | $25\text{ms} - 80\text{ms}$ | $15\text{ms} - 50\text{ms}$ | **$< 10\text{ms}$** |
| **Cost Profile** | Lowest (amortized into existing DB). | Medium. | High (dedicated memory-intensive instances). |
