# Parent-Child & Hierarchical Chunking Architecture

## 1. The Granularity Conflict in Vector Search

Standard RAG forces a painful architectural compromise:
* Embed small chunks (128 tokens) $\to$ High vector search precision, but the LLM lacks surrounding context to construct a complete answer.
* Embed large chunks (1024 tokens) $\to$ Rich context for the LLM, but diluted embedding vectors cause search to return irrelevant chunks.

**Parent-Child Chunking** resolves this conflict by **decoupling the search unit from the generation unit**.

```mermaid
flowchart TD
    subgraph Storage ["Document Hierarchy in Storage"]
        ParentDoc["Parent Chunk (1,024 tokens / Complete Section)\nStored in Document Store (PostgreSQL / Mongo / S3)"]
        Child1["Child 1 (128 tokens)"]
        Child2["Child 2 (128 tokens)"]
        Child3["Child 3 (128 tokens)"]
        
        ParentDoc --- Child1 & Child2 & Child3
    end

    subgraph Search ["Vector Search Phase"]
        Query["User Query"] --> SearchIndex[("Vector DB (Embeds ONLY Child Chunks)")]
        SearchIndex -->|Best Match (Cosine 0.89)| Child2
    end

    subgraph ContextAssembly ["Generation Phase"]
        Child2 -->|Resolve parent_id reference| FetchParent["Fetch Complete Parent Chunk (1,024 tokens)"]
        FetchParent --> LLMPrompt["Inject Parent Chunk into LLM Context"]
        LLMPrompt --> LLM["Foundation Model Synthesis"]
    end
```

---

## 2. Invariant: Reference Integrity
The vector database stores child embeddings accompanied by a metadata pointer: `{"parent_id": "doc-891-parent-4"}`. The document store must guarantee sub-10ms key-value retrieval of the full parent chunk upon match.
