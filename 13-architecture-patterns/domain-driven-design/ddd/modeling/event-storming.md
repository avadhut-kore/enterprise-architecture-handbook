# DDD Modeling Practice: Event Storming: Rapid Domain Discovery

## 1. Purpose & Overview
A collaborative modeling method bringing domain experts and developers together to map business domains using orange domain event sticky notes.

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
