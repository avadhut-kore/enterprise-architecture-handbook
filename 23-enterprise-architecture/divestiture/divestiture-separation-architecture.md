# Divestiture Separation Architecture

How Enterprise Architects plan and execute technical carve-outs without disrupting parent or divested business operations.

---

## 1. The Divestiture Asset Classification Matrix

```mermaid
graph TD
    Assets["Divestiture Scope: All Technology Assets"] --> Dedicated["1. Dedicated Assets<br/>(Used exclusively by divested unit)<br/><b>Action: Transfer ownership directly to buyer</b>"]
    Assets --> Shared["2. Shared Enterprise Assets<br/>(Shared ERP, HR, Network, Identity)<br/><b>Action: Carve out data, clone systems, or negotiate TSA</b>"]
    Assets --> Retained["3. Retained Parent Assets<br/>(Core intellectual property & parent systems)<br/><b>Action: Revoke all access for divested staff</b>"]
```
