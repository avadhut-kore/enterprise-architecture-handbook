# Logical Data Flow Diagram (DFD Level 1)

Domain-level logical flow representing business data transformation, validation gates, and domain boundaries without coupling to specific hardware or infrastructure vendors.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph ExternalEntities ["External Actors"]
        Customer["Customer (Web/Mobile)"]
        PaymentGateway["External Payment Provider"]
    end

    subgraph OrderDomain ["Order Management Bounded Context"]
        P1["1.0 Capture & Validate Order"]
        P2["2.0 Calculate Taxes & Discounts"]
        P3["3.0 Authorize Payment Transaction"]
        P4["4.0 Emit Order Confirmed Event"]

        D1[("D1: Pending Orders")]
        D2[("D2: Customer Profiles")]
        D3[("D3: Product Catalog")]
    end

    subgraph FulfillmentDomain ["Fulfillment Context"]
        P5["5.0 Reserve Warehouse Inventory"]
        D4[("D4: Inventory Store")]
    end

    Customer -->|"Order Submission Payload"| P1
    D2 -->|"Customer Tier & Address"| P2
    D3 -->|"Item Price & Availability"| P1
    P1 -->|"Validated Order"| P2
    P2 -->|"Final Payable Amount"| P3
    P3 <-->|"Payment Auth Token"| PaymentGateway
    P3 -->|"Settled Payment Record"| D1
    P3 -->|"Trigger Fulfillment"| P4
    P4 -->|"Order Placed Event"| P5
    P5 <-->|"Lock Stock"| D4

    classDef domain fill:#f3e5f5,stroke:#4a148c,stroke-width:2px;
    classDef ext fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    class OrderDomain,FulfillmentDomain domain;
    class Customer,PaymentGateway ext;
```

## PlantUML Specification

```plantuml
@startuml
actor Customer
actor "Payment Gateway" as PG
database "Customer Profiles" as D2
database "Product Catalog" as D3
database "Pending Orders" as D1
database "Inventory Store" as D4

package "Order Context" {
  component "1.0 Validate Order" as P1
  component "2.0 Calculate Taxes" as P2
  component "3.0 Authorize Payment" as P3
  component "4.0 Emit Event" as P4
}

Customer -> P1 : Submit Order
D3 -> P1 : Product Pricing
D2 -> P2 : Tax Exemption Rules
P1 -> P2 : Valid Order
P2 -> P3 : Total Due
P3 <-> PG : Tokenized Auth
P3 -> D1 : Record Order
P3 -> P4 : Confirm
P4 -> D4 : Reserve Stock
@enduml
```

## Architectural Design Considerations

* **Technology Agnosticism**: Logical DFDs depict *what* data transformations take place rather than *how* or *where* (e.g., whether a datastore is Postgres or Cassandra).
* **Data Store Boundaries**: Data stores must be scoped to bounded contexts; no direct cross-context database queries without explicit API or event interfaces.
* **Idempotency Guarantees**: Define logical idempotency keys at entry process nodes to reject duplicate business submissions.

## Related Documentation & Patterns

* [Physical Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/physical-data-flow.md)
* [Event-Driven Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/event-driven.md)
* [Sequence: Order Processing](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/sequence/order-processing.md)
