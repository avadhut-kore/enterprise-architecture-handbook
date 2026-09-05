# Mermaid State Diagrams & Lifecycle Transitions

State diagrams capture state machines, distributed transaction sagas, and object lifecycles.

## Order Lifecycle Finite State Machine (FSM)

```mermaid
stateDiagram-v2
    [*] --> Created : Submit Order
    
    Created --> PaymentPending : Authorize Payment
    
    state PaymentProcessing {
        PaymentPending --> FraudCheck : Run ML Fraud Model
        FraudCheck --> ChargeSubmitted : Approved
        ChargeSubmitted --> PaymentSettled : Bank Confirmed
    }
    
    PaymentProcessing --> Cancelled : Fraud Detected / Card Declined
    PaymentSettled --> FulfillmentPending : Trigger Warehouse
    
    state Fulfillment {
        FulfillmentPending --> Picking : Allocating Stock
        Picking --> Packed : Box Sealed
        Packed --> Shipped : Carrier Picked Up
    }

    Shipped --> Delivered : Customer Signed
    Delivered --> [*]
    Cancelled --> [*]
```

## Architectural Guidelines
* **Use `stateDiagram-v2`**: Provides modern visual rendering and clean curved connectors.
* **Composite States**: Group related sub-states into parent states (e.g., `PaymentProcessing` or `Fulfillment`) to keep diagrams readable.
