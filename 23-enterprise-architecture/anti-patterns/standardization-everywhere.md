# Anti-Pattern: Standardization Everywhere

---

## 1. The Symptom
> "Enforcing rigid technology uniformity across fundamentally different business domains (e.g., forcing AI teams to use Java)."

In enterprises afflicted by this anti-pattern, architects and leaders notice:
* High friction between technical teams and executive business sponsors.
* Major IT investments delivering systems that fail to gain user adoption.
* Decisions justified by technical novelty rather than customer value or risk reduction.

---

## 2. The Root Cause
Why organizations fall into this trap:
* Misaligned incentives: engineering rewarded for adopting trendy tech; business rewarded for short-term revenue.
* Lack of Business Architecture maturity; absence of clear business capability mapping.
* Architecture treated as an academic ivory-tower discipline rather than a commercial transformation engine.

---

## 3. The Enterprise Damage
* **Financial Waste**: Millions spent on software licenses and cloud infrastructure that do not move corporate KPIs.
* **Loss of Architectural Credibility**: Business leaders stop consulting architects, treating them as blockers to be routed around.
* **Compounded Technical Debt**: Solutions become over-engineered, difficult to maintain, and brittle in production.

---

## 4. The Architectural Prescription & Remediation
1. **Standardize common commodity plumbing (IAM, cloud landing zones, CI/CD); permit domain-specific diversification where justified.**
2. Conduct a formal Portfolio Assessment to evaluate existing assets against the TIME model.
3. Reframe all technical discussions into the Minto Pyramid executive narrative: Lead with Business Outcome, follow with Trade-offs, conclude with Architecture.
