# State Management & Conversation Session Architecture

## 1. The Context Window Expansion Trap

As a conversation progresses, naive applications append every user prompt and assistant response to the request payload. In a 20-turn conversation, passing the full uncompressed conversation history results in **quadratic token cost inflation and attention degradation ("lost in the middle")**.

```mermaid
flowchart TD
    NewMsg["Turn 21: User Question"] --> SessionStore[("Redis Session Store")]
    SessionStore --> FetchHist["Fetch Full Conversation History (Turns 1 - 20)"]
    
    FetchHist --> PruneStrategy{"Session Compression Strategy"}
    
    PruneStrategy -->|Sliding Window| Opt1["Keep Last N Turns (e.g., Last 4 Turns)\nDiscard Turns 1 - 16"]
    PruneStrategy -->|Summarization Buffer| Opt2["Compress Turns 1 - 16 into a 100-word Summary\nAppend Last 4 Raw Turns"]
    PruneStrategy -->|Semantic Memory Search| Opt3["Search Episodic Vector Store\nInject Only Semantically Relevant Past Turns"]
    
    Opt1 & Opt2 & Opt3 --> AssembledContext["Assembled Prompt within Context Budget"]
```

---

## 2. Architectural Session Store Topology
* **Fast In-Memory Layer (Redis Cluster)**: Stores active conversation threads with a 24-hour TTL. Sub-millisecond read/write latency ensures zero overhead on token streaming.
* **Cold Persistence Layer (PostgreSQL / DynamoDB)**: Asynchronously stores full unredacted conversation transcripts for auditing, compliance, and offline model evaluation.
