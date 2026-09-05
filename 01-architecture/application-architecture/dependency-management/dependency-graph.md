# Dependency Graphs & Directed Acyclic Graphs (DAG)

## 1. The Acyclic Dependencies Principle (ADP)

> **The dependency structure between packages or components must be a Directed Acyclic Graph (DAG); there must be no cycles.**

```
Valid DAG:
Module A ──► Module B ──► Module C
     │                       ▲
     └───────────────────────┘

Invalid Cycle (Tightly Coupled):
Module A ──► Module B ──► Module C
     ▲                       │
     └───────────────────────┘
```

When cycles exist:
- Modules A, B, and C can no longer be built, tested, or released independently.
- They become a single, de facto distributed or in-process monolith.
