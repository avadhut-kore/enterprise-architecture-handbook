# Lead Engineer Architectural Sanity & Release Checklist

> **"When systems span multiple squads and platforms, failure is rarely a coding bug; it is an uncoordinated assumption between teams."**

---

## 1. Cross-Team Alignment & Contract Governance
- [ ] **Cross-Squad RFC Sign-off**: Have technical leads from all upstream and downstream squads reviewed and signed off on the RFC?
- [ ] **Contract Breaking-Change Gate**: Have Protobuf or OpenAPI schemas been validated against backward-compatibility linters (`buf breaking`)?
- [ ] **Dependency Topology Review**: Does the cross-service call graph have zero circular dependencies or tight synchronous coupling?

---

## 2. Platform Paved Roads & Operational Sanity
- [ ] **Paved Road Scaffolding**: Does the initiative utilize standard company developer templates, logging libraries, and CI/CD pipelines?
- [ ] **Systemic Failure Mode Review**: Have we evaluated the failure mode if an entire cloud availability zone goes offline?
- [ ] **Security & Identity Gate**: Are inter-service communications authenticated via zero-trust mTLS or signed JWTs with short expiry?

---

## 3. Financial & Capacity Sanity (FinOps)
- [ ] **Capacity Forecast**: Has storage growth, read/write IOPs, and network egress bandwidth been modeled for 12-month peak traffic?
- [ ] **FinOps Budget Approval**: Is the projected monthly cloud compute and database spend within the department's authorized infrastructure budget?

---

## 4. Multi-Phase Cutover & Rollout Sequencing
- [ ] **Sequenced Deployment Plan**: Is there a documented rollout order (e.g., Service C $\to$ Service B $\to$ Service A)?
- [ ] **Dual-Run / Shadow Read Phase**: Will new services shadow read live traffic to verify data correctness before primary cutover?
- [ ] **Executive Status Channel**: Is there a designated communication channel for executive stakeholders during the release window?
