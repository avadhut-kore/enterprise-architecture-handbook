# Architecture Prototyping and Spikes

The purpose of an architectural spike is not to write production code. It is to answer a specific, high-risk question with empirical data.

## 1. Spikes vs PoCs vs Tracer Bullets

| Technique | Primary Goal | Code Disposal | Typical Duration |
| :--- | :--- | :--- | :--- |
| **Spike** | Answer a single technical uncertainty (e.g., "Can Redis handle 50k writes/sec with persistence?"). | Discarded immediately. | 1-3 days |
| **Proof of Concept (PoC)**| Validate feasibility of a library or external vendor API integration. | Throwaway or reference. | 3-5 days |
| **Tracer Bullet** | End-to-end skeleton connecting UI, API, Queue, and DB with dummy logic. | Kept; flesh out logic. | 1-2 weeks |

## 2. Spike Governance Rules
1. **Define the Hypothesis Upfront**: e.g., *"We hypothesize that Cassandra will sustain 20,000 writes/sec on 3 nodes with sub-5ms latency."*
2. **Strict Timeboxing**: If an answer is not found within 3 days, the technology is deemed too complex or unstable for adoption.

## Related Modules
- [Benchmarking and Performance Profiling](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/benchmarking/benchmarking-and-performance-profiling.md)
- [Irreversible vs Reversible Decisions](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/decision-making/irreversible-vs-reversible-decisions.md)
