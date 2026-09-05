# Distributed Design Principle: Idempotency

## 1. Core Principle Definition

An operation is defined as **idempotent** if executing it multiple times with the exact same input produces the identical systemic state and returns the identical outcome as executing it exactly once:
$$f(f(x)) = f(x)$$

In distributed environments where networks are unreliable and message brokers provide "at-least-once" delivery, idempotency is the foundational requirement for building fault-tolerant services.

---

## 2. HTTP Method Idempotency Matrix

```
+------------+---------------+-----------------------------------------------+
| HTTP Method| Idempotent?   | Architectural Behavior                        |
+------------+---------------+-----------------------------------------------+
| GET        | Yes           | Safe read; produces no side effects           |
| PUT        | Yes           | Replaces resource with exact provided payload |
| DELETE     | Yes           | Resource deleted; subsequent calls return 404 |
| POST       | No (Default)  | Creates new resource on each execution        |
| PATCH      | Conditional   | Idempotent if absolute; non-idempotent if inc |
+------------+---------------+-----------------------------------------------+
```

---

## 3. Production Implementation: Idempotency Keys

For non-idempotent business operations (such as `POST /charges` or `POST /orders`):
1. The client generates a unique UUID `Idempotency-Key` and includes it in the HTTP header.
2. The server acquires a distributed lease on that key in Redis/DB using `SET key status NX EX 300`.
3. If the key already exists and has completed, the cached response is returned immediately.
4. If the key is currently being processed, subsequent duplicate requests wait or receive `HTTP 409 Conflict`.
