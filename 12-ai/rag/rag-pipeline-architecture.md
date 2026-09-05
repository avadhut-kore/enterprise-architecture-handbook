# Enterprise RAG Pipeline Architecture

## 1. The Multi-Tier End-to-End Pipeline

An enterprise RAG system is not a single script; it is a decoupled, multi-tier distributed pipeline composed of an **Offline Ingestion & Indexing Pipeline** and an **Online Real-Time Retrieval & Synthesis Pipeline**:

```mermaid
flowchart TD
    subgraph Offline ["1. Offline Ingestion & Indexing Pipeline (Asynchronous / CDC)"]
        RawDocs[("Enterprise Repositories\n(SharePoint / S3 / Confluence / DBs)")] --> Parse["Document Parser (PDF/DOCX/OCR)"]
        Parse --> Chunk["Semantic Chunker"]
        Chunk --> MetaInject["Metadata & ACL Enrichment"]
        MetaInject --> EmbedWorker["Batch Embedding Worker (Dense & Sparse)"]
        EmbedWorker --> VecIndex[("Vector & Keyword Indexes")]
    end

    subgraph Online ["2. Online Query & Synthesis Pipeline (Real-Time Synchronous)"]
        UserQuery["User Inbound Query"] --> Rewriter["Query Rewriting & HyDE"]
        Rewriter --> HybridRet["Hybrid Retrieval (Dense Vector + BM25)"]
        VecIndex -.-> HybridRet
        HybridRet --> Filter["Tenant ACL & Metadata Filter"]
        Filter --> Reranker["Cross-Encoder Reranker (Top-N to Top-K)"]
        Reranker --> PromptBuilder["Prompt Assembler & Context Compressor"]
        PromptBuilder --> LLM["Foundation Model (Streaming Generation)"]
        LLM --> OutStream["Streaming Answer with Exact Citations"]
    end
```

---

## 2. Pipeline SLAs & Latency Budgeting

| Pipeline Stage | Target Latency | Architectural Strategy |
| :--- | :--- | :--- |
| **Query Rewriting / HyDE** | $50\text{ms} - 150\text{ms}$ | Small, fast model (8B parameter) or local CPU ONNX runtime. |
| **Vector & BM25 Retrieval**| $15\text{ms} - 40\text{ms}$ | Parallel async RPCs; HNSW index residing in-memory. |
| **Cross-Encoder Reranking**| $40\text{ms} - 100\text{ms}$ | Rerank only top 30 candidates to select top 5; GPU batch inference. |
| **LLM Generation (TTFT)** | $300\text{ms} - 600\text{ms}$ | High-performance serving engine (vLLM / TensorRT-LLM). |
| **Total P99 Latency** | $< 1,000\text{ms}$ | Strict timeout budgets per stage with fallback defaults. |
