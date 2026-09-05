# Distributed Transaction Saga: Orchestration with Compensating Rollback

Demonstrates how an **Orchestrator-driven Saga** handles failures by executing compensating transactions to restore system consistency.

```mermaid
sequenceDiagram
    autonumber
    actor Customer as Customer
    participant Orchestrator as Order Saga Orchestrator
    participant OrderSvc as Order Service
    participant PaymentSvc as Payment Service
    participant InventorySvc as Inventory Service
    participant ShippingSvc as Shipping Service

    Customer->>Orchestrator: PlaceOrder(Items, PaymentMethod, Address)
    activate Orchestrator
    
    Note over Orchestrator: Step 1: Create Pending Order
    Orchestrator->>OrderSvc: CreateOrder(PENDING)
    OrderSvc-->>Orchestrator: Order Created (ID: ord_101)

    Note over Orchestrator: Step 2: Authorize Payment
    Orchestrator->>PaymentSvc: ProcessPayment(ord_101, $200.00)
    PaymentSvc-->>Orchestrator: Payment Approved (Txn: txn_555)

    Note over Orchestrator: Step 3: Reserve Inventory
    Orchestrator->>InventorySvc: ReserveStock(SKU_88, Qty: 2)
    InventorySvc-->>Orchestrator: Stock Reserved (Hold: hold_333)

    Note over Orchestrator: Step 4: Schedule Shipping (SIMULATED FAILURE)
    Orchestrator->>ShippingSvc: CreateShipment(ord_101, Address)
    activate ShippingSvc
    ShippingSvc-->>Orchestrator: 503 SERVICE UNAVAILABLE (Delivery Address Invalid)
    deactivate ShippingSvc

    Note over Orchestrator: SAGA COMPENSATION INITIATED (Reverse Actions)
    Orchestrator->>InventorySvc: ReleaseStock(Hold: hold_333)
    InventorySvc-->>Orchestrator: Stock Released OK

    Orchestrator->>PaymentSvc: RefundPayment(Txn: txn_555, Reason: "Shipping Failed")
    PaymentSvc-->>Orchestrator: Refund Processed OK

    Orchestrator->>OrderSvc: UpdateOrderStatus(ord_101, CANCELLED)
    OrderSvc-->>Orchestrator: Order Cancelled OK

    Orchestrator-->>Customer: Order Failed: Shipping Destination Not Serviceable (Funds Refunded)
    deactivate Orchestrator
```
