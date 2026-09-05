# REST API Design Standards

## 1. Resource Modeling & URI Conventions
* Use plural nouns for resource collections: `/customers`, `/orders`, `/shipments`.
* Use sub-resources for hierarchy: `/customers/{id}/payment-methods`.
* Never use verbs in URIs (Bad: `/createOrder`; Good: `POST /orders`).

## 2. HTTP Method Semantics
| Verb | CRUD | Safe | Idempotent | Success Status |
|---|---|---|---|---|
| `GET` | Read | Yes | Yes | `200 OK` |
| `POST` | Create | No | No (unless keyed) | `201 Created` (`Location` header required) |
| `PUT` | Replace | No | Yes | `200 OK` / `204 No Content` |
| `PATCH` | Modify | No | No | `200 OK` |
| `DELETE` | Remove | No | Yes | `204 No Content` / `200 OK` |
