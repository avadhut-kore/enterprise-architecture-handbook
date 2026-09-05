# Architecture Decision Records & Evolution Roadmap: Marketplace

## 1. Canonical Architecture Decision Records

### ADR-001: Adoption of Managed Payout Rails (Stripe Connect) over Custom Banking Integration
- **Status**: Accepted
- **Context**: Disbursing payouts across 40 global countries requires complex local banking rails, KYC identity verification, and currency conversion.
- **Decision**: Outsource seller KYC, bank account tokenization, and payout disbursement to Stripe Connect / Adyen.
- **Consequences**: Fast time-to-market; ongoing payment interchange SaaS fee.

---

## 2. Evolution Roadmap (1x to 100x Scale)
- **Stage 1 (1x)**: Monolithic marketplace with manual seller payout batches.
- **Stage 2 (10x)**: Automated escrow split-payments; OpenSearch catalog; automated dispute workflows.
- **Stage 3 (100x)**: Global multi-currency cross-border trade engine with AI counterfeit listing detection.
