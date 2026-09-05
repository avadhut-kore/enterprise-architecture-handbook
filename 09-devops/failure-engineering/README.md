# DevOps Failure Engineering: 15 Production Breakdown Scenarios

When the delivery platform fails, all feature development halts and emergency hotfixes cannot be deployed. This reference analyzes 15 high-severity DevOps platform failures.

---

### 1. Broken Pipeline Halting Deployment Queue
- **Impact**: 40 engineers blocked from deploying emergency hotfixes during an active production incident.
- **Root Cause**: Breaking change in an unpinned third-party CI action (`uses: actions/setup-node@v3`).
- **Preventive Architecture**: Pin all actions to immutable commit SHAs; maintain local mirror of critical actions.

---

### 2. Corrupted Artifact Deployed to Staging
- **Impact**: Staging services crash loop with missing symbol errors.
- **Root Cause**: Build step produced partial output due to out-of-disk condition on the CI runner host, but exited with status code 0.
- **Preventive Architecture**: Build within strict containerized sandboxes; verify artifact cryptographic checksums before publishing.

---

### 3. Bad Deployment Bypassing Smoke Test
- **Impact**: 500 Internal Server Errors served to 100% of customers on production checkout.
- **Root Cause**: Smoke test script evaluated HTTP 200 on an error page displaying "System Unavailable".
- **Preventive Architecture**: Semantic response assertions (e.g., asserting JSON response body contains `status: ok` and expected payload).

---

### 4. Container Registry Global Outage
- **Impact**: Kubernetes nodes unable to scale horizontally; new pods fail with `ImagePullBackOff`.
- **Root Cause**: Third-party registry DNS failure or authentication rate limiting.
- **Preventive Architecture**: Deploy internal OCI registry mirror (Harbor / Cloudflare cache) with read-through caching in local VPCs.

---

### 5. Git Provider Service Degradation
- **Impact**: CI/CD pipelines cannot checkout code; all deployments paralyzed globally.
- **Root Cause**: DDoS attack or database outage at SaaS Git provider.
- **Preventive Architecture**: Maintain automated cold backup mirrors of critical core repositories on secondary cloud git host.

---

### 6. Secret/Token Expiration in CI Runner
- **Impact**: All deployments to AWS fail at 02:00 UTC with `AccessDenied`.
- **Root Cause**: Static IAM Access Key expired after 90-day rotation deadline without automated alerts.
- **Preventive Architecture**: Eliminate static secrets in favor of OIDC federated authentication with zero expiration maintenance.

---

### 7. TLS Certificate Expiration Sev-1
- **Impact**: Ingress controllers reject external customer traffic with SSL warnings.
- **Root Cause**: Manual renewal tracking spreadsheet missed a wildcard certificate.
- **Preventive Architecture**: Automated certificate lifecycle management via `cert-manager` with Let's Encrypt and Prometheus expiry alerts at 30/14/7 days.

---

### 8. Terraform State Lock Deadlock / State Corruption
- **Impact**: Infrastructure deployments blocked with `Error: Error acquiring the state lock`.
- **Root Cause**: A developer terminated an apply command mid-run, leaving an unreleased DynamoDB lock lease.
- **Preventive Architecture**: Standardized runbook for `terraform force-unlock` combined with CI/CD timeouts and state backup versioning.

---

### 9. Kubernetes Control Plane Unresponsive
- **Impact**: `kubectl` commands time out; pods cannot be rescheduled or autoscaled.
- **Root Cause**: etcd disk IOPS saturation caused by excessive unindexed API server events.
- **Preventive Architecture**: Host etcd on dedicated fast NVMe SSDs; tune event retention to 1 hour and enforce event rate limits.

---

### 10. Misconfigured Ingress Routing Loop
- **Impact**: Incoming HTTP requests bounce between HTTP and HTTPS indefinitely, causing 301 redirect loops.
- **Root Cause**: Ingress controller SSL termination mismatched with upstream CDN header forwarding (`X-Forwarded-Proto`).
- **Preventive Architecture**: Automated synthetic canary testing in pre-release staging; strict ingress linting rules.

---

### 11. DNS Failover Propagation Failure
- **Impact**: Disaster recovery cutover to secondary region ignored by 40% of global users.
- **Root Cause**: Upstream client ISPs caching DNS records ignoring 60-second TTLs.
- **Preventive Architecture**: Use Anycast BGP routing (AWS Global Accelerator / Cloudflare) rather than DNS-based failover.

---

### 12. Cloud Provider Regional Outage
- **Impact**: Entire availability zone goes offline in `us-east-1`.
- **Root Cause**: Power failure or underlying fiber cut in primary cloud datacenter.
- **Preventive Architecture**: Multi-AZ quorum architecture with automated inter-zone pod distribution budgets.

---

### 13. CI Runner Pool Exhaustion Under Burst
- **Impact**: PR build queues delay from 2 minutes to 3 hours during company-wide hackathon.
- **Root Cause**: Static fixed runner pool unable to handle burst demand.
- **Preventive Architecture**: Kubernetes-based autoscaling runners (ARC) scaling dynamically from 2 to 200 pods based on webhook queue depth.

---

### 14. Dependency Registry Outage (npm / PyPI / Maven)
- **Impact**: Builds fail globally with `503 Service Unavailable` downloading public packages.
- **Root Cause**: Public upstream registry downtime or transient network partition.
- **Preventive Architecture**: Enterprise artifact proxy (Artifactory / Nexus) with permanent local caching of all external dependencies.

---

### 15. Security Scanner False Positive Blocking Release
- **Impact**: High-priority hotfix blocked by CI security gate due to false positive in dev dependency.
- **Root Cause**: Rigid "block on all CVEs" policy with no automated exception mechanism.
- **Preventive Architecture**: Scoped `.trivyignore` / policy exceptions signed by designated security champions with mandatory 14-day expiry.

## Related Resources
- [Disaster Recovery](../disaster-recovery/README.md)
- [Red Teaming](../red-team/README.md)
