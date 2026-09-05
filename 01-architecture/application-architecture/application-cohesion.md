# Application Cohesion: Semantic Grouping

## 1. Cohesion Levels (From Worst to Best)

```
Cohesion Hierarchy:
[Worst]
  1. Coincidental: Random helper utilities (StringHelper, CommonUtils)
  2. Logical: Operations grouped by type, not domain (InputHandler)
  3. Temporal: Tasks grouped because they happen at startup (InitAll)
  4. Procedural: Steps of a script executed in sequence
  5. Communicational: Operates on the same data set
  6. Sequential: Output of one step is input to next (Pipe)
  7. Functional: Every element contributes to ONE well-defined task
[Best]
```

---

## 2. Architectural Antipattern: The "Common" or "Shared" Project
Creating a `MyCompany.Common` or `Shared` library is a primary cause of architectural decay:
- It becomes a dumping ground with high afferent coupling from all services.
- A minor change in `Common` forces recompilation and redeployment of the entire enterprise portfolio.
- **Rule**: Eliminate `Common`. Prefer duplicate code over premature shared abstractions.
