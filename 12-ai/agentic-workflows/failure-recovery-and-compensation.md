# Failure Recovery & Compensation Patterns in AI Pipelines

## 1. The Saga Pattern for AI Workflows

Because AI outputs can fail validation halfway through a multi-step sequence, systems must implement the **Saga Pattern**: every forward action must have an associated **Compensating Transaction** to roll back partial changes.

```mermaid
flowchart TD
    subgraph ForwardPath ["Forward Actions"]
        F1["1. Create Draft Booking in CRM"] --> F2["2. Reserve Airline Ticket"]
        F2 --> F3["3. AI Generates Customer Itinerary Email"]
        F3 --> F4["4. Email Output Fails Safety / Policy Check!"]
    end

    subgraph CompensationPath ["Compensating Reversals"]
        F4 -.->|Trigger Saga Compensation| C2["Cancel Reserved Airline Ticket"]
        C2 --> C1["Mark CRM Booking as 'CANCELLED'"]
        C1 --> Alert["Notify Human Agent of Pipeline Abort"]
    end
```

---

## 2. Invariant: Idempotency of Compensations
All compensating actions must be strictly idempotent. If the compensation worker retries canceling the ticket due to a network timeout, the downstream airline API must return HTTP 200 without throwing duplicate cancellation errors.
