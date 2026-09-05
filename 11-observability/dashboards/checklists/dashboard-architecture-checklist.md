# Dashboard Architecture & Usability Checklist

## 1. Executive Summary
This 25-point checklist provides engineering squads, UI/UX designers, and Architecture Review Boards (ARBs) with an objective verification rubric for operational dashboard design, performance, and governance.

---

## 2. The 25-Point Checklist

### Section 1: Visual Hierarchy & Cognitive Ergonomics
- [ ] **01.** The 5-Second Rule is satisfied: overall system health is immediately identifiable within 5 seconds of opening.
- [ ] **02.** Layout follows the Inverted Pyramid: summary status at top, symptoms (RED) in middle, causes (USE) below.
- [ ] **03.** The total number of panels on Tier-1 dashboards is bounded ($< 12$ to $15$ panels).
- [ ] **04.** Semantic colors are strictly enforced: Red is reserved exclusively for errors and SLO breaches.
- [ ] **05.** Percentage and count bar/area charts are anchored at zero baseline; misleading truncations are eliminated.
- [ ] **06.** Dashboard explicitly displays a prominent, clickable link to the service's operational runbook.
- [ ] **07.** All times and timestamps are configured to display in UTC.

### Section 2: Audience & Tier Alignment
- [ ] **08.** Dashboard is categorized into the 4-tier hierarchy (Tier 0 Business, Tier 1 RED, Tier 2 Subsystem, Tier 3 Host).
- [ ] **09.** Tier-1 dashboards focus exclusively on user-facing symptoms and SLO error budget burn rates.
- [ ] **10.** Tier-2 drill-down links are embedded within Tier-1 panels to enable intuitive 1-click navigation.
- [ ] **11.** Dashboards are organized into squad-specific Grafana folders with appropriate RBAC permissions.

### Section 3: Query Performance & Templating
- [ ] **12.** Hardcoded pods, hostnames, or cluster strings are replaced with dynamic Grafana template variables.
- [ ] **13.** Expensive percentile queries (`histogram_quantile`) use pre-computed Prometheus Recording Rules.
- [ ] **14.** Dashboard panels load and render completely within $< 2$ seconds over a standard 1-hour time window.
- [ ] **15.** Query time ranges use relative offsets (`now-1h`, `now-6h`) with standardized bucket steps.
- [ ] **16.** All panels specify explicit unit definitions (seconds, bytes, percent, QPS); unlabelled axes are eliminated.

### Section 4: Data Integration & Deep Linking
- [ ] **17.** Prometheus Exemplars are enabled, allowing 1-click navigation from metric spikes to distributed traces.
- [ ] **18.** Embedded log panels filter automatically based on the active time window and template variables.
- [ ] **19.** Deployment annotations are visible on time-series graphs, correlating releases with metric shifts.

### Section 5: Governance & Dashboard-as-Code
- [ ] **20.** Dashboards are managed declaratively via Dashboard-as-Code (Jsonnet / Terraform / Kubernetes CRD).
- [ ] **21.** Production dashboards are marked as "Read-Only / Non-Editable" in the Grafana UI to prevent ad-hoc mutations.
- [ ] **22.** Dashboards are version-controlled in Git and reviewed through pull requests with automated linters.
- [ ] **23.** Orphaned or unviewed dashboards are automatically flagged and pruned after 90 days of inactivity.
- [ ] **24.** High-frequency auto-refresh ($< 30\text{s}$) is disabled on unattended or non-incident dashboards.
- [ ] **25.** Visual accessibility is verified: color palettes are distinguishable for color-blind responders.
