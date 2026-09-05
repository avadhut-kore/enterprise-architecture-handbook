# Debt Inventory & Enterprise Heatmaps

Cataloging architectural debt as a formal financial liability on the enterprise risk register.

---

## 1. Enterprise Debt Registry Schema

Every architectural debt item must be logged with:
```yaml
id: DEBT-FIN-042
title: Core Settlement Engine Running on Unsupported Oracle 11g
domain: Financial Services / Payment Processing
severity: Critical (Catastrophic Business Risk)
principal_cost_usd: 850000       # One-time cost to migrate to Aurora Postgres
annual_interest_usd: 420000      # Extended vendor support + manual DB tuning hours
blast_radius: Tier-0 Payment Settlement Ledger (Affects 12 downstream apps)
cve_vulnerabilities: 18 known unpatched CVEs
target_remediation_milestone: Q3 2027
```

---

## 2. The Debt Interest Calculation
$$\text{Annual Debt Interest} = \text{Extra Operational Support Costs} + \text{Extended Vendor Support Fees} + \text{Estimated Downtime Financial Liability}$$
When the annual interest exceeds 50% of the principal remediation cost, **modernization is financially mandatory**.
