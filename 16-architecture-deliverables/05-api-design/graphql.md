# GraphQL Schema & Federation Standards

## 1. Governance & Best Practices
* Enforce query depth limits (max depth 6) to prevent malicious nested query attacks.
* Require query cost analysis at the API gateway layer.
* Use Apollo Federation for distributed subgraph composability across microservices.
