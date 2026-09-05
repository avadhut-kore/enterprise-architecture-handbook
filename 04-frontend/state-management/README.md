# Frontend State Management Architecture

State management is the primary driver of frontend complexity. In modern web architectures, conflating local UI state, remote server cache, and global application state results in desynchronization, race conditions, and unmaintainable codebases.

This directory categorizes state into distinct architectural layers and provides pattern blueprints.

---

## State Management Catalog
- [Local Component State](local-state.md)
- [Server State & Caching](server-state.md)
- [Global Application State](global-state.md)
- [Derived State & Memoization](derived-state.md)
- [State Normalization](state-normalization.md)
- [Finite State Machines (XState)](state-machines.md)
- [Event-Driven UI State](event-driven-ui.md)
- [State Persistence](state-persistence.md)
- [Optimistic UI Updates](optimistic-updates.md)
- [Offline State Management](offline-state.md)
- [State Consistency & Race Conditions](state-consistency.md)
- [State Management Architectural Comparison](state-management-comparison.md)
