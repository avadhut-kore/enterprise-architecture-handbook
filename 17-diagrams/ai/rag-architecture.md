# Enterprise Retrieval-Augmented Generation (RAG) Architecture

Production-grade advanced RAG architecture featuring hybrid search (dense + sparse), reciprocal rank fusion (RRF), cross-encoder reranking, and citation grounding.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph IngestionPipeline ["Offline Ingestion & Indexing"]
        Docs["Enterprise PDF/Doc Corpus"]
        Parser["Document Parser & OCR"]
        Chunker["Semantic Chunker (512 tokens)"]
        DenseModel["Dense Embedding Model"]
        SparseModel["BM25 Lexical Indexer"]
        VectorDB[("Hybrid Vector Store<br/>(Milvus / Pinecone / pgvector)")]

        Docs --> Parser
        Parser --> Chunker
        Chunker --> DenseModel
        Chunker --> SparseModel
        DenseModel --> VectorDB
        SparseModel --> VectorDB
    end

    subgraph OnlineQueryTier ["Online Query & Grounding"]
        UserQuery["User Prompt Query"]
        QueryRewrite["Query Expansion & HyDE Engine"]
        HybridRetrieve["Hybrid Retrieval (Dense + BM25)"]
        Reranker["Cross-Encoder Reranker (Cohere Rerank)"]
        PromptAssembler["Context Grounding Prompt Builder"]
        LLM["LLM Foundation Model"]
        Answer["Factually Grounded Response + Citations"]

        UserQuery --> QueryRewrite
        QueryRewrite --> HybridRetrieve
        HybridRetrieve <-->|"Top-50 Candidates"| VectorDB
        HybridRetrieve --> Reranker
        Reranker -->|"Top-5 Relevant Chunks"| PromptAssembler
        PromptAssembler --> LLM
        LLM --> Answer
    end
```

## PlantUML Specification

```plantuml
@startuml
actor User
participant "Query Engine" as query
database "Vector DB (Hybrid)" as vdb
participant "Reranker (Cohere)" as rerank
participant "LLM (GPT-4o)" as llm

User -> query : Ask Question
query -> query : Expand Query (HyDE)
query -> vdb : Semantic + Keyword Search
vdb -> query : Top 50 Chunks
query -> rerank : Score Semantic Relevance
rerank -> query : Top 5 Best Chunks
query -> llm : Prompt + Grounded Chunks
llm -> User : Answer with Verified Citations
@enduml
```

## Architectural Design Considerations

* **Document-Level Security ACLs**: Embed user permissions directly in vector metadata; filter retrieval results based on requesting user identity.
* **Reranking Impact**: Cross-encoder rerankers dramatically improve answer accuracy by scoring the full interaction between the query and candidate passages.
* **Hallucination Detection**: Implement automated post-generation guardrails checking whether the generated claims are strictly supported by the retrieved context.

## Related Documentation & Patterns

* [Data-Flow: AI RAG Pipeline](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/ai-rag-data-flow.md)
* [Autonomous LLM Agent](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/ai/llm-agent-workflow.md)
* [AI Gateway](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/ai/ai-gateway.md)
