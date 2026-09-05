# Retrieval-Augmented Generation (RAG) Architecture (`rag/`)

## Executive Summary

Retrieval-Augmented Generation (RAG) is the enterprise architectural pattern for grounding foundation models in private, up-to-date, domain-specific enterprise knowledge without the prohibitive cost, latency, and obsolescence of continuous model fine-tuning.

This module establishes the comprehensive architecture of enterprise RAG systems, from multi-format ingestion and semantic chunking to vector indexing, hybrid retrieval, graph-augmented knowledge, and the RAG evaluation triad.

---

## Directory Catalog

* **[RAG Pipeline Architecture](rag-pipeline-architecture.md)** — End-to-end multi-tier pipeline: ingestion, indexing, retrieval, reranking, synthesis.
* **[Document Parsing & Chunking Strategies](document-parsing-and-chunking.md)** — Fixed-size, semantic, sentence-window, and document-aware chunking trade-offs.
* **[Metadata Filtering & Multi-Tenancy](metadata-filtering-and-multitenancy.md)** — Logical tenant isolation, ACL synchronization, and pre/post-retrieval filtering.
* **[Query Transformation & Rewriting](query-transformation-and-rewriting.md)** — Hypothetical Document Embeddings (HyDE), query decomposition, and multi-query expansion.
* **[RAG Variants Comparison](rag-variants-comparison.md)** — Comprehensive analysis comparing Basic, Hybrid, GraphRAG, Multi-Hop, Agentic, and Hierarchical RAG.
* **[GraphRAG Architecture](graph-rag-architecture.md)** — Combining knowledge graphs (Neo4j) with vector embeddings for global document summarization and relationship traversal.
* **[Agentic RAG Architecture](agentic-rag-architecture.md)** — Dynamic multi-step reasoning, self-correction, adaptive retrieval routers, and reflection loops.
* **[Parent-Child & Hierarchical Chunking](parent-child-and-hierarchical-chunking.md)** — Decoupling retrieval granularity (small child chunks) from generation context (large parent chunks).
* **[RAG Evaluation & The RAG Triad](rag-evaluation-and-triad.md)** — Quantifying Faithfulness, Answer Relevance, and Context Relevance using automated evaluation pipelines.
