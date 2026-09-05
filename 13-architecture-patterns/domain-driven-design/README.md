# Domain-Driven Design (DDD)

Domain-Driven Design (Eric Evans) is an approach to software development that centers the architecture around a deeply understood, evolving model of the business domain.

> [!IMPORTANT]
> **DDD is NOT Mandatory**: Applying full tactical DDD (Aggregates, Repositories, Domain Events) to a simple CRUD application or standard data-ingest pipeline introduces massive accidental complexity. DDD provides immense value in complex, high-churn enterprise core domains, but is unnecessary overhead for generic or supporting subdomains.

---

## Catalog of Strategic & Tactical DDD Documents

### Strategic Design (Contexts, Subdomains, Mapping)
- [DDD Overview & Pragmatic Adoption](ddd-overview.md)
- [Domain vs Technical Model](domain-vs-technical-model.md)
- [Domain Modeling Principles](domain-modeling.md)
- [Ubiquitous Language](ubiquitous-language.md)
- [Bounded Contexts](bounded-contexts.md)
- [Context Mapping](context-mapping.md)
- [Subdomains Strategy](subdomains.md)
- [Core Domain](core-domain.md)
- [Supporting Subdomain](supporting-subdomain.md)
- [Generic Subdomain](generic-subdomain.md)

### Tactical Design (Domain Building Blocks)
- [Entities](entities.md)
- [Value Objects](value-objects.md)
- [Aggregates](aggregates.md)
- [Aggregate Boundaries](aggregate-boundaries.md)
- [Domain Services](domain-services.md)
- [Application Services](application-services.md)
- [Domain Events](domain-events.md)
- [Integration Events](integration-events.md)
- [Repositories](repositories.md)
- [Factories](factories.md)

### Integration & Relationships Between Contexts
- [Anti-Corruption Layer (ACL)](anti-corruption-layer.md)
- [Published Language](published-language.md)
- [Shared Kernel](shared-kernel.md)
- [Customer-Supplier](customer-supplier.md)
- [Conformist](conformist.md)
- [Open Host Service (OHS)](open-host-service.md)

---

## Domain Modeling Practice (`ddd/modeling/`)
- [Event Storming](ddd/modeling/event-storming.md)
- [Domain Discovery](ddd/modeling/domain-discovery.md)
- [Business Capability Mapping](ddd/modeling/business-capability-mapping.md)
- [Domain Boundary Identification](ddd/modeling/domain-boundary-identification.md)
- [Aggregate Design](ddd/modeling/aggregate-design.md)
- [Bounded Context Identification](ddd/modeling/bounded-context-identification.md)
