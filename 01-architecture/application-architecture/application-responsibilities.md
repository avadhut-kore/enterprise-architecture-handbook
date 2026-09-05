# Application Responsibilities & Separation of Concerns

## 1. Core Architectural Responsibility Matrix

```
+--------------------------+---------------------------------+---------------------------------+
| Architectural Layer      | Primary Responsibilities        | Prohibited Responsibilities     |
+--------------------------+---------------------------------+---------------------------------+
| Presentation / API       | HTTP routing, JSON framing,     | Direct SQL queries,             |
|                          | token extraction, input schema  | financial math, transaction     |
|                          | validation, status codes        | management                      |
+--------------------------+---------------------------------+---------------------------------+
| Application / Use Case   | Orchestrating domain workflows, | HTTP requests, raw SQL, direct  |
|                          | transaction boundaries, security| hardware operations             |
|                          | checks, emitting events         |                                 |
+--------------------------+---------------------------------+---------------------------------+
| Domain Core              | Pure business logic, entity     | Network calls, file I/O, cloud  |
|                          | invariants, aggregate roots,    | SDKs, framework imports         |
|                          | domain events, value objects    |                                 |
+--------------------------+---------------------------------+---------------------------------+
| Infrastructure           | Database queries, ORM mapping,  | Domain invariant validation,    |
|                          | message broker publishing, third| business rule orchestration     |
|                          | party REST clients, file disks  |                                 |
+--------------------------+---------------------------------+---------------------------------+
```

---

## 2. Architectural Red Flags & Violations

- **Smart UI / Fat Controllers**: API controllers containing 500 lines of SQL and business calculation logic.
- **Anemic Domain Model**: Domain entities that are pure property bags (`get; set;`), while all business logic is scattered across random procedural service classes.
- **Leaky Infrastructure**: Domain classes importing `Microsoft.EntityFrameworkCore`, `org.hibernate`, or `boto3`.
