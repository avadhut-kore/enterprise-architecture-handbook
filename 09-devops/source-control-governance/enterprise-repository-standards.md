# Enterprise Repository Standards

Unconstrained repository creation results in "Repository Sprawl," orphan codebases, unpatched security vulnerabilities, and zero accountability.

## 1. Mandatory Repository Baseline

Every production enterprise repository must contain:
1. `README.md`: Explaining business purpose, architecture diagram, owning team, and local setup instructions.
2. `CODEOWNERS`: Defining explicit review ownership by domain path.
3. `CONTRIBUTING.md`: PR process, commit conventions, and testing requirements.
4. `SECURITY.md`: Vulnerability disclosure policy and reporting contacts.
5. `.pre-commit-config.yaml`: Pre-commit hooks for secret detection (Gitleaks) and linting.

## 2. Repository Naming Standard

$$\text{[business-domain]}-\text{[capability]}-\text{[component-type]}$$

Examples:
- `billing-invoicing-service` (Backend microservice)
- `claims-portal-frontend` (Web application)
- `shared-terraform-networking` (IaC module)
- `risk-scoring-model` (ML pipeline)

## 3. Repository Lifecycle Management
- **Active**: Actively maintained, passing security scans, deployed to production.
- **Deprecated**: Scheduled for retirement; read-only mode enabled; new PRs blocked.
- **Archived**: Permanently locked, code retained for legal and compliance audit obligations.

## Related Resources
- [GitHub Enterprise Governance](../github/github-enterprise-governance.md)
- [DevSecOps Architecture](../devsecops/README.md)
