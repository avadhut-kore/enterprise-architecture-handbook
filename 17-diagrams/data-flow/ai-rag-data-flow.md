# AI / Retrieval-Augmented Generation (RAG) Data Ingestion Pipeline

End-to-end multi-stage data processing pipeline for generative AI: document extraction, semantic chunking, dense vector embedding, and hybrid search indexing.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph DocumentSources ["Enterprise Document Repositories"]
        Confluence["Confluence Wikis"]
        Sharepoint["SharePoint PDFs & Office Docs"]
        GitRepo["Engineering Git Repositories"]
    end

    subgraph ExtractionTier ["1. Document Parsing & Cleansing"]
        DocExtractor["Unstructured.io / LlamaParse"]
        OCR["OCR & Table Extraction Engine"]
        DocExtractor --> OCR
        Confluence --> DocExtractor
        Sharepoint --> DocExtractor
        GitRepo --> DocExtractor
    end

    subgraph ChunkingTier ["2. Semantic Chunking & Enrichment"]
        Chunker["Context-Aware Chunking Engine<br/>(Chunk Size: 512 tokens, 10% Overlap)"]
        MetadataTagger["Metadata Extractor (Author, Bounded Context, ACLs)"]
        
        OCR --> Chunker
        Chunker --> MetadataTagger
    end

    subgraph EmbeddingTier ["3. Dense & Sparse Vectorization"]
        DenseEmbed["Dense Embedding Model<br/>(text-embedding-3-large / bge-large)"]
        SparseEmbed["Sparse BM25 Indexer (Keyword Search)"]

        MetadataTagger --> DenseEmbed
        MetadataTagger --> SparseEmbed
    end

    subgraph VectorDatabase ["4. Hybrid Vector Store & Retrieval"]
        VectorDB[("Vector DB (Pinecone / Milvus / pgvector)<br/>- Dense Cosine Vectors (1536 dim)<br/>- Sparse Lexical Index<br/>- Document Access Control Lists (ACLs)")]
        
        DenseEmbed -->|"Index Vectors"| VectorDB
        SparseEmbed -->|"Index Keywords"| VectorDB
    end

    subgraph RuntimeRAG ["5. Online Retrieval & Generation"]
        UserQuery["User Prompt Query"]
        HybridSearch["Reciprocal Rank Fusion (RRF)"]
        Reranker["Cross-Encoder Reranker (Cohere)"]
        LLM["Foundation Model (GPT-4o / Claude 3.5)"]

        UserQuery --> HybridSearch
        HybridSearch <-->|"Query Top-K Candidates"| VectorDB
        HybridSearch --> Reranker
        Reranker -->|"Top 5 Highly Relevant Chunks"| LLM
        LLM --> Answer["Grounded Answer with Citations"]
    end

    classDef src fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef pipe fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef vec fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;
    classDef rnt fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class Confluence,Sharepoint,GitRepo src;
    class DocExtractor,OCR,Chunker,MetadataTagger,DenseEmbed,SparseEmbed pipe;
    class VectorDB vec;
    class UserQuery,HybridSearch,Reranker,LLM,Answer rnt;
```

## PlantUML Specification

```plantuml
@startuml
package "Document Sources" {
  [PDFs & Wikis]
}
package "Ingestion Pipeline" {
  component "Parser & Table Extractor" as parse
  component "Semantic Chunker (512 tokens)" as chunk
  component "Embedding Model" as embed
}
package "Vector Store" {
  database "Vector DB (pgvector / Pinecone)" as vdb
}
package "Runtime Retrieval" {
  actor User
  component "Hybrid Search & Reranker" as search
  component "LLM Generation" as llm
}

[PDFs & Wikis] -> parse : Extract Text
parse -> chunk : Split into Semantically Meaningful Chunks
chunk -> embed : Generate Dense Float32 Vectors
embed -> vdb : Upsert Vector + ACL Metadata
User -> search : Query Text
search <-> vdb : Cosine Distance + Metadata Filter
search -> llm : Augment Prompt with Grounded Facts
llm -> User : Factually Grounded Response
@enduml
```

## Architectural Design Considerations

* **Hybrid Search Strategy**: Combine dense semantic embeddings (cosine similarity) with sparse keyword matching (BM25) via Reciprocal Rank Fusion to maximize recall.
* **Document-Level Security ACLs**: Embed user access group tags directly in vector metadata to enforce enterprise authorization at query time.
* **Cross-Encoder Reranking**: Run candidate chunks retrieved from the vector index through a secondary cross-encoder reranker model before constructing the LLM prompt.

## Related Documentation & Patterns

* [AI Security](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/ai-security.md)
* [Data Lakehouse](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/lakehouse.md)
* [Physical Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/physical-data-flow.md)
