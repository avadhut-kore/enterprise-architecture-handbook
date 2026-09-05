# DevOps Operating Models & Organizational Topologies

How an enterprise organizes its teams dictates the software architecture it produces (Conway's Law).

## 1. The Five Enterprise Operating Models

### Model 1: Fully Embedded DevOps (Cross-Functional Stream-Aligned)
- **Structure**: Each product squad has dedicated software engineers, QA, and embedded DevOps/SRE engineers.
- **Pros**: Complete autonomy, zero external handoffs, rapid cycle time.
- **Cons**: Duplicated efforts across squads, divergence of tooling, high talent hiring cost.

### Model 2: Centralized Platform Team with Golden Paths (Recommended for Enterprise)
- **Structure**: A centralized Platform Engineering team builds internal self-service capabilities (Internal Developer Platform). Stream-aligned squads consume platform APIs autonomously.
- **Pros**: Standardization, cost efficiency, compliance guardrails without slowing teams down.
- **Cons**: Requires product management discipline; risk of platform team becoming an isolated ivory tower.

### Model 3: Enabling DevOps Team (Coaching & Diffusion)
- **Structure**: A team of expert DevOps architects embeds with product teams for 4-8 weeks to modernize pipelines and upskill engineers, then rotates out.
- **Pros**: Spreads knowledge across the enterprise without building permanent silos.
- **Cons**: Requires high organizational maturity and engineering willingness to learn.

### Model 4: Siloed Operations as a Service (Anti-Pattern)
- **Structure**: Development writes code, then files Jira tickets to a "DevOps Team" to deploy to staging or provision an S3 bucket.
- **Result**: Queue delays, slow delivery, frustration, and total lack of developer ownership.

## 2. Selection Criteria Matrix

| Organizational Trait | Recommended Operating Model |
| :--- | :--- |
| **Startup / Scaleup (< 50 engineers)** | Cross-Functional Embedded Engineers |
| **Mid-Size Enterprise (50 - 500 engineers)** | Platform Team + Golden Paths |
| **Global Enterprise (1,000+ engineers)** | Federated Platform Engineering + Enabling CoE |
| **Highly Regulated Bank / Healthcare** | Platform Team with Automated Compliance Guardrails |

## Related Resources
- [Platform Engineering](../platform-engineering/README.md)
- [Organizational Design & Team Topologies](../../10-architect-mastery/organizational-design/README.md)
