# Application Layering Strategies

## 1. Strict Layering vs Relaxed Layering

```
Strict Layering (Closed Layers):
Layer N ──► Layer N-1 ──► Layer N-2 (Every layer can ONLY call immediately lower layer)

Relaxed Layering (Open Layers):
Layer N ──┬──► Layer N-1
          └──► Layer N-2 (Layer N can bypass N-1 for performance or simplicity)
```

---

## 2. The Architectural Dilemma: CQRS in Layered Systems

In traditional strict 3-tier layering:
- A simple read query (`SELECT id, name FROM users WHERE id = ?`) must pass:
  `Controller → UserService → UserRepository → DbContext`.
- For read-heavy queries, this generates massive object-mapping boilerplate (Entities $\rightarrow$ Domain Models $\rightarrow$ ViewModels) with zero business validation value.

### Architectural Recommendation:
Adopt **CQRS (Command Query Responsibility Segregation)**:
- **Write Path (Commands)**: Enforce strict layering and domain aggregate encapsulation to protect business invariants.
- **Read Path (Queries)**: Allow relaxed layering where the API directly invokes an optimized read model or Dapper/SQL projection, bypassing the domain layer completely.
