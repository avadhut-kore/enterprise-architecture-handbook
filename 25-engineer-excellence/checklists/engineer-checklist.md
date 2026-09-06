# Software Engineer Definition of Done Checklist

> **"A task is not 'done' when you finish typing code on your machine; it is done when it is tested, reviewed, instrumented, and running stably in production behind a feature flag."**

---

## 1. The Pre-Coding Gate
- [ ] **Requirements Clarity**: Do I understand the customer problem and the exact acceptance criteria?
- [ ] **Architectural Boundary**: Does this change fit within existing domain models, or does it require an ADR?
- [ ] **Small Batch Scoping**: Can this task be completed and merged in $< 300\text{ lines of code}$? If not, decompose it vertically.

---

## 2. Implementation & Code Craft Gate
- [ ] **Intent-Revealing Names**: Do variable, function, and struct names express clear business intent?
- [ ] **Low Cognitive Complexity**: Are nesting levels kept under 3? Are methods focused on a single responsibility?
- [ ] **Zero Hardcoded Secrets**: Are API keys, passwords, and tokens loaded strictly via environment variables or secret vaults?
- [ ] **Static Analysis Clean**: Did the code pass all local formatters (`gofmt`, `prettier`), linters, and type checkers with zero warnings?

---

## 3. Automated Testing & Verification Gate
- [ ] **Unit Test Coverage**: Are all domain calculations and branching logic covered by fast, deterministic unit tests?
- [ ] **Integration Test Rigor**: Are external dependencies (Postgres, Redis, Kafka) tested using testcontainers or clean fakes rather than brittle mocks?
- [ ] **Edge Case Invariants**: Are empty lists, null/nil values, maximum bounds, and network timeouts tested explicitly?

---

## 4. Pull Request Submission Gate
- [ ] **Small PR Size**: Is the total diff under 250–300 lines of code?
- [ ] **Commit Narrative**: Are commit messages formatted cleanly (e.g., `feat(billing): implement idempotent webhook outbox`)?
- [ ] **PR Context**: Does the PR description explain *Why* this change was made, *What* was tested, and link to the Jira/Linear issue?
- [ ] **CI Pipeline Green**: Did all CI build, lint, and automated test stages pass successfully?

---

## 5. Deployment & Production Verification Gate
- [ ] **Feature Flag Guard**: Is the new capability deployed behind a feature flag for safe dark launching?
- [ ] **Telemetry Verification**: Did I inspect Grafana/Datadog immediately post-deploy to verify error rates and latency?
- [ ] **Flag Cleanup Scheduled**: Is a calendar reminder or ticket created to remove the feature flag after full promotion?
