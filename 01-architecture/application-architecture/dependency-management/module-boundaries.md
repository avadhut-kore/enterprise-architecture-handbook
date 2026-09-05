# Module Boundaries & Encapsulation

## 1. Encapsulation Mechanisms
Languages provide access modifiers to enforce module boundaries:
- **Java**: Package-private (default) classes and Java Platform Module System (`module-info.java`).
- **C# / .NET**: `internal` classes and assembly-level `InternalsVisibleTo` attributes.
- **TypeScript**: Package export maps (`package.json` `"exports": { ... }`).

---

## 2. Architectural Rule: Facades and Public Contracts
A module should expose only:
1. Public Interfaces (contracts).
2. Public DTOs (data carriers).
3. Public Events (notifications).

All implementations (aggregates, repositories, handlers) must remain internal.
