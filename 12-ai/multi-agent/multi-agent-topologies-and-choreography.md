# Multi-Agent Topologies & Choreography

## 1. Multi-Agent Design Patterns

```mermaid
flowchart TD
    subgraph Pattern1 ["1. Centralized Supervisor Pattern"]
        Sup["Supervisor Agent"] --> WorkerA["Specialist: SQL Analyst"]
        Sup --> WorkerB["Specialist: Python Coder"]
        Sup --> WorkerC["Specialist: Report Writer"]
        WorkerA & WorkerB & WorkerC --> Sup
    end

    subgraph Pattern2 ["2. Hierarchical Team Pattern"]
        Executive["Executive Planner Agent"] --> Lead1["Research Lead"]
        Executive --> Lead2["Engineering Lead"]
        Lead1 --> Res1["Web Researcher"]
        Lead2 --> Code1["Backend Coder"]
    end

    subgraph Pattern3 ["3. Peer Choreography (Message Bus)"]
        AgentX["Agent X"] <-->|Shared Event Stream / Kafka| AgentY["Agent Y"]
    end
```

---

## 2. Invariant: Structured Communication Schemas
Agents in a multi-agent system must **never communicate via raw, unstructured natural language chat**. Inter-agent messages must be serialized into strict JSON Schemas (defining sender, recipient, task_id, status, and payload) to prevent circular misunderstandings and hallucinated conversational loops.
