# Conway's Law and Team Topologies

Software architecture cannot be designed in isolation from organizational structure. Trying to build a loosely-coupled distributed microservices architecture with a monolithic, centralized team structure will inevitably fail.

## 1. Conway's Law in Action

```
Centralized Database Team + Backend Team + Frontend Team
                             │
                             ▼ (Produces)
Layered Architecture with Heavy Inter-Team Coordination Bottlenecks
                             │
                             ▼ (Compare to)
Cross-Functional Stream-Aligned Teams (End-to-End Ownership)
                             │
                             ▼ (Produces)
Decoupled Microservices / Modular Domains Aligned to Business Capabilities
```

## 2. Team Topologies (Skelton & Pais) for Architects

To design scalable enterprise systems, architects leverage four team types:

### 1. Stream-Aligned Teams
- Core product teams aligned directly to a continuous flow of business value (e.g., Checkout, Claims Processing, Onboarding).
- Cross-functional: Product Manager, Frontend, Backend, Data Engineer, QA.
- Own services from inception to production operation.

### 2. Platform Teams
- Enable stream-aligned teams to deliver work autonomously without directly dealing with low-level infrastructure complexity.
- Build internal self-service platforms, CI/CD pipelines, observability tooling, and Kubernetes environments.

### 3. Enabling Teams
- Subject matter experts (Security, Performance, AI/ML, Cloud) who upskill stream-aligned teams without becoming gatekeepers.
- Temporary engagements: embed with teams for 2-6 weeks to establish best practices.

### 4. Complicated-Subsystem Teams
- Dedicated specialists managing rare, mathematically intense, or domain-complex components (e.g., 3D graphics rendering, proprietary optical recognition algorithms, low-latency financial matching engines).

## 3. Team Interaction Modes

| Mode | Purpose | Architectural Implication |
| :--- | :--- | :--- |
| **Collaboration** | Two teams working closely together for a defined period. | Used when discovering new API boundaries or prototyping joint architecture. |
| **X-as-a-Service** | One team provides a capability as a service with clear APIs. | Platform and Complicated-subsystem interaction; minimal coordination meetings. |
| **Facilitating** | One team actively coaching and upskilling another. | Enabling teams diffusing architecture principles across the enterprise. |

## Related Modules
- [Reverse Conway Maneuver](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/organizational-design/reverse-conway-maneuver.md)
- [Platform Strategy](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/platform-strategy/README.md)
