# C4 Dynamic Diagram

A **C4 Dynamic Diagram** illustrates runtime interactions, collaboration sequences, and data flows between containers or components for a specific business use case. It combines the structural clarity of a Container/Component diagram with the temporal ordering of a Sequence diagram.

```mermaid
flowchart LR
    Client["1. Investor submits $50k Buy Order
[Retail Client]"] -->|HTTPS| Gateway["2. Terminate TLS & Validate JWT
[API Gateway]"]
    Gateway -->|3. Route Buy Order (gRPC)| OrderSvc["4. Check Purchasing Power & Idempotency
[Order Execution Service]"]
    OrderSvc -->|5. Verify Margin Limit| RiskSvc["6. Assert Account Margin OK
[Risk Engine]"]
    OrderSvc -->|7. Persist Pending Order (ACID)| DB[("8. Write Pending Status
[PostgreSQL Order DB]")]
    OrderSvc -->|9. Dispatch FIX Order| Exchange["10. Execute Trade on Market
[External Exchange]"]
    OrderSvc -.->|11. Emit OrderPlaced Event| Kafka["12. Broadcast to Topic
[Kafka Event Mesh]"]
    Kafka -.->|13. Ingest Event| Notify["14. Dispatch Push Alert to Mobile
[Notification Service]"]
```
