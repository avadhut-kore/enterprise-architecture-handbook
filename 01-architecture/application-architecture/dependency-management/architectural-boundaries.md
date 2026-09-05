# Architectural Boundaries & Cross-Boundary Crossing

## 1. What Crosses a Boundary?

A boundary is crossed whenever an application thread transitions from one architectural layer or module into another.

```
+--------------------------+---------------------------------+---------------------------------+
| Boundary Crossing        | Permitted Data Types            | Prohibited Data Types           |
+--------------------------+---------------------------------+---------------------------------+
| Web API -> Application   | Primitive types, Command DTOs,  | HTTP Request context, Cookies,  |
|                          | Query DTOs                      | raw socket handles              |
+--------------------------+---------------------------------+---------------------------------+
| Application -> Domain    | Domain models, Value Objects,   | DTOs, Entity Framework Models,  |
|                          | IDs                             | SQL query strings               |
+--------------------------+---------------------------------+---------------------------------+
| Domain -> Infrastructure | Interfaces, Domain Events       | Concrete repository classes, DB |
|                          |                                 | connection objects              |
+--------------------------+---------------------------------+---------------------------------+
```
