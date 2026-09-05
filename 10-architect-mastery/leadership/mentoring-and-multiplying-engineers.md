# Mentoring and Multiplying Engineers

An architect who does not teach becomes a bottleneck. The highest leverage activity of a principal architect is elevating senior engineers into architectural thinkers.

## 1. Architectural Thinking Apprenticeship

1. **Shadowing ADR Creation**: Bring senior engineers into early discovery interviews, stakeholder negotiation meetings, and ADR drafting sessions.
2. **Architecture Katas**: Host monthly 60-minute architecture design exercises where engineers design a system under constraints (e.g., "Design a ticketing system with 1M concurrent users without using Redis").
3. **Safe Delegation**: Delegate ownership of bounded architectural decisions (e.g., selecting an object storage abstraction or message envelope schema) with architect review.

## 2. The "Teach How to Fish" Heuristic
When an engineer asks: *"Should we use SQS or Kinesis here?"*
Never answer: *"Use SQS."*
Instead answer: *"What are the ordering requirements, replay expectations, and consumer fan-out needs? Let's look at the master trade-offs library together."*

## Related Modules
- [Master Trade-offs Library](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/trade-offs/master-trade-offs-library.md)
- [Architecture Review Operating Model](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/architecture-review/architecture-review-board-operating-model.md)
