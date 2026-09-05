# Branch Protection and GitHub Environments

Branch protection rules and environment gates prevent untested, vulnerable, or unauthorized code from entering production systems.

## 1. Production Branch Protection Standards (`main`)

- [x] **Require pull request before merging** (Minimum 1 approving review from designated CODEOWNERS).
- [x] **Dismiss stale pull request approvals** when new commits are pushed.
- [x] **Require status checks to pass before merging** (Strict mode: branch must be up-to-date with `main`):
  - `build-and-test`
  - `security-sast-scan`
  - `dependency-vulnerability-check`
- [x] **Require signed commits** (Enforce cryptographically verified GPG/SSH signatures).
- [x] **Include administrators** (Prevent tech leads from bypassing checks during crunch periods).
- [x] **Do not allow force pushes** and **do not allow deletions**.

## 2. GitHub Environments & Deployment Gates
Environments (`staging`, `production`) allow scoped configuration and deployment protection:
- **Required Reviewers**: Deployments to `production` require approval from on-call release engineers or product leads.
- **Deployment Branches**: Restrict production deployments exclusively to the `main` branch.
- **Environment Secrets**: Database passwords and production API keys are strictly inaccessible to pull request CI runs.

## Related Resources
- [GitHub Enterprise Governance](./github-enterprise-governance.md)
- [Production Readiness Review](../production-readiness/README.md)
