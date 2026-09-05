# Architectural Anti-Patterns Master Index

Anti-patterns are recurring software design choices that appear intuitive at first, but reliably lead to negative consequences.

## 1. The Top Enterprise Architectural Anti-Patterns

### 1. Distributed Monolith
- **Symptom**: 30 microservices that must be deployed together in a strict lockstep order, sharing an internal database or invoking synchronous chains 6 layers deep.
- **Remediation**: Consolidate tightly coupled services into a modular monolith, or enforce strict asynchronous event boundaries.

### 2. Database-as-an-Integration-Bus
- **Symptom**: Multiple autonomous applications reading and writing directly to the same database tables.
- **Remediation**: Establish strict service ownership; expose bounded context data via APIs or published domain events.

### 3. Entity Services (Anemic Microservices)
- **Symptom**: Creating a microservice for every database table (e.g., `UserService`, `OrderService`, `ItemService`) resulting in massive network hops for basic business logic.
- **Remediation**: Align services to Business Capabilities and Aggregates (DDD), not database tables.

### 4. Golden Hammer / Law of the Instrument
- **Symptom**: Forcing every enterprise problem into a single favored paradigm (e.g., using Kafka for simple request-response, or using Elasticsearch as primary ACID storage).
- **Remediation**: Choose purpose-built tools based on access patterns and trade-off analysis.

## Related Modules
- [Master Trade-offs Library](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/trade-offs/master-trade-offs-library.md)
- [Enterprise Failure Modes](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/failure-analysis/enterprise-failure-modes-post-mortems.md)
