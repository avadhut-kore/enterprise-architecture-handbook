# M&A Architecture Integration

During mergers and acquisitions, the architect evaluates technical debt, estimates integration synergies, and consolidates fragmented application portfolios.

## 1. Technical Due Diligence Dimensions
- **Codebase & Architecture Quality**: Architecture diagrams, dependency health, license compliance (GPL risks), and test coverage.
- **Cybersecurity & Compliance**: Vulnerability history, SOC2/ISO status, IAM controls, and known breaches.
- **Infrastructure TCO**: Cloud spend, third-party software licensing, and contract renewal cliffs.
- **Team & Key Person Dependency**: Knowledge concentration in key individuals vs documented runbooks.

## 2. Post-Merger Integration Archetypes

| Strategy | Integration Depth | Speed | Risk | Best Applied When |
| :--- | :--- | :--- | :--- | :--- |
| **Absorb** | Full migration into parent stack; acquired tech retired. | Slow (12-24 mos) | High | Acquired product has severe tech debt but valuable customer book. |
| **Federate (Loose Coupling)**| Integrate via SSO, shared APIs, and common data reporting. | Fast (3-6 mos) | Low | Standalone product serving independent market segment. |
| **Best-of-Breed Blend** | Unify core platforms into a modernized hybrid. | Very Slow | Extremely High | Merger of equals with complementary platform capabilities. |

## Related Modules
- [Application Portfolio Management](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/portfolio-thinking/application-portfolio-management.md)
- [Decommissioning & Sunsetting](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/obsolescence/decommissioning-and-sunsetting-systems.md)
