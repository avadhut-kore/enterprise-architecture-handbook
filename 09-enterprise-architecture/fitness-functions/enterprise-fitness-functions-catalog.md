# Enterprise Architectural Fitness Functions Catalog

Automating architecture governance through code: replacing manual review checklists with automated CI/CD policy gates.

---

## 1. The 10 Core Enterprise Fitness Functions

### Fitness Function 1: Zero Unsupported Production Runtimes
* **Target**: Block any deployment whose runtime or OS is listed as "Retire" in the Technology Portfolio.
* **Enforcement**: Trivy / Snyk scan in GitHub Actions blocks build if base container uses deprecated image.

### Fitness Function 2: Mandatory System Ownership
* **Target**: No production microservice without an assigned technical owner and business unit.
* **Enforcement**: Kubernetes admission controller (OPA Gatekeeper) rejects pods lacking `owner.team` and `owner.email` labels.

### Fitness Function 3: Mandatory Disaster Recovery SLA Tagging
* **Target**: Every database and cloud storage bucket must have explicit RTO and RPO backup policies.
* **Enforcement**: AWS Conformance Pack / Terraform Sentinel blocks bucket creation lacking `BackupPolicy` tags.

### Fitness Function 4: Strict API Backward Compatibility
* **Target**: No breaking changes permitted on public production APIs.
* **Enforcement**: OpenAPI / Protobuf linter (Buf / Spectral) in PR pipeline compares against main branch; blocks field deletions.

### Fitness Function 5: Data Sensitivity Classification
* **Target**: Every database schema table containing PII or financial data must be explicitly labeled.
* **Enforcement**: Data catalog scanner flags unlabeled SQL migrations during CI test run.

### Fitness Function 6: Mandatory Distributed Tracing Propagation
* **Target**: Every microservice must propagate W3C TraceContext headers.
* **Enforcement**: Chaos testing pipeline injects synthetic requests; fails build if span hierarchy breaks.

### Fitness Function 7: AI Use-Case Risk Registration
* **Target**: No application may call enterprise AI models without a registered EU AI Act risk tier in the AI Gateway.
* **Enforcement**: Enterprise AI Gateway rejects requests lacking an authorized `X-Enterprise-UseCase-ID` header.

### Fitness Function 8: Architecture Exception Hard Expiration
* **Target**: No temporary architecture waiver remains active beyond 365 days.
* **Enforcement**: Automated nightly script in enterprise repo flags expired exceptions in Jira and notifies Chief Architect.

### Fitness Function 9: Banned Dependency Vulnerability Gate
* **Target**: Zero Critical or High CVEs permitted in production artifacts.
* **Enforcement**: Snyk / Dependabot blocks docker image build if CVE CVSS score > 7.0.

### Fitness Function 10: FinOps Resource Tagging Compliance
* **Target**: 100% of cloud resources must have `CostCenter` and `ApplicationID` tags.
* **Enforcement**: AWS SCP (Service Control Policy) prevents launching EC2/RDS instances without required tags.
