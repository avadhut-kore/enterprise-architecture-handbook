# Payment Failure Modes, Retries, and Fallbacks

## 1. Card Decline Classifications

| Decline Category | Error Codes | Retry Permitted? | Recommended Action |
| :--- | :--- | :--- | :--- |
| **Hard Decline** | Stolen Card (04), Fraud Suspect (07), Invalid Acct (14) | **NO** | Block customer, prompt for new card |
| **Soft Decline** | Insufficient Funds (51), Exceeded Limit (61) | Conditionally | Notify customer, retry once after 24h |
| **Systemic Failure**| Issuer Timeout (91), System Error (96), Network Glitch | **YES** | Immediate retry with exponential backoff / alternate acquirer |

## 2. Stand-in Processing (STIP) and Fallback Protocols
When card networks or issuing banks suffer systemic outages, payment gateways trigger **STIP mode**:
- Transactions below floor limits (e.g., $50) are tentatively authorized.
- The acquirer assumes short-term credit risk, reconciling captured authorizations once the issuer returns online.
