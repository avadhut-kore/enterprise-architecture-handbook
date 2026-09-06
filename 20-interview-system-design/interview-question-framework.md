# The Interview Question Framework: Interviewer Psychology & Probe Engine

> Understand what interviewers are actually testing beneath the surface prompt, uncover hidden constraints, and master the follow-up probe engine.

---

## 1. What Interviewers Are Actually Evaluating

Interviewers at the Principal, Staff, Lead, and Enterprise Architect levels do not grade you like a checklist. They observe how your brain works when confronted with ambiguity and technical pressure:

```
                  ┌─────────────────────────────────────┐
                  │ Can they handle ambiguity?          │
                  ├─────────────────────────────────────┤
                  │ Can they simplify before scaling?   │
                  ├─────────────────────────────────────┤
                  │ Can they identify real bottlenecks? │
                  ├─────────────────────────────────────┤
                  │ Do they reason with trade-offs?     │
                  ├─────────────────────────────────────┤
                  │ Do they think about operations?     │
                  ├─────────────────────────────────────┤
                  │ Can they defend decisions cleanly?  │
                  ├─────────────────────────────────────┤
                  │ Can they adapt when facts change?   │
                  └─────────────────────────────────────┘
```

---

## 2. The 3 Tiers of Interviewer Questions

### Tier 1: The Initial Ambiguous Prompt
* *Examples*:
  * *"Design a global payment platform."*
  * *"Design a system like Twitter/X."*
  * *"How would you modernize our core legacy banking monolith?"*
* *The Hidden Test*: **Will you jump straight to technology, or will you ask clarifying questions?** Candidates who immediately start drawing microservices fail. Senior architects clarify the business context and scope boundaries first.

### Tier 2: Mid-Interview Probes (Stress Testing Decisions)
Once you present an architecture, the interviewer will challenge your assumptions:
* *"What happens if the primary database becomes unresponsive during a flash sale?"*
* *"Why did you choose Kafka over SQS when your write throughput is only 500 RPS?"*
* *"How will you prevent split-brain if the network link between US-East and EU-West severs?"*
* *The Hidden Test*: **Can you defend your decisions without becoming defensive or dogmatic?** Can you articulate the explicit trade-off you chose?

### Tier 3: Curveball & Constraint-Shift Questions
In the final 15 minutes, interviewers introduce a sudden shift in parameters:
* *"Our budget was just cut by 40%. What can we eliminate?"*
* *"A European privacy regulation just passed requiring strict data sovereignty. How does that affect your global database schema?"*
* *"Traffic just grew 20x overnight due to a celebrity endorsement. What fails first?"*
* *The Hidden Test*: **Evolutionary adaptability.** Do you erase your whiteboard and panic, or do you methodically evolve your architecture?

---

## 3. The Reusable Follow-Up Question Engine

When practicing or preparing for interviews, test your own design against this standard battery of 14 probe questions:

```
Scale & Concurrency
  1. What happens when traffic increases 10x? What breaks first?
  2. What happens when 100,000 users concurrently attempt to claim the exact same item?

Failure & Resilience
  3. What happens if the distributed cache (Redis) dies completely? (Cache Stampede / Avalanche)
  4. What happens if the downstream payment processor experiences 5-second latency spikes?
  5. What happens if a network partition isolates one availability zone?

Data & Consistency
  6. What happens if a consumer worker crashes after reading a message but before saving state?
  7. How do you resolve write conflicts in a multi-region active-active setup?
  8. How do you ensure idempotent processing on retry?

Security & Governance
  9. How do you prevent an authenticated tenant from accessing another tenant's records?
  10. Where is sensitive PII / financial data encrypted, and who holds the keys?

Operations & Economics
  11. What is the single biggest contributor to monthly cloud infrastructure cost?
  12. If a customer reports missing an event from 2 hours ago, how do you trace what happened?
  13. How do you roll back a breaking database schema migration with zero downtime?
  14. What would you simplify to ship an MVP in 6 weeks instead of 6 months?
```

---

## 4. Uncovering Hidden Constraints

Interviewers frequently hold "hidden constraints" that they will only reveal if you ask the right questions:

| System Type | Common Hidden Constraint | Clarifying Question to Uncover It |
| :--- | :--- | :--- |
| **Notification Engine** | Strict priority delivery (e.g., OTPs must deliver in < 3s, while marketing emails can take 2 hours). | *"Are all notifications created equal in priority, or are there transactional OTPs that have strict SLA precedence?"* |
| **Payment Engine** | Regulatory requirement to preserve raw audit logs immutably for 7 years. | *"What are the compliance and financial audit retention requirements for transaction logs?"* |
| **Ride Sharing** | Driver location pings are transient (dropping a single ping is acceptable, but database write amplification must be avoided). | *"If a driver GPS ping is dropped, do we retry, or do we prioritize the freshest location over historical completeness?"* |
| **E-Commerce Catalog** | Read traffic outnumbers write traffic 5,000 to 1, but inventory counts must never oversell. | *"Is it acceptable for product descriptions to be eventually consistent while inventory reservations require strict serialization?"* |

---

## 5. Cross-References

* **Requirements Discovery Matrix**: [`requirements-discovery.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/requirements-discovery.md)
* **NFR Discovery Checklist**: [`nfr-discovery.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/nfr-discovery.md)
* **Handling Difficult Questions**: [`architecture-communication.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-communication.md)
* **Incident & Production Scenarios**: [`scenario-based/README.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/scenario-based/README.md)
