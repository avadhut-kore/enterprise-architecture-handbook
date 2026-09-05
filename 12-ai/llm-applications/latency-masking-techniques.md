# Latency Masking & Perceived Performance Architecture

## 1. Managing User Perception during High-Latency Inference

When an agentic workflow or RAG pipeline takes $5\text{s} - 20\text{s}$ to retrieve documents, execute tools, and formulate an answer, a blank screen or static spinner causes user frustration and abandoned sessions.

Modern AI architecture incorporates **active perceptual latency masking**.

```mermaid
flowchart TD
    UserSubmit["User Submits Prompt"] --> UIUpdate["1. Optimistic Local Render of User Message (0ms)"]
    UIUpdate --> StageTicker["2. Stream Intermediate State Tickers via SSE:"]
    
    subgraph Tickers ["Progressive Step Tickers"]
        T1["'🔍 Searching internal knowledge base...' (200ms)"]
        T2["'📄 Found 3 relevant policy documents...' (600ms)"]
        T3["'⚙️ Calculating compliance score...' (1200ms)"]
    end

    StageTicker --> Tickers
    Tickers --> StreamFirst["3. Stream First Token of Final Answer (1500ms)"]
    StreamFirst --> FullText["4. High-Speed Markdown Token Rendering"]
```

---

## 2. Architectural Invariants
* **Never Block on Background Operations**: If an operation does not impact the immediate answer (e.g., logging to observability store, updating user profile analytics), execute it asynchronously in the background via detached worker threads or event queues.
* **Typing Speed Smoothing**: Buffer fast GPU token bursts (e.g., 80 tps) and release them to the UI at a smoothed human-readable pace (30–40 tps) to prevent visual flickering.
