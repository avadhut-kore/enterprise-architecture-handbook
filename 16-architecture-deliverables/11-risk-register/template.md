# Architecture Risk Register: [SYSTEM / INITIATIVE NAME]

---
**Metadata**:
```yaml
register_id: "RISK-REG-[PROJECT-ID]"
title: "Architecture Risk Register — [System Name]"
version: "1.0.0"
status: "Active" # Active | Closed | Archived
risk_manager: "[Lead Architect / Risk Owner Name <email>]"
last_audit_date: "YYYY-MM-DD"
next_audit_date: "YYYY-MM-DD"
```
---

## 1. Risk Scoring Methodology
Overall Risk Exposure = **Likelihood (1–5)** $	imes$ **Impact (1–5)**.
* **1–4**: Low (Accept / Monitor)
* **5–9**: Medium (Track with standard mitigation)
* **10–15**: High (Escalate to ARB; proactive mitigation required)
* **16–25**: Critical (Executive visibility; blocks production deployment)

## 2. Risk Register Ledger
| Risk ID | Category | Risk Description | Root Cause | Impact | Likelihood (1-5) | Severity (1-5) | Exposure Score | Assigned Owner | Mitigation Strategy | Contingency Plan | Status | Due Date | Residual Risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **RSK-001** | Architecture | Cross-region consensus latency degrades checkout UX | Multi-region Raft consensus roundtrips | Checkout p99 exceeds 500ms SLO | 4 | 4 | **16 (Critical)** | Lead Architect | Implement geo-partitioned follower reads | Fall back to asynchronous checkout queue | In Progress | YYYY-MM-DD | 6 (Medium) |
| **RSK-002** | Vendor | Single cloud provider dependency (AWS) | Deep reliance on AWS Aurora and KMS | Potential egress fee spike or outage | 2 | 4 | **8 (Medium)** | Cloud Architect | Interface abstractions at repository boundaries | Disaster recovery secondary warm standby | Accepted | YYYY-MM-DD | 8 (Medium) |
| **RSK-003** | Data | Dual-write inconsistency during order event dispatch | Non-atomic write to DB and Kafka | Orders lost or balance mismatch | 3 | 5 | **15 (High)** | Data Architect | Implement Transactional Outbox Pattern | Nightly reconciliation batch job | Mitigated | YYYY-MM-DD | 3 (Low) |
