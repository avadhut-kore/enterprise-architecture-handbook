# Preserving Optionality in Architecture Design

Options have economic value. In an environment of rapid technological change and market uncertainty, an architecture that preserves the option to pivot is worth significantly more than an overly optimized rigid architecture.

## 1. Principles of Architectural Optionality

1. **Defer Decisions to the Last Responsible Moment**: Do not choose a physical database engine until domain models and query patterns are validated.
2. **Build Thin Wrappers Around External Dependencies**: Wrap third-party SDKs (e.g., Stripe, Twilio, OpenAI) in internal domain interfaces to preserve the option to change providers in hours rather than months.
3. **Favor Composition Over Deep Inheritance**: Modular pipelines allow plugging new processors without rewriting core execution graphs.

## Related Modules
- [Master Trade-offs Library](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/trade-offs/master-trade-offs-library.md)
- [Irreversible vs Reversible Decisions](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/decision-making/irreversible-vs-reversible-decisions.md)
