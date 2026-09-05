# Mermaid GitGraph & Branching Models

GitGraph visualizes branching strategies, release trains, hotfix flows, and trunk-based development practices.

## Scaled Trunk-Based Development with Short-Lived Feature Branches

```mermaid
gitGraph
    commit id: "Initial v1.0.0"
    commit id: "Setup CI/CD"
    branch feature/payment-gateway
    checkout feature/payment-gateway
    commit id: "Add Stripe SDK"
    commit id: "Unit tests"
    checkout main
    merge feature/payment-gateway id: "PR #104 Merged"
    branch release/v1.1.0
    checkout release/v1.1.0
    commit id: "Tag v1.1.0-RC1"
    checkout main
    commit id: "Changelog update"
    checkout release/v1.1.0
    commit id: "Promote Prod v1.1.0" tag: "v1.1.0"
    checkout main
    merge release/v1.1.0 id: "Sync back"
```

## Architectural Guidelines
* Use GitGraph to visually establish development workflows for engineering teams during architecture onboarding.
