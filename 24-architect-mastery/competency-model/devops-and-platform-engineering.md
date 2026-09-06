# Competency Deep Dive: DevOps & Platform Engineering

> **"Platform engineering is not building another layer of bureaucracy. It is the discipline of creating self-service internal developer platforms (IDPs) and golden paths that make the secure, scalable, and compliant way the easiest way."**

---

## 1. Definition & Core Essence

**DevOps & Platform Engineering** is the discipline of architecting automated software delivery pipelines and internal self-service developer platforms. It encompasses:
* Platform as a Product: Designing Internal Developer Platforms (IDPs) that reduce developer cognitive load and eliminate ticket-based infrastructure provisioning.
* GitOps & continuous delivery: Declarative infrastructure, ArgoCD/Flux drift reconciliation, progressive delivery (canary, blue-green), and automated rollback.
* Golden paths & paved roads: Reusable application scaffolding, standardized container base images, and automated compliance gates.
* Software delivery metrics: Optimizing the four DORA metrics (Deployment Frequency, Lead Time for Changes, Change Failure Rate, Time to Restore Service).

---

## 2. Why It Matters for Modern Architects

* **Solution Architects**: Ensures architectural designs can be built, tested, and deployed safely 50 times a day without requiring manual operator intervention.
* **Technical Architects**: Governs the enterprise CI/CD infrastructure, Kubernetes cluster standards, and automated architectural linters.
* **Enterprise Architects**: Eliminates multi-million-dollar developer productivity waste across engineering divisions.

---

## 3. 5-Tier Behavioral Capability Progression

| Level | Behavioral Capability Anchor |
| :--- | :--- |
| **L1 (Practitioner)** | Uses Git workflows; configures simple CI pipelines running unit tests and linters. |
| **L2 (Independent)** | Writes Dockerfiles, Helm charts, and multi-stage container builds; creates automated CI/CD deployment pipelines to staging and production. |
| **L3 (Advanced)** | Implements GitOps deployment fabrics with automated canary verification; builds reusable CI/CD pipeline templates across multiple squads. |
| **L4 (Architect)** | Designs Internal Developer Platforms (IDPs); implements self-service "Golden Paths" that reduce onboarding time from weeks to hours; enforces automated architectural linters ([Doc Linter](../../21-architecture-tools/linters/doc_linter.py)). |
| **L5 (Strategic)** | Redesigns the corporate software delivery lifecycle (SDLC) across thousands of engineers to achieve elite DORA performance and transform engineering culture. |

---

## 4. Practical Experiences & Apprenticeship Exercises

1. **Build a Self-Service Golden Path**: Author an application template (e.g., Backstage / Cookiecutter) that provisions a Git repository, CI/CD pipeline, Kubernetes manifest, OpenTelemetry instrumentation, and cloud database with a single click.
2. **Implement GitOps Progressive Delivery**: Configure ArgoCD with Argo Rollouts to automate a canary deployment, routing 5% of traffic to a new service version and automatically rolling back if error rates exceed 0.5%.
3. **Enforce Automated Architectural Linting**: Integrate an automated architectural linter into a CI pipeline that rejects pull requests violating domain layer separation rules.

---

## 5. Objective Evidence of Capability (What to Inspect in Git)

- [ ] Complete Platform Architecture Blueprint specifying self-service developer workflows and control planes.
- [ ] Production GitOps repository managing multi-cluster Kubernetes deployments declaratively.
- [ ] Published DORA metrics dashboard demonstrating measurable improvements in deployment velocity and change failure rate.

---

## 6. Common Cognitive Gaps & Blind Spots

* **Treating Platform as a Project**: Building an internal platform as a one-off IT project without dedicated product management, user feedback, or ongoing developer empathy.
* **Mandating Golden Cages Instead of Paved Roads**: Forcing developers into rigid, uncustomizable platforms that incentivize "shadow IT" and workarounds.
* **Complex CI/CD Spaghetti**: Writing thousands of lines of unmaintainable Bash scripts in Jenkins/GitLab CI instead of declarative, modular pipeline actions.

---

## 7. Authoritative Repository Links

* DevOps Core: [`09-devops/`](../../09-devops/README.md)
* Platform Strategy Capstone: [`24-architect-mastery/platform-strategy/`](../platform-strategy/README.md)
* Architectural Linters & Tools: [`21-architecture-tools/linters/`](../../21-architecture-tools/linters/README.md)

---

## 8. Diagnostic Assessment Questions

1. *How does an Internal Developer Platform (IDP) differ from traditional DevOps, and what metrics prove its return on investment (ROI)?*
2. *How does GitOps prevent configuration drift between Git and active production Kubernetes clusters?*
3. *What mechanisms should be in place to ensure automated canary rollouts can reliably detect regressions before 100% traffic cutover?*
