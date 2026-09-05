# Observability Testing & Chaos Readiness Checklist

## 1. Executive Summary
This 25-point checklist provides engineering squads, SRE teams, and Architecture Review Boards (ARBs) with an objective verification rubric for testing observability systems, running chaos experiments, and maintaining synthetic monitors.

---

## 2. The 25-Point Checklist

### Section 1: Pre-Production Telemetry Validation
- [ ] **01.** Prometheus alert and recording rules are unit-tested in CI/CD using `promtool test rules`.
- [ ] **02.** Structured log schemas are validated against corporate JSON schemas during automated builds.
- [ ] **03.** OpenTelemetry trace propagation is verified in staging via automated trace-based integration tests.
- [ ] **04.** New microservice pull requests verify that RED metrics are emitted for all newly introduced endpoints.
- [ ] **05.** Sensitive data linters verify that zero un-sanitized PII or credentials leak into test logs.

### Section 2: Chaos Engineering & Fault Injection
- [ ] **06.** Chaos experiments operate with strictly bounded blast radiuses (isolated to staging or canary pools).
- [ ] **07.** Automated abort conditions (steady-state monitors) terminate chaos experiments instantly if error budget is threatened.
- [ ] **08.** Network delay chaos verifies that client-side timeouts and circuit breakers trigger within configured thresholds.
- [ ] **09.** Chaos tests verify that when a dependency fails, the root-cause alert fires before downstream symptom alerts.
- [ ] **10.** Pod crash and container kill tests confirm that Kubernetes self-heals without user-facing 5xx errors.
- [ ] **11.** Database failover chaos confirms that connection pools re-establish automatically without manual pod restarts.

### Section 3: SRE GameDays & Simulation Drills
- [ ] **12.** GameDays are conducted at least quarterly for all Tier-1 enterprise applications.
- [ ] **13.** Every GameDay scenario has a written hypothesis, steady-state baseline, and rollback plan.
- [ ] **14.** Incident responders are evaluated on Mean Time to Detect (MTTD) and Mean Time to Mitigate (MTTR).
- [ ] **15.** Responders strictly adhere to published runbooks; missing or ambiguous instructions are logged as remediation tasks.
- [ ] **16.** Post-GameDay retrospectives yield prioritized engineering action items tracked in Jira.

### Section 4: Synthetic Monitoring & Active Probing
- [ ] **17.** Synthetic probes continuously execute critical user journeys (e.g., login, search, checkout) 24/7/365.
- [ ] **18.** Probes execute from at least 3 geographically distinct cloud regions to detect regional transit failures.
- [ ] **19.** Synthetic test journeys execute with headless browser automation (Playwright / Puppeteer).
- [ ] **20.** Synthetic tests assert both functional correctness (HTTP 200/201) and performance SLOs (journey $< 5\text{s}$).
- [ ] **21.** Test credentials used by synthetic monitors are rotated automatically to prevent false expiry pages.
- [ ] **22.** Synthetic monitors page on-call engineers when failures occur consecutively across multiple regions.

### Section 5: Governance & Resiliency Culture
- [ ] **23.** Chaos engineering results and telemetry accuracy scorecards are presented to engineering leadership.
- [ ] **24.** Services that fail chaos drills are restricted from accelerating release velocity until remediated.
- [ ] **25.** GameDay participation is rotated to ensure all on-call engineers gain practical incident response experience.
