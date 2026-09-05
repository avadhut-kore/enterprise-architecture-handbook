# Idempotency & Transactional Safety in Tool Execution

## 1. The Duplicate Mutation Danger

Foundation models frequently retry tool calls if an intermediate response times out or if the model's reasoning loop backtracks. If a tool executes a state mutation (e.g., `charge_card`, `create_user`), retrying the call without an idempotency key will result in **duplicate credit card charges or orphaned database records**.

```mermaid
sequenceDiagram
    autonumber
    participant Agent as Agent Execution Runtime
    participant API as Payment Gateway API
    participant DB as Core Transaction Ledger

    Note over Agent: Agent generates deterministic Idempotency Key:<br/>`idempotency_key = sha256(session_id + goal_step_3)`
    Agent->>API: POST /v1/charges {amount: $50, key: "idem-98124"}
    Note over API: API processes charge; writes to DB;<br/>Network drops response!
    Agent->>Agent: Timeout after 5000ms! Retry tool call.
    Agent->>API: POST /v1/charges {amount: $50, key: "idem-98124"} (Retry)
    Note over API: API detects duplicate key "idem-98124";<br/>skips charge; returns cached HTTP 200
    API-->>Agent: HTTP 200 {status: "SUCCESS"}
```

---

## 2. Invariant: Deterministic Tool Idempotency Keys
The agent runtime must generate idempotency keys deterministically by hashing the `session_id`, `task_step_id`, and `tool_parameters`. Passing random UUIDs on retries destroys idempotency protections.
