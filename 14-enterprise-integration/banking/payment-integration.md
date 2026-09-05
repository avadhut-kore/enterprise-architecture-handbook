# Payment Rails Integration: FedNow, RTP, SEPA, SWIFT

## 1. Modern vs. Legacy Payment Rail Characteristics

| Rail | Settlement Speed | Message Standard | Operating Hours | Irrevocability |
| :--- | :--- | :--- | :--- | :--- |
| **FedNow (US)** | Real-Time ($< 5	ext{s}$) | ISO 20022 (`pacs.008`) | 24x7x365 | Immediate |
| **RTP (The Clearing House)**| Real-Time ($< 5	ext{s}$) | ISO 20022 (`pacs.008`) | 24x7x365 | Immediate |
| **SEPA Instant (EU)** | Real-Time ($< 10	ext{s}$) | ISO 20022 (`pacs.008`) | 24x7x365 | Immediate |
| **ACH / NACHA (US)** | Same-day / Multi-day | Fixed-width NACHA record | Business days only | Reversible (60-day window) |
| **SWIFT Cross-Border** | Minutes to Days | ISO 20022 (CBPR+) / MT | Business days | Conditional |

## 2. Real-Time Ingress Rail Gateway Architecture
See [payments/payment-architecture.md](../payments/payment-architecture.md) for full orchestration details.
