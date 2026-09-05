# Enterprise Architecture Decision Frameworks

The master catalog of 20 formal Enterprise Architecture decision scorecards providing quantitative criteria, trade-off matrices, and boundary conditions for high-stakes enterprise choices.

---

## 1. Decision Catalog Index

| # | Decision Framework | Primary Architectural Dilemma | Core Evaluation Criteria |
| :-: | :--- | :--- | :--- |
| 1 | [Centralized vs Federated Architecture](centralized-vs-federated-architecture.md) | Determining whether architectural authority should reside in a ce... | Organization scale, business unit diversity, deliv... |
| 2 | [Global vs Regional Platform](global-vs-regional-platform.md) | Deciding whether to deploy a single global platform or allow regi... | Data sovereignty laws (PIPL, GDPR), cross-border l... |
| 3 | [Standardize vs Diversify](standardize-vs-diversify.md) | Balancing technology standard efficiency with domain-specific spe... | Skill availability, operational support overhead, ... |
| 4 | [Build vs Buy](build-vs-buy.md) | Deciding whether to build proprietary software or purchase commer... | Strategic differentiation, market software maturit... |
| 5 | [Consolidate vs Coexist](consolidate-vs-coexist.md) | Deciding whether to force duplicate systems onto one platform or ... | Integration cost, cultural friction, business unit... |
| 6 | [Retain vs Modernize](retain-vs-modernize.md) | Evaluating whether a legacy system should be preserved as-is or m... | Business criticality, change frequency, defect rat... |
| 7 | [Replace vs Re-platform](replace-vs-re-platform.md) | Choosing between replacing a legacy system with SaaS or re-platfo... | Customization depth, availability of SaaS fit, cod... |
| 8 | [Cloud vs On-Premises](cloud-vs-on-prem.md) | Determining hosting tiering between public hyperscalers and priva... | Elasticity requirements, data sovereignty, ultra-l... |
| 9 | [Single Cloud vs Multi-Cloud](single-cloud-vs-multi-cloud.md) | Evaluating whether to concentrate workloads on one hyperscaler or... | Vendor lock-in leverage, regulatory secondary clou... |
| 10 | [Central Platform vs Team-Owned Platform](central-platform-vs-team-owned-platform.md) | Deciding whether infrastructure and CI/CD are owned by a dedicate... | Cognitive load on developers, standardization need... |
| 11 | [Shared Service vs Product Team](shared-service-vs-product-team.md) | Choosing between pooled functional shared service centers or dedi... | Specialization depth, handoff latency, strategic a... |
| 12 | [Global vs Local Capability](global-vs-local-capability.md) | Allocating capability ownership between global headquarters and l... | Local market intimacy, global regulatory consisten... |
| 13 | [Data Centralization vs Decentralization](data-centralization-vs-decentralization.md) | Deciding between a monolithic enterprise data warehouse and feder... | Data schema complexity, query performance, cross-d... |
| 14 | [Data Mesh vs Centralized Data Platform](data-mesh-vs-centralized-data-platform.md) | Determining when an organization is mature enough to transition f... | Data engineering maturity, domain business ownersh... |
| 15 | [API-First vs Integration Middleware](api-first-vs-integration-middleware.md) | Choosing between direct API-led connectivity and centralized ESB ... | System coupling, protocol heterogeneity, message t... |
| 16 | [Event-Driven vs Synchronous Integration](event-driven-vs-synchronous-integration.md) | Selecting between asynchronous event streaming (Kafka) and synchr... | Temporal coupling, write throughput, read latency,... |
| 17 | [AI Platform vs Application-Specific AI](ai-platform-vs-application-specific-ai.md) | Deciding whether to build a shared enterprise AI gateway/platform... | Token cost governance, prompt injection defense, E... |
| 18 | [Enterprise AI Gateway vs Direct Model Access](enterprise-ai-gateway-vs-direct-model-access.md) | Evaluating whether to mandate an intermediate AI gateway for all ... | Data leakage (PII scrubbing), credential security,... |
| 19 | [Custom AI vs SaaS AI](custom-ai-vs-saas-ai.md) | Choosing between building custom RAG/fine-tuned models and buying... | Domain specificity, proprietary intellectual prope... |
| 20 | [Acquire vs Develop Capability](acquire-vs-develop-capability.md) | Deciding whether to acquire a technology startup/competitor or de... | Time to market urgency, talent acquisition, integr... |

---

## 2. Standard Decision Scorecard Structure
Every decision framework in this directory provides:
1. **Context & Problem Statement**: The organizational or technical dilemma.
2. **Decision Criteria & Evaluation Rubric**: Weighted scoring factors.
3. **Available Architectural Options**: Clear trade-off analysis of each path.
4. **Failure Modes & Anti-Patterns**: What happens when the wrong choice is made.
5. **Concrete Enterprise Case Example**: Real-world production scenario and resulting decision.
