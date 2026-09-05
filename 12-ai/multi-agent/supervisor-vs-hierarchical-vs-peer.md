# Supervisor vs. Hierarchical vs. Peer Multi-Agent Topologies

## 1. Architectural Trade-Off Analysis

| Topology | Control Flow | Debuggability | Token Overhead | Ideal Enterprise Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Centralized Supervisor** | Central router dispatches subtasks and aggregates results. | **High**: Single point of inspection for all state transitions. | Medium ($2\times - 3\times$ baseline). | Customer support escalation, triaged code review. |
| **Hierarchical Teams** | Multi-level tree; managers delegate to specialized subordinates. | Medium: High state complexity across sub-trees. | High ($4\times - 8\times$ baseline). | Large-scale automated software development, complex audit discovery. |
| **Peer Choreography** | Decentralized; agents publish/subscribe to shared message buses. | **Very Low**: High risk of emergence, infinite chatter, deadlocks. | Extremely High (unbounded). | **Avoid in enterprise production** unless backed by strict formal Petri nets. |
