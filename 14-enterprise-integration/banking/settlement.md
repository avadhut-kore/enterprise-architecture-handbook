# Interbank Settlement Integration (Gross vs. Net)

## 1. Settlement Models and Liquidity Management
In banking integration, settlement represents the irrevocable transfer of funds between financial institutions across central bank accounts.

| Parameter | Real-Time Gross Settlement (RTGS) | Deferred Net Settlement (DNS) |
| :--- | :--- | :--- |
| **Mechanics** | Each payment settled individually in real-time | Batched transactions netted periodically |
| **Examples** | Fedwire, TARGET2, CHAPS, RTGS Systems | ACH (NACHA), Bacs, SEPA Core |
| **Counterparty Risk** | Zero (Immediate settlement finality) | Present until end-of-cycle netting completes |
| **Liquidity Demand** | High (Requires large central bank intraday reserves) | Low (Only net difference requires liquidity) |
| **Message Protocol** | ISO 20022 `pacs.009` / `pacs.008` | Batch EDI / ISO 20022 bulk clearing |

## 2. Central Bank Integration Topology
Core banking gateways connect to central banks via dedicated private extranets (e.g., SWIFT Alliance Gateway, FedLine Direct) utilizing hardware VPNs and hardware-based client certificates.
