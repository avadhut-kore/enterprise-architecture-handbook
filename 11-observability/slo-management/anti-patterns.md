# Enterprise SLO Anti-Patterns Catalog

## 1. Executive Summary
This document catalogs 12 widespread enterprise anti-patterns in Service Level Indicator design, SLO target setting, and error budget governance.

---

## 2. The 12 SLO Anti-Patterns

### 1. The 100% Availability Delusion
* **Problem**: Setting an SLO target of 100%.
* **Why It Happens**: Executives believing that admitting any downtime is unprofessional.
* **Impact**: Release velocity grinds to an absolute halt; infrastructure costs balloon by $50\times$; the first 5-second cloud network blip permanently breaches the SLO.
* **Remediation**: Educate stakeholders that 100% is mathematically impossible on distributed cloud infrastructure.

### 2. The Unenforced Error Budget (Paper Tiger SLO)
* **Problem**: A service exhausts 300% of its error budget, yet product managers continue shipping new features without consequence.
* **Why It Happens**: Lack of executive backing for the Error Budget Policy.
* **Impact**: SRE team loses credibility; system reliability degrades uncontrollably until a catastrophic public outage occurs.
* **Remediation**: Enforce automated CI/CD deployment gates backed by VP-level signed contracts.

### 3. Metric Proliferation (The 50-SLO Service)
* **Problem**: Defining 50 individual SLOs for a single microservice (e.g., separate SLO for every database query and internal helper method).
* **Why It Happens**: Confusing internal telemetry metrics with user-facing objectives.
* **Impact**: Total administrative paralysis; budget calculations become meaningless.
* **Remediation**: Limit each tier-1 service to **2 to 3 canonical SLIs** (Availability, Latency, and optional Freshness).

### 4. Setting SLOs Tighter Than Upstream Cloud Providers
* **Problem**: Guaranteeing 99.99% availability for an application hosted on AWS EC2 single-AZ instances (which have a 99.5% SLA).
* **Why It Happens**: Setting targets based on wishful thinking rather than architectural math.
* **Impact**: Inevitable failure whenever the underlying cloud provider experiences nominal maintenance.
* **Remediation**: Follow the Downstream Dependency Ceiling Rule: $\text{SLO}_{\text{service}} \le \prod \text{SLO}_{\text{dependencies}}$.

### 5. Vanity SLOs (Setting Targets Too Low)
* **Problem**: Setting an SLO of 95% for a system that naturally operates at 99.9%, simply to guarantee the team never runs out of budget.
* **Why It Happens**: Squads gaming the system to avoid release freezes.
* **Impact**: Destroys the value of the error budget as a meaningful signal of customer dissatisfaction.
* **Remediation**: Align SLOs directly with measurable customer happiness thresholds.

### 6. Averaging Percentages Across Time or Clusters
* **Problem**: Calculating an SLI by averaging daily percentages: `avg(daily_availability_percentages)`.
* **Why It Happens**: Basic mathematical ignorance of weighted averages.
* **Impact**: A 10-minute outage at 3:00 AM (10 requests) is given the same mathematical weight as a 10-minute outage during Black Friday (1,000,000 requests).
* **Remediation**: Always sum total good events and divide by total events over the entire 30-day window.

### 7. The Calendar Month Reset Anti-Pattern
* **Problem**: Resetting error budgets to 100% on the 1st of every month.
* **Why It Happens**: Mimicking monthly accounting cycles.
* **Impact**: Creates perverse behavior: teams hoard deployments until the 1st, or deploy recklessly on the 2nd.
* **Remediation**: Use a continuous **Rolling 30-Day (720-Hour)** window.

### 8. Paging Directly on SLO Breaches
* **Problem**: Configuring an alert to page when cumulative monthly availability drops below 99.9%.
* **Why It Happens**: Confusing SLO reporting with alerting.
* **Impact**: By the time the alert fires, the monthly budget is already 100% dead!
* **Remediation**: Alert on **Multi-Window Multi-Burn-Rate** (consuming budget too fast), not on the final breach.

### 9. Measuring SLIs Behind Internal CDNs or Synthetic Probes Only
* **Problem**: Calculating availability based solely on an external Pingdom check hitting `/healthz` every 60 seconds.
* **Why It Happens**: Easy to set up without instrumenting application code.
* **Impact**: The synthetic probe returns 200 OK while 90% of real users are getting 500 Internal Server Errors on checkout!
* **Remediation**: Measure SLIs directly from real user traffic at the edge or within application controllers.

### 10. Counting Client 4xx Errors Against the Service
* **Problem**: Including HTTP 401 Unauthorized or HTTP 404 Not Found in the total error count of an availability SLI.
* **Why It Happens**: Naive query filtering: `status != 200`.
* **Impact**: Invalid client requests or security scanners drain the team's error budget, halting legitimate feature deployments.
* **Remediation**: Filter out 4xx errors; count only server-side failures (HTTP 5xx).

### 11. Excluding Major Outages as "Force Majeure"
* **Problem**: Manually wiping out a 4-hour outage from the SLO calculation because "it wasn't our fault, the cloud provider had an issue."
* **Why It Happens**: Fear of organizational retribution for exhausted budgets.
* **Impact**: Conceals architectural single-points-of-failure; prevents investment in multi-region resilience.
* **Remediation**: All user-impacting downtime counts against the budget, regardless of cause.

### 12. Lack of SLO Visibility for Product Managers
* **Problem**: SLO metrics buried in obscure Prometheus consoles that only SREs have access to.
* **Why It Happens**: Treating SLOs as purely technical operations tools.
* **Impact**: Product managers have no awareness of remaining budget and cannot make informed feature roadmap trade-offs.
* **Remediation**: Publish high-level SLO and Error Budget status directly into Jira, Slack, and executive executive dashboards.
