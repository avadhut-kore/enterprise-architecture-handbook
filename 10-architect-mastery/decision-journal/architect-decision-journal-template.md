# Architect Decision Journal Template

Great judgment is developed by comparing past predictions with actual outcomes. Use this decision journal to log major technical choices at the moment they are made.

---

### Decision Entry: [e.g., Choosing Apache Pulsar over Kafka for Multi-Tenancy]

- **Date & Context**: [2026-04-10]
- **Current Emotional State & Stress Level**: [Calm / Under Pressure from Q3 Launch Deadline]
- **Problem Statement**: [Need multi-tenancy and geo-replication with 10k separate topics]

#### 1. The Decision Made
[Selected Apache Pulsar with BookKeeper storage tiering]

#### 2. The Mental Model & Assumptions
- Assumption 1: Pulsar's decoupled compute and storage will simplify horizontal scaling.
- Assumption 2: Team can master BookKeeper operational complexity within 60 days.

#### 3. Expected Outcome & Predictions (6 Months)
- Projected Metric: Cluster provisioning time reduced by 50%; zero partition rebalance storms.
- Confidence Score: 85%

#### 4. Post-Outcome Review (To be completed 6 months later)
- Date of Review: [2026-10-10]
- What actually happened? [BookKeeper operational complexity proved harder than anticipated; required 2 weeks consulting assistance, but multi-tenancy worked flawlessly.]
- Calibration Lesson: [Factor operational learning curves higher for niche storage engines.]
