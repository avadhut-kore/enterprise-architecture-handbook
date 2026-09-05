# Master Catalog of 30+ Lethal DevOps Anti-Patterns

Anti-patterns are recurring engineering practices that seem intuitive at first, but systematically result in technical debt, operational fragility, and developer burnout.

## 1. Cultural & Organizational Anti-Patterns
1. **The "DevOps Team" as a Siloed Ticket Queue**: Creating a DevOps team that acts as an intermediary ticket processor, recreating the classic wall of confusion.
2. **Platform Built Without Users**: Platform teams building complex tools in isolation without interviewing internal developers.
3. **The Mandatory Golden Prison**: Enforcing strict golden paths with zero escape hatches for legitimate specialized engineering needs.
4. **Gaming DORA Metrics**: Optimizing deployment frequency by deploying trivial typo fixes rather than business value.
5. **Hero Culture**: Relying on 2 or 3 senior engineers to perform manual weekend deployments and hotfixes.

## 2. CI/CD & Pipeline Anti-Patterns
6. **Rebuilding Artifacts per Environment**: Compiling code separately for Dev, QA, Staging, and Production, invalidating staging test confidence.
7. **Giant Monolithic Pipelines**: 90-minute pipelines running thousands of serial tests without caching or parallelization.
8. **Pipelines with No Automated Tests**: Automated deployments without automated test gates (simply automating bad code delivery).
9. **Poisoned Pipeline Secrets**: Granting pull request workflows write-access to production cloud environments.
10. **Unpinned Pipeline Dependencies**: Using `@latest` or `@v1` tags on third-party actions/plugins that break pipelines unexpectedly.

## 3. Deployment & Release Anti-Patterns
11. **Manual Production Deployments**: Requiring engineers to log into production consoles or SSH into servers to deploy code.
12. **SSH-Driven Deployments**: Deploying code by `git pull` on production servers.
13. **Deploying on Friday Afternoon Without Canaries**: Shipping unverified changes right before weekend operational coverage transitions.
14. **No Rollback Strategy**: Assuming every deployment will succeed and relying exclusively on forward-fixes during outages.
15. **Big-Bang Cutover**: Accumulating 3 months of features and deploying them simultaneously at midnight.

## 4. Infrastructure & Container Anti-Patterns
16. **Kubernetes-First Dogmatism**: Mandating Kubernetes for a 3-engineer team running a simple CRUD application.
17. **Docker-Everything Without Optimization**: 2GB container images running as root containing full Ubuntu desktops and compilers.
18. **Terraform-Everything in a Single State File**: Managing an entire multi-account cloud estate in one giant `terraform.tfstate`.
19. **Ansible as Cloud Provisioner**: Using Ansible for cloud resources that require declarative state tracking and drift detection.
20. **Snowflake Servers**: Hand-crafted virtual machines with unversioned, undocumented configuration edits.

## 5. Security & Governance Anti-Patterns
21. **Secrets in Git**: Checking API keys, private certs, or database passwords into source control.
22. **Long-Lived Cloud Credentials in CI**: Storing permanent AWS Access Keys in repository settings instead of OIDC.
23. **Blocking Everything Security Gate**: Halting production builds on minor, unexploitable upstream CVEs, causing developer fatigue.
24. **No Artifact Provenance or SBOM**: Running container images in production with zero visibility into transitive dependencies.
25. **Shared Production Passwords**: Multiple engineers sharing a single `admin` database or Kubernetes credential.

## 6. Environment & Observability Anti-Patterns
26. **Environment Sprawl**: Maintaining 8 permanent, idle static environments (Dev, QA, UAT, System, Stage, Pre-Prod, Prod).
27. **Environment Configuration Drift**: Staging running different software versions, OS patches, or schema updates than Production.
28. **Noisy Neighbor Shared Clusters**: Hosting CPU-hungry batch jobs on the same Kubernetes cluster as low-latency customer APIs.
29. **Alert Fatigue**: Thousands of un-actionable Datadog alerts firing into Slack channels that engineers silence.
30. **Optimizing Build Speed Over Correctness**: Disabling unit and integration tests to hit arbitrary CI speed targets.

## Related Resources
- [DevOps Foundations](../devops-foundations/README.md)
- [DevOps Decision Frameworks](../decision-frameworks/README.md)
