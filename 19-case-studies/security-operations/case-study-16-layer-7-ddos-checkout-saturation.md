# Enterprise Case Study: Volumetric Layer 7 DDoS Attack on Enterprise Checkout

## 1. Business & System Context
Large-scale enterprise platform processing high-throughput mission-critical transactions.

## 2. Incident Description
500,000 req/sec HTTP flood bypassing basic rate limits. The failure resulted in customer disruption, elevated error budget burn rates, and executive escalation.

## 3. Root Cause Analysis
- Inadequate architectural guardrails, missing defensive isolation, or reliance on legacy manual operational processes.

## 4. Immediate Mitigation & Recovery
- Contained the incident, restored baseline operational capacity, and executed emergency rollback.

## 5. Permanent Architectural Remediation
- **Target Architecture**: Deployed Cloudflare Magic Transit and behavioral challenge WAF rules.
- Codified systemic safeguards into automated CI/CD and infrastructure policies.

## 6. Lessons Learned & Preventive Controls
- Security and reliability must be engineered into the architecture from Day 0.
- All recovery runbooks must be automated and validated in regular game days.
