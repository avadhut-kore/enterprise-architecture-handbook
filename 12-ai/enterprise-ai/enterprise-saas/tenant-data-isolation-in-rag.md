# Tenant Data Isolation in Shared Vector Databases

## 1. Enforcing Isolation at the Vector Engine Layer

```mermaid
flowchart LR
    Client["Tenant Request (JWT: tenant_id='corp_100')"] --> GW["AI Gateway"]
    GW --> AddFilter["Inject Mandatory Filter:\nmetadata.tenant_id == 'corp_100'"]
    AddFilter --> VecDB[("Shared Vector DB (Qdrant / Milvus)")]
    VecDB --> SafeResults["Results: Exclusively 'corp_100' vectors"]
```

### Invariant: Gateway-Enforced Filtering
The filter parameter must be injected by the authenticated server middleware; it is **never** accepted as an arbitrary parameter from client request payloads.
