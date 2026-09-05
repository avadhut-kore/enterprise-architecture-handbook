# Enterprise Integration Security Review Checklist

## Architecture & Boundary Controls
- [ ] Are all external-to-internal boundaries mediated by an API Gateway and Web Application Firewall?
- [ ] Is mutual TLS (mTLS) with TLS 1.3 enforced on all partner and core-banking integrations?
- [ ] Are internal microservices prohibited from directly connecting to external internet endpoints?

## Identity & Access Control
- [ ] Are machine-to-machine integrations using short-lived OAuth 2.0 client credentials tokens ($\le 15$ min)?
- [ ] Is fine-grained authorization (ABAC / OPA) decoupled from application business logic?
- [ ] Are service accounts restricted to the absolute least privilege with no wildcard permissions?

## Data Protection & Privacy
- [ ] Are sensitive fields (PAN, SSN, PHI) tokenized or encrypted with envelope encryption prior to queue storage?
- [ ] Are sensitive credentials eliminated from git, docker images, and environment variables?
- [ ] Is payload data minimization enforced at the ingress adapter?

## Observability & Audit
- [ ] Does every cross-system request carry an immutable correlation ID?
- [ ] Are all authorization rejections and validation errors streamed to the enterprise SIEM?
- [ ] Are certificate expiration metrics exported and alerted on?
