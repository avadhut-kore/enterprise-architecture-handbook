# Mermaid Sequence Diagrams & Advanced Annotations

Sequence diagrams visually communicate dynamic inter-service communication over time.

## Enterprise Payment Sequence with Retry and Fallback

```mermaid
sequenceDiagram
    autonumber
    actor Customer as User (Browser)
    participant GW as API Gateway
    participant OrderSvc as Order Service
    participant PaySvc as Payment Service
    participant Stripe as Stripe Gateway API

    Customer->>GW: POST /orders/checkout
    GW->>OrderSvc: Forward Request (JWT Verified)
    OrderSvc->>PaySvc: Initiate Payment ($120.00)
    
    critical Charge External Provider
        PaySvc->>Stripe: POST /v1/charges
        Stripe-->>PaySvc: 200 OK (Charge ID: ch_9921)
    option Network Timeout (Retry 1)
        PaySvc->>Stripe: POST /v1/charges (Idempotency-Key)
        Stripe-->>PaySvc: 200 OK
    option Provider Down
        PaySvc-->>OrderSvc: Payment Failed (503 Service Unavailable)
        OrderSvc-->>GW: Order Queued in Pending Review
    end

    PaySvc-->>OrderSvc: Payment Confirmed
    OrderSvc-->>GW: Order Created (201 Created)
    GW-->>Customer: Render Order Confirmation
```

## Architectural Guidelines
* **Autonumbering**: Always use `autonumber` to make diagram steps clear and easy to reference during code and architecture reviews.
* **Control Blocks**: Use `critical`, `alt / else`, `loop`, and `par` blocks to capture non-happy-path real-world behavior.
