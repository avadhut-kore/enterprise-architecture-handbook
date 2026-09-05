# Episodic & Semantic User Memory Architecture

## 1. Extracting Durable Facts from Conversations

To provide continuous personalization across sessions without passing full historical transcripts, the system uses an **Asynchronous Memory Extractor Worker**:

```mermaid
flowchart LR
    Session["Completed Conversation Session"] --> Worker["Async Memory Extraction Worker (Small SLM)"]
    
    Worker --> Extractor{"Extract Durable Entities"}
    Extractor -->|User Fact| FactDB[("Semantic Memory Table\n(Key-Value: user_id -> facts)")]
    Extractor -->|Episode Summary| VectorDB[("Episodic Vector Store\n(Embeddings of past interactions)")]

    FactDB --> ExampleFact["'User prefers AWS over Azure'\n'User role: Enterprise Architect'"]
    VectorDB --> ExampleEpisode["'Discussed multi-region failover on 2025-03-12'"]
```

---

## 2. Invariant: User Transparency & Editing
Enterprise systems must provide an administrative UI allowing users to view, edit, and delete their stored semantic memories. Storing secret, invisible behavioral dossiers violates consumer trust and privacy regulations.
