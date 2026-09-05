# Managing Technical Conflict

Technical disagreements are healthy and inevitable. When unmanaged, however, they degenerate into ideological factionalism and analysis paralysis.

## 1. Deconstructing Architectural "Religious Wars"

Most protracted technical disputes stem from hidden unstated assumptions or conflicting optimization goals:
- Engineer A optimizes for **Developer Velocity & Expressiveness** (proposes GraphQL, DynamoDB).
- Engineer B optimizes for **Data Integrity & Long-Term Query Flexibility** (proposes REST, Postgres ACID).

Neither is "wrong"; they are optimizing for different axes.

## 2. The Conflict Resolution Algorithm

```
Step 1: Uncover Hidden Objectives -> "What specific failure mode are you guarding against?"
                                  │
Step 2: Translate to Metrics      -> Define quantifiable thresholds (latency, p99, delivery date).
                                  │
Step 3: Define Timeboxed Spike    -> Give both approaches 3 days to test against real criteria.
                                  │
Step 4: Decision & ADR Sign-off   -> Lead architect decides; document reasoning in ADR.
                                  │
Step 5: Disagree and Commit       -> Execute without passive-aggressive sabotage.
```

## Related Modules
- [Consensus vs Ownership](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/decision-making/consensus-vs-ownership.md)
- [Architectural Leadership](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/leadership/architectural-leadership-and-influence.md)
