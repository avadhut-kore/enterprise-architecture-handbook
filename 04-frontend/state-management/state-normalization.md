# Frontend State: State Normalization & Relational Structures

## 1. Architectural Purpose & Problem Context
Normalizing nested API payloads (byId, allIds) to avoid stale references and duplicate records.

---

## 2. Structural Architecture & Data Flow

```mermaid
flowchart TD
    UserEvent[User Event] --> StateCheck{"Is this Server Data?"}
    StateCheck -->|Yes| ServerCache[TanStack Query / RTK Query]
    StateCheck -->|No| IsGlobal{"Is it shared across distant views?"}
    IsGlobal -->|Yes| GlobalStore[Zustand / SignalStore]
    IsGlobal -->|No| LocalState[useState / Local Signal]
```

---

## 3. Production Guidelines & Anti-Patterns
- **The Golden Rule**: Never duplicate server cache data into a client global store (Redux).
- Avoid impossible UI states (e.g., status flags without state machines) by using explicit status enums.
