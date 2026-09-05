# Risk Assessment & Residual Risk Quantification

## Executive Summary

Threat modeling identifies potential vulnerabilities; risk quantification prioritizes which vulnerabilities must be engineered out immediately vs those that can be accepted or mitigated via compensating controls.

---

## 1. DREAD Scoring Rubric

$$\text{Risk Score} = \frac{\text{Damage} + \text{Reproducibility} + \text{Exploitability} + \text{Affected Users} + \text{Discoverability}}{5}$$

*(Each factor scored from 1 to 10. Overall score: 1–3 Low, 4–6 Medium, 7–8 High, 9–10 Critical).*

---

## 2. Inherent Risk vs Residual Risk

$$\text{Residual Risk} = \text{Inherent Risk} - \text{Impact of Architectural Controls}$$

- **Inherent Risk**: The raw exposure of a system assuming zero defensive controls exist (e.g., public internet-facing database).
- **Compensating Controls**: Multi-AZ private VPC, zero public IP, security group allowlist, mTLS authentication, envelope encryption.
- **Residual Risk**: The remaining exposure (e.g., risk of 0-day zero-click exploit in PostgreSQL engine). Must be evaluated against enterprise risk appetite.
