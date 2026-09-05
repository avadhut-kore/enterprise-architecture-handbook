# SLO Architecture & Governance Checklist

## 1. Executive Summary
This 25-point checklist provides engineering squads, Product Managers, and Architecture Review Boards (ARBs) with an objective verification rubric for designing, implementing, and enforcing Service Level Objectives and Error Budgets.

---

## 2. The 25-Point Checklist

### Section 1: SLI Design & Measurement
- [ ] **01.** SLIs are formulated as the ratio: $\sum \text{Good Events} / \sum \text{Total Valid Events}$.
- [ ] **02.** Request-based SLIs distinguish server errors (HTTP 5xx) from client errors (HTTP 4xx).
- [ ] **03.** Latency SLIs evaluate percentile thresholds (e.g., duration $\le 500\text{ms}$) on valid requests.
- [ ] **04.** SLIs are derived from real user traffic, not solely synthetic ping checks.
- [ ] **05.** Asynchronous processing pipelines maintain Freshness and Queue Lag SLIs.
- [ ] **06.** Mathematical calculations use rolling 30-day windows (720 hours) rather than calendar months.

### Section 2: Realistic Target Setting
- [ ] **07.** Target SLOs reflect user happiness thresholds rather than arbitrary round numbers.
- [ ] **08.** The 100% availability delusion is rejected across all engineering and product leadership.
- [ ] **09.** The Downstream Dependency Ceiling Rule is verified: service SLO does not exceed dependent systems.
- [ ] **10.** Total number of SLOs per tier-1 service is strictly bounded ($< 3$ canonical objectives).
- [ ] **11.** Allowed downtime budgets are understood and documented across the organization.

### Section 3: SLA vs SLO Safety Buffers
- [ ] **12.** External legal SLAs are backed by internal SLOs that are at least $3\times$ to $5\times$ stricter.
- [ ] **13.** An adequate Buffer Zone exists between the internal freeze line and legal contractual penalty lines.
- [ ] **14.** Customer contractual penalty clauses and rebate tiers are documented and aligned with finance.

### Section 4: Error Budget Governance & Policy
- [ ] **15.** A formal Error Budget Policy is signed by the VP of Product, Head of Engineering, and Lead SRE.
- [ ] **16.** The policy defines unambiguous actions for Green ($> 20\%$), Yellow ($0-20\%$), and Red ($\le 0\%$) states.
- [ ] **17.** Error budget exhaustion automatically triggers software deployment release freezes.
- [ ] **18.** Sprint planning pivots 100% of engineering capacity to reliability debt when the budget is exhausted.
- [ ] **19.** An executive break-glass procedure exists requiring written co-signatures from the CTO and CPO.

### Section 5: Tooling & Visibility
- [ ] **20.** SLO burn rates are monitored using Google SRE Multi-Window Multi-Burn-Rate alerting rules.
- [ ] **21.** Real-time Error Budget burn-down gauges are visible on Tier-0 and Tier-1 operational dashboards.
- [ ] **22.** Automated Slack/Jira notifications alert product squads when error budget drops below 50% and 20%.
- [ ] **23.** CI/CD deployment pipelines query the SLO engine to gate risky production releases.
- [ ] **24.** Post-mortem reviews evaluate error budget consumption and update targets if necessary.
- [ ] **25.** Quarterly SLO review audits ensure that targets remain calibrated with evolving business needs.
