# Shared Code Governance

## 1. The Golden Rule of Shared Code

> **Shared code creates shared dependencies and coordinated deployments.**

Before sharing code across services, ask:
*Is this shared business domain logic, or shared technical utility?*
- **Shared Technical Utility** (e.g., Base64 helper, custom HTTP handler): Acceptable to share via versioned libraries.
- **Shared Domain Logic** (e.g., Order calculation): Sharing this couples services. Duplicate the code or extract a dedicated domain microservice.
