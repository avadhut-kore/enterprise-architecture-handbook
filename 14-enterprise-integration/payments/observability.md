# Payment Observability, Metrics, and Alerting

## 1. Critical Operational Metrics (Payment Golden Signals)
1. **Authorization Approval Rate**:
   $$	ext{Approval Rate} = rac{	ext{Successful Authorizations}}{	ext{Total Authorization Requests}} 	imes 100$$
   - Baseline: 88% - 94%. Alert P1 if falls below 82% over a 5-minute rolling window.
2. **Processor P95 Latency**: Alert if payment processor round-trip latency exceeds 1500ms.
3. **Refund / Chargeback Velocity**: Track volume of chargebacks per BIN (Bank Identification Number) to detect card testing attacks.
4. **Reconciliation Break Count**: Number of un-reconciled transactions aging over 24 hours.
