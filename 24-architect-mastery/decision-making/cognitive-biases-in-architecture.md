# Cognitive Biases in Architecture

Architecture decisions fail more often from psychological traps and organizational dysfunctions than technical incompetence. Recognizing cognitive biases is mandatory for professional architectural judgment.

## 1. The Critical Biases in Architecture

### 1. Sunk Cost Fallacy
- **Manifestation**: Continuing to invest millions into an in-house bespoke message broker or proprietary framework that is demonstrably failing because "we already spent 3 years building it."
- **Countermeasure**: Frame decisions using prospective opportunity cost: "If we started today with a clean slate and current funding, would we build this or use an industry-standard managed service?"

### 2. Resume-Driven Development (RDD) / Shiny Object Syndrome
- **Manifestation**: Adopting complex distributed architectures (e.g., event-sourcing, Rust microservices, or custom Kubernetes operators) simply because engineering leadership wants marketable experience.
- **Countermeasure**: Enforce the Boring Technology principle. Require justifications that demonstrate measurable business value over simpler alternatives.

### 3. Survivorship Bias
- **Manifestation**: "Netflix and Google built custom distributed orchestration platforms, so our 30-engineer company should replicate their architecture."
- **Countermeasure**: Analyze context mismatch. Netflix's scale, talent density, and economics do not apply to standard enterprise software domains.

### 4. Status Quo Bias & Loss Aversion
- **Manifestation**: Refusing to modernize a legacy mainframe or end-of-life monolith because "it has worked for 15 years and change is risky," ignoring compounding operational risk.
- **Countermeasure**: Calculate the Cost of Inaction (CoI) alongside modernization costs.

### 5. Hyper-Specialization / Law of the Instrument ("Golden Hammer")
- **Manifestation**: A database expert solves every business problem using stored procedures and complex relational triggers, regardless of streaming or search requirements.
- **Countermeasure**: Mandate peer architectural reviews from cross-domain architects.

## Related Modules
- [Architecture Decision-Making Framework](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/decision-making/architecture-decision-making-framework.md)
- [Master Trade-offs Library](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/trade-offs/master-trade-offs-library.md)
