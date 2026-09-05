# System & Data Uncoupling Patterns

Technical execution patterns for separating tangled enterprise data, identity, and network links during a carve-out.

---

## 1. Shared Database Carve-Out Pattern

```mermaid
flowchart LR
    SharedDB["Shared Corporate Database<br/>(Contains Parent & Divested Data)"] --> Filter["ETL Filter & Anonymization Engine"]
    Filter --> CleanDB["Carved-Out Standalone Database<br/>(Parent records expunged; buyer-specific schema)"]
    CleanDB --> BuyerCloud["Transfer to Buyer Cloud Environment"]
```

---

## 2. Identity & Access Separation Checklist
1. **Directory Clone**: Extract divested employee records from parent Entra ID / Okta into a clean, independent tenant.
2. **Network Perimeter Severing**: Terminate direct IPsec VPN and Transit Gateway connections between parent and divested offices.
3. **SaaS Seat License Transfer**: Carve out assigned software seats into separate commercial contracts with vendors.
