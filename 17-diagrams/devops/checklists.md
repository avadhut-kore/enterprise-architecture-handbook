# DevOps & Continuous Delivery Review Checklist

This checklist provides a structured 25-point evaluation for continuous integration, progressive delivery, and cluster observability.

## 1. CI Pipeline & Quality Gates
- [ ] Are unit tests and linters automated on every pull request, completing in under 5 minutes?
- [ ] Are automated SAST, SCA dependency scanning, and secret leak detection integrated into CI?
- [ ] Are container images cryptographically signed using Cosign/Sigstore with verifiable provenance?
- [ ] Are container images scanned for vulnerabilities, blocking deployment on critical CVEs?

## 2. GitOps & Continuous Deployment
- [ ] Is Git maintained as the single source of truth for all Kubernetes manifests and configuration?
- [ ] Are deployment manifests managed via Helm or Kustomize with environment-specific overrides?
- [ ] Is in-cluster drift detection enabled, automatically reconciling untracked changes back to Git?
- [ ] Are zero-downtime deployment strategies (Canary or Blue-Green) configured for all public APIs?

## 3. Observability & Operational Resilience
- [ ] Is OpenTelemetry SDK integrated across all microservices for unified metrics, logs, and traces?
- [ ] Are W3C Trace Context headers propagated across all HTTP, gRPC, and asynchronous event boundaries?
- [ ] Are automated canary analysis metrics (error rates, p99 latency) configured for automated rollbacks?
- [ ] Are actionable alerts mapped to runbooks with defined escalations and MTTR objectives?
