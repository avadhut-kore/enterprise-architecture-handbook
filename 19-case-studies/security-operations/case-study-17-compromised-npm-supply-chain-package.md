# Enterprise Case Study: Compromised NPM Dependency Exfiltrating Environment Variables

## 1. Business & System Context
Large-scale enterprise platform processing high-throughput mission-critical transactions.

## 2. Incident Description
Typosquatted package injecting malicious telemetry. The failure resulted in customer disruption, elevated error budget burn rates, and executive escalation.

## 3. Root Cause Analysis
- Inadequate architectural guardrails, missing defensive isolation, or reliance on legacy manual operational processes.

## 4. Immediate Mitigation & Recovery
- Contained the incident, restored baseline operational capacity, and executed emergency rollback.

## 5. Permanent Architectural Remediation
- **Target Architecture**: Private Artifactory mirror with SLSA Level 3 verified SBOMs.
- Codified systemic safeguards into automated CI/CD and infrastructure policies.

## 6. Lessons Learned & Preventive Controls
- Security and reliability must be engineered into the architecture from Day 0.
- All recovery runbooks must be automated and validated in regular game days.
