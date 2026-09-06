# Role Readiness Gate: Technical Architect (TA) / Domain Architect

> **"Readiness for Technical Architect is proven by platform leverage, cross-application consistency, technology lifecycle governance, and developer acceleration across multiple teams."**

---

## 1. Readiness Threshold Matrix

| Pillar | Required Standard | Verification Method |
| :--- | :--- | :--- |
| **1. Knowledge** | Level 4 (Architect) across Platform Engineering, Cloud, Integration, and Security; Level 3 in Strategy. | Review against [Competency Matrix](../skill-matrix/architect-competency-matrix.md). |
| **2. Experience** | Architected and deployed 1+ shared platform capability adopted by 3+ independent squads; led the decommissioning of 1 major legacy technology. | Platform adoption telemetry, deprecation records, and team testimonials. |
| **3. Decisions** | Authored platform RFCs; curated domain entries on the corporate Technology Radar with published adoption lifecycles. | Inspect Technology Radar and RFC repository. |
| **4. Evidence** | 1 approved Domain Platform Blueprint; 1 set of automated CI/CD architectural linters; documented Technology Radar updates. | Git platform repositories, linter configurations, and radar history. |

---

## 2. Core Readiness Checklist

### Platform Strategy & Developer Acceleration
- [ ] Designs self-service Internal Developer Platforms (IDPs) that reduce time-to-first-commit for new engineers by >50%.
- [ ] Authors standardized reference blueprints that serve as golden paths for 80% of new microservice implementations.
- [ ] Prioritizes developer experience (DevEx) and adoption over authoritarian architectural mandates.

### Cross-System Consistency & Integration
- [ ] Establishes enterprise-wide API, event streaming, and telemetry standards across polyglot ecosystems.
- [ ] Eliminates duplicate engineering effort by consolidating overlapping tools and frameworks.
- [ ] Presides over cross-squad architecture reviews to spot architectural drift and integration bottlenecks early.

### Technology Governance & Obsolescence
- [ ] Active steward of the corporate [Technology Radar](../../TECHNOLOGY-RADAR.md); defines explicit transition paths for Adopt, Trial, Assess, and Hold.
- [ ] Leads multi-team migration programs away from end-of-life runtimes, vulnerable dependencies, and legacy systems.
- [ ] Implements automated architecture fitness functions (e.g., [`doc_linter.py`](../../21-architecture-tools/linters/doc_linter.py), ArchUnit) to prevent architectural decay.

---

## 3. Mandatory Evidence Portfolio Items
1. **Domain Platform Blueprint**: Comprehensive architecture specification for an internal developer platform or shared service ([Platform Blueprint](../../18-reference-architectures/README.md)).
2. **Corporate Technology Radar Stewardship**: Documented additions, transitions, and phase-out rationales ([Technology Radar](../../TECHNOLOGY-RADAR.md)).
3. **Automated Architectural Fitness Policy**: Production CI rules enforcing architectural boundaries and linting standards.

---

## 4. Remediation Plan if Not Ready
* **If lacking platform impact**: Identify a recurring pain point across 3 engineering teams (e.g., custom auth handling or inconsistent logging) and author a reusable platform module or golden path.
* **If lacking lifecycle governance**: Conduct a technical debt and obsolescence audit across your engineering domain; author an RFC outlining a 6-month deprecation roadmap.
