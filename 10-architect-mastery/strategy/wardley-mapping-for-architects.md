# Wardley Mapping for Architects

Wardley Mapping (Simon Wardley) provides situational awareness by mapping components along two axes: **Value Chain (Visibility to User)** and **Evolution (Maturity)**.

## 1. The Four Evolutionary Stages

```
Value Chain (High)
      ▲
      │   [User Need]
      │        │
      │   [Public Web UI]
      │        │
      │   [Custom Business Logic]
      │        │
      │   [Compute Engine] ───────────────► [Cloud Virtual Machines]
      │        │                                     │
      ▼   [Power Grid] ────────────────────────► [Utility Commodity]
      └─────────────────────────────────────────────────────────────►
        Genesis  │  Custom-Built  │  Product/Rental  │  Commodity/Utility
                               Evolution
```

### Stage 1: Genesis
- Unique, rare, uncertain, rapidly changing. Build exploratory prototypes in-house.
- Example: Cutting-edge quantum computing algorithms, custom bespoke deep learning kernels.

### Stage 2: Custom-Built
- Bespoke software built by individual enterprises. Increasing reliability, high operational cost.
- Example: Proprietary supply chain routing optimization engines.

### Stage 3: Product / Rental
- Commercially available products, SaaS platforms, or established open-source projects.
- Example: Postgres, Kafka, Salesforce, Datadog.

### Stage 4: Commodity / Utility
- Standardized, volume-based, ubiquitous utility services. High certainty, zero competitive differentiation.
- Example: AWS S3, compute cycles, electricity, public internet.

## 2. The Golden Rule of Wardley Strategy
**Never build custom software on components that have evolved to Commodity/Utility.** Outsource or leverage cloud managed services for utility layers, and focus custom development exclusively on Genesis and Custom-Built stages where business differentiation exists.

## Related Modules
- [Architecture Strategy Formulation](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/strategy/architecture-strategy-formulation.md)
- [Platform Strategy](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/platform-strategy/README.md)
