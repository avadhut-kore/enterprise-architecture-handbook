# DDD Modeling Practice: Domain Discovery Techniques

## 1. Purpose & Overview
Heuristics for interviewing domain stakeholders, analyzing business processes, and extracting hidden business invariants.

---

## 2. Modeling Workflow

```mermaid
flowchart LR
    DomainEvents[1. Identify Domain Events (Orange)] --> Triggers[2. Identify Commands & Triggers (Blue)]
    Triggers --> Aggregates[3. Identify Aggregates & Entities (Yellow)]
    Aggregates --> Contexts[4. Group into Bounded Contexts]
```

---

## 3. Practical Enterprise Guidelines
- Focus on business milestones, not database tables.
- Look for nouns that mean different things to different teams—this marks a boundary between Bounded Contexts.
