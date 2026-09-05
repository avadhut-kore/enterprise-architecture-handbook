# Architecture Pre-Mortem Guide: Prospective Hindsight

A pre-mortem (Gary Klein) flips the standard risk assessment mindset. Instead of asking *"What could go wrong?"*, the team assumes:
> *"It is 12 months in the future. The project has launched and suffered a catastrophic, public disaster. What caused it?"*

## 1. The 5-Step Pre-Mortem Workshop

1. **Set the Stage (5 mins)**: Gather engineering leads, architects, product managers, and SREs. Declare total failure.
2. **Individual Brainstorm (10 mins)**: Every participant silently writes down every conceivable reason for the disaster on sticky notes without censorship.
3. **Cluster and Categorize (15 mins)**: Group failure modes:
   - *Technical/Operational*: Connection pool exhaustion, database deadlocks, slow queries.
   - *Organizational/Process*: Missing skillsets, key person dependencies, unclear ownership.
   - *Product/Business*: Scope creep, unrealistic launch deadlines, third-party SLA breaches.
4. **Prioritize the "Deadliest Sins" (15 mins)**: Vote on the top 3 most likely fatal failure modes.
5. **Architectural Countermeasures (15 mins)**: Draft ADR amendments and automated fitness functions that make these specific failures impossible.

## Related Modules
- [Architectural Red Teaming](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/red-team/architectural-red-teaming.md)
- [Blameless Post-Mortem Framework](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/post-mortem/blameless-post-mortem-framework.md)
