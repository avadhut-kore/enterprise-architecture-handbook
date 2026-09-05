# Vendor Lock-In & Exit Strategies

Architectural design patterns to prevent multi-million dollar vendor entrapment.

---

## 1. The 4 Layers of Vendor Lock-In

```mermaid
graph TD
    L1["1. Data Lock-in (Highest Risk)<br/>Proprietary binary storage formats, massive egress costs, unexportable history"]
    L2["2. Logic Lock-in<br/>Business rules hardcoded in vendor-proprietary scripting languages (e.g., Apex, ABAP)"]
    L3["3. Interface Lock-in<br/>Applications calling vendor-specific APIs directly without abstraction"]
    L4["4. Contractual Lock-in<br/>Multi-year auto-renewing commitments with punitive early termination fees"]
```

---

## 2. The Architectural Exit Pattern: The Vendor Façade
Never allow downstream applications to import vendor SDKs or call vendor APIs directly. Always wrap third-party vendors behind an enterprise **Anti-Corruption Layer / Adapter**:

```mermaid
flowchart LR
    App["Internal Enterprise Apps"] --> Adapter["Enterprise Payment Gateway Façade<br/>(Standard Enterprise REST API)"]
    Adapter -->|Translates to| Vendor1["Vendor A (Stripe)"]
    Adapter -.->|Can hot-swap to| Vendor2["Vendor B (Adyen)"]
```
