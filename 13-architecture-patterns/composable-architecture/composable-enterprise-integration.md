# Composable Enterprise Integration Patterns

## 1. Composition Topologies

Connecting multiple autonomous PBCs requires an integration fabric that avoids creating a centralized monolithic bottleneck:

```mermaid
flowchart TD
    Client["Client Experience Application"] --> Gateway["API Gateway / GraphQL Federation"]
    
    Gateway --> PBC1["Payments PBC"]
    Gateway --> PBC2["Inventory PBC"]
    Gateway --> PBC3["AI Recommendations PBC"]
    
    PBC1 -.->|Publish Event: 'payment.completed'| Bus[("Enterprise Event Mesh (Kafka)")]
    Bus -.->|Subscribe| PBC2
```
