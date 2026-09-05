# Architecture Question Frameworks

Master architects ask penetrating questions that expose unstated assumptions, ambiguous requirements, and hidden architectural risks.

---

## 1. The 7 Dimension Question Framework

### 1. Business Context & Drivers
* What specific business problem are we solving, and what measurable KPI moves when we succeed?
* Why is this being funded *now* instead of 12 months ago or 12 months from now?
* What happens to the business if we do absolutely nothing?
* Who is the executive business sponsor who will defend this budget when trade-offs arise?

### 2. Scale & Workload Profiles
* What is the steady-state request rate, and what is the peak-to-average traffic multiplier?
* What is the read-to-write ratio across core entities?
* What is the expected 3-year data accumulation volume, and what is the data retention policy?
* What is the geographic distribution of users, and what are their latency expectations?

### 3. Reliability & Failure Modes
* What is the financial and operational cost of 1 hour of downtime during peak business operations?
* What is the acceptable Recovery Point Objective (RPO: maximum data loss) and Recovery Time Objective (RTO)?
* Can this business workflow operate in a degraded mode with eventual consistency, or is strict ACID consistency mandatory?
* What happens when the primary database engine becomes unavailable for 5 minutes?

### 4. Security & Compliance
* What is the data classification of every entity processed, stored, or transmitted (PII, PCI, PHI)?
* What regulatory frameworks legally bind this system (GDPR, HIPAA, SOC 2, DORA)?
* What is the blast radius if an attacker compromises a single application container?
* How are secrets, API keys, and cryptographic certificates rotated in production?

### 5. Financial Economics & TCO
* What is the capital expenditure (Capex) budget envelope and maximum monthly operational cloud spend (Opex)?
* What is the projected infrastructure cost per settled business transaction?
* Does this architecture scale costs sub-linearly with revenue growth, or will infrastructure bills explode?

### 6. Organizational & Team Realities
* Which product squad will own, support, and maintain this system in production at 3 AM?
* Does the engineering team possess production experience with the proposed technology stack?
* How does this architecture align with team boundaries to minimize cross-squad coordination overhead?

### 7. Evolution & Exit Strategy
* Which architectural decisions in this proposal are one-way doors (irreversible)?
* If this commercial vendor triples its pricing in Year 3, what is our technical exit strategy?
* How will this system adapt when transaction volume increases by 10x?
