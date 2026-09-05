# Secrets Management Anti-Patterns

## Executive Summary

1. **Secrets Committed to Version Control (Git)**:
   - *Threat*: Git repositories are duplicated across developer workstations and CI servers. Even if deleted, secrets remain in Git history.
   - *Mitigation*: Enforce pre-commit hooks (TruffleHog / Gitleaks) that block commits containing high-entropy strings or secret formats.
2. **Secrets Passed as Container Environment Variables**:
   - *Threat*: Environment variables are logged in crash dumps, inspectable via `docker inspect`, and inherited by child processes.
   - *Mitigation*: Mount secrets as in-memory `tmpfs` volume files (`/var/run/secrets`).
3. **Shared Production Credentials**:
   - *Threat*: Team members share a single `admin` password; audit trails are non-existent.
   - *Mitigation*: Mandate individual SSO with Just-in-Time elevation.
