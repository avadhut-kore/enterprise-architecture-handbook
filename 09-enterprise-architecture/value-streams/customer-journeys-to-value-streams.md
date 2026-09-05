# Customer Journeys vs Value Streams

How front-office customer experience (CX) journeys map directly to foundational back-office enterprise value streams.

---

## 1. Journey-to-Stream Alignment

```mermaid
flowchart TD
    subgraph Front-Office Customer Experience (Journey)
        J1["Mobile UX: Browse Catalog"] --> J2["Mobile UX: 1-Click Checkout"]
        J2 --> J3["Push Notification: Shipment Tracked"]
        J3 --> J4["Doorstep: Package Received"]
    end
    subgraph Back-Office Enterprise Value Stream (Stream)
        V1["Stage 1: Order Validation"] --> V2["Stage 2: Payment Authorization & Settlement"]
        V2 --> V3["Stage 3: Warehouse Pick & Pack (WMS)"]
        V3 --> V4["Stage 4: Carrier Logistics Dispatch"]
    end
    J2 -.->|Triggers API Request| V1
    V2 -.->|Dispatches Kafka Event| J3
    V4 -.->|Updates Tracking State| J4
```

---

## 2. Architectural Takeaways
* Customer journeys change rapidly based on marketing tests, UI redesigns, and channel shifts.
* Enterprise value streams provide the enduring, stable transactional backbone.
* Use **API Gateways and Backend-For-Frontend (BFF)** layers to insulate the stable back-office value stream from volatile front-office customer journey experiments.
