# Architecture Leadership Scenarios: Behavioral Judgment in Action

> 7 realistic architecture leadership interview scenarios featuring explicit Situation breakdowns, Interviewer Evaluations, Weak vs. Strong responses, and Leadership Signals.

---

## Scenario Catalog

1. [Scenario 1: Engineering Wants Microservices, Product Demands a 3-Month Launch](#scenario-1-engineering-wants-microservices-product-demands-a-3-month-launch)
2. [Scenario 2: Security Rejects Architecture 48 Hours Before Production Launch](#scenario-2-security-rejects-architecture-48-hours-before-production-launch)
3. [Scenario 3: Two Senior Engineers Are Deadlocked Over Database Architecture](#scenario-3-two-senior-engineers-are-deadlocked-over-database-architecture)
4. [Scenario 4: The CTO Demands Kubernetes, but the Team Has Zero Kubernetes Experience](#scenario-4-the-cto-demands-kubernetes-but-the-team-has-zero-kubernetes-experience)
5. [Scenario 5: Business Demands 99.999% Availability but Refuses Additional Funding](#scenario-5-business-demands-99999-availability-but-refuses-additional-funding)
6. [Scenario 6: The Legacy Core Mainframe Cannot Be Replaced for 5 Years](#scenario-6-the-legacy-core-mainframe-cannot-be-replaced-for-5-years)
7. [Scenario 7: Three Independent Teams Are Building Duplicate Notification Platforms](#scenario-7-three-independent-teams-are-building-duplicate-notification-platforms)

---

### Scenario 1: Engineering Wants Microservices, Product Demands a 3-Month Launch

* **Situation**: Engineering wants to decompose the legacy system into 8 microservices. The Product VP has a fixed regulatory or commercial market window to launch the new capability in 90 days.
* **What the Interviewer is Testing**: Pragmatism, commercial alignment, ability to avoid dogmatic purity, and phasing strategy.
* **Weak Response**: *"Engineering is right. Microservices are best practice, so I will tell Product that they have to wait 9 months because technical debt cannot be compromised."*
* **Strong Response**:
  * *"I would broker an evolutionary compromise. Splitting into 8 microservices in 90 days introduces fatal delivery risk due to network scaffolding, distributed tracing, and cross-team dependencies. Instead, I would propose building this feature as a **Modular Monolith** with strict in-process bounded contexts. This allows us to meet the 90-day product launch window with zero distributed networking overhead. Once the product proves commercial traction, we can extract those well-defined modules into independent microservices in Phase 2."*
* **Leadership Signals**: High commercial awareness; understands that software must deliver revenue to survive; uses modular code design as a risk-mitigation bridge.

---

### Scenario 2: Security Rejects Architecture 48 Hours Before Production Launch

* **Situation**: The CISO and Security Audit team flag an unencrypted inter-service communication path and refuse to sign off on production deployment two days before the marketing launch.
* **What the Interviewer is Testing**: Crisis management, composure under pressure, ability to balance risk against business impact, and governance remediation.
* **Weak Response**: *"I would escalate to the CEO and explain that Security is being unreasonable and blocking company growth."*
* **Strong Response**:
  * *"First, I do not panic or antagonize Security. Security is doing their job protecting the enterprise. Second, I assemble an emergency 1-hour triage with the Lead Security Architect and the Engineering Squad to understand the exact vulnerability: Is it exposed to the public internet, or strictly within an isolated private VPC? Third, we evaluate tactical immediate mitigations: Can we enable AWS ALB TLS termination or automated mesh mTLS within 24 hours? If not, can we introduce IP-restricted security groups and WAF rate limits as a temporary compensating control to obtain a signed, 14-day time-bound waiver from the CISO? Finally, for the long term, I implement automated CI/CD security scanning fitness functions so security issues are discovered in sprint 1, not 48 hours before launch."*
* **Leadership Signals**: Empathetic collaborator; treats security as a partner; solves immediate crisis with compensating controls while fixing the root process.

---

### Scenario 3: Two Senior Engineers Are Deadlocked Over Database Architecture

* **Situation**: Engineer A insists on PostgreSQL; Engineer B insists on Cassandra. The disagreement has stalled sprint planning for three weeks.
* **What the Interviewer is Testing**: Conflict de-escalation, objective technical evaluation, and decisive leadership.
* **Weak Response**: *"I am the architect, so I will just pick PostgreSQL and tell Engineer B to deal with it."*
* **Strong Response**:
  * *"I bring both engineers into a room and depersonalize the debate. First, we write down the system's actual functional requirements and scale numbers: What is our write RPS? (e.g., 2,500 RPS). What is our data volume? (e.g., 500 GB/year). What query patterns exist? (e.g., frequent multi-table JOINs for financial audit reports). Looking at those numbers, a single PostgreSQL instance easily handles 2,500 RPS and supports our relational query needs, whereas Cassandra would introduce eventual consistency complications and make relational reporting impossible. I give Engineer B full credit for thinking about scale, but demonstrate that Cassandra is premature optimization for our current constraints. I record this decision in an ADR and ask both engineers to commit."*
* **Leadership Signals**: Data-driven mediator; focuses on constraints rather than ego; documents rationale transparently.

---

### Scenario 4: The CTO Demands Kubernetes, but the Team Has Zero Kubernetes Experience

* **Situation**: The CTO read an executive report on Kubernetes and wants all 5 company services migrated to EKS immediately. The 6-person engineering team only knows basic Docker and VMs.
* **What the Interviewer is Testing**: Managing up, preventing resume-driven development, and protecting team cognitive load.
* **Weak Response**: *"I'll tell the CTO that Kubernetes is stupid for small teams and refuse to do it."*
* **Strong Response**:
  * *"I schedule a 1-on-1 with the CTO to understand their underlying goal. Usually, executive interest in Kubernetes is driven by a desire for automated scaling, self-healing, faster deployments, and cloud cost optimization. I would present a data-driven proposal: 'We share your goals for automated scaling and zero-downtime deployments. However, our 6-person team currently lacks the operational bandwidth to manage Kubernetes control planes, CNIs, and ingress controllers—it would consume 40% of our engineering capacity for 6 months. Instead, we can achieve 95% of your desired outcomes using AWS ECS / Fargate or Google Cloud Run with standard Docker containers today, with zero control-plane operational overhead. We can revisit Kubernetes when our engineering organization scales past 50 engineers.' "*
* **Leadership Signals**: Executive empathy; manages up effectively by validating the goal while steering away from the wrong implementation.

---

### Scenario 5: Business Demands 99.999% Availability but Refuses Additional Funding

* **Situation**: The Product VP demands "Five Nines" (under 5 minutes of downtime per year) for a standard SaaS platform, but Finance rejects any budget increase for multi-region active-active infrastructure.
* **What the Interviewer is Testing**: Ability to educate non-technical executives on financial unit economics and SLA trade-offs.
* **Weak Response**: *"I'll just try my best to make a single region 99.999% available."*
* **Strong Response**:
  * *"I create a simple visual matrix showing the exponential cost curve of availability: 99.9% (8.7 hours downtime/yr) costs $5,000/mo; 99.99% (52 minutes downtime/yr) costs $12,000/mo; 99.999% (5 minutes downtime/yr) requires active-active multi-region deployment, cross-continental data consensus, redundant staffing, and costs $60,000/mo. I ask the business leadership: 'What is the exact financial revenue loss if our platform is down for 30 minutes on a Sunday?' If the revenue loss is $5,000, spending an extra $600,000 per year on infrastructure to prevent it makes no financial sense. I steer them toward a realistic 99.9% SLA with robust multi-AZ failover and automated backups, which fully satisfies user expectations within budget."*
* **Leadership Signals**: Commercial fiduciary mindset; educates stakeholders using business ROI rather than technical jargon.

---

### Scenario 6: The Legacy Core Mainframe Cannot Be Replaced for 5 Years

* **Situation**: The company relies on an aging on-premise COBOL/DB2 mainframe core that cannot be replaced or modified without immense risk, but modern digital web/mobile channels require fast APIs and new features.
* **What the Interviewer is Testing**: Evolutionary modernization patterns, change risk management, and enterprise integration.
* **Weak Response**: *"We must initiate a multi-million-dollar big-bang rewrite to replace the mainframe immediately."*
* **Strong Response**:
  * *"Proposing a big-bang rewrite of a 20-year-old core banking system is a classic failure mode. Instead, I deploy an **Event-Driven Strangler Fig Architecture**. We install Change Data Capture (CDC via IBM InfoSphere or Debezium) directly on the mainframe DB2 transaction log. Every time an account or balance updates, CDC streams the change into an Apache Kafka event mesh in the cloud. We build cloud-native microservices that read from Kafka and maintain optimized read models in PostgreSQL/Elasticsearch. Digital mobile channels query the fast cloud read replicas at sub-50ms latency with zero load on the mainframe. New business features are built cloud-native, and the mainframe is relegated to a simple backend settlement ledger until it can be systematically decommissioned."*
* **Leadership Signals**: Master of legacy enterprise modernization; isolates risk; creates immediate modern business value without destabilizing the core.

---

### Scenario 7: Three Independent Teams Are Building Duplicate Notification Platforms

* **Situation**: Due to lack of central coordination, the E-commerce team, Marketing team, and Mobile team have each started building separate notification engines.
* **What the Interviewer is Testing**: Organizational governance, deduplication of enterprise platforms, and platform team leadership.
* **Weak Response**: *"I'll order two of the teams to delete their code and use the third team's system."*
* **Strong Response**:
  * *"I convene a joint architecture workshop with the leads of all three teams. I recognize that each team built their own solution because they had urgent business needs that central IT was not satisfying. We map their overlapping requirements (SMS, Email, Push, Rate Limiting, Template Engine). I propose creating a unified **Enterprise Platform Team** dedicated to building an internal Notification-as-a-Service paved road. We evaluate the 3 existing codebases, adopt the strongest implementation as the foundational core, and invite members from all three teams to contribute to the open internal RFC. We give the other two teams a gradual 6-month migration roadmap so they can decommission their duplicate systems without disrupting their immediate product deliverables."*
* **Leadership Signals**: Empathetic platform consolidator; avoids heavy-handed executive decrees; respects past engineering investments while consolidating enterprise capabilities.

---

## Cross-References

* **Stakeholder Management**: [`stakeholder-management.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/leadership/stakeholder-management.md)
* **Conflict Resolution**: [`conflict-management.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/leadership/conflict-management.md)
* **Legacy Modernization Playbook**: [`architecture-interviews/legacy-modernization.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/legacy-modernization.md)
