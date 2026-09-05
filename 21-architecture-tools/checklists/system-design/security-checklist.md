# System Design Checklist: Security & Threat Modeling

## 1. Perimeter & Transport
- [ ] TLS 1.3 enforced for all inbound external traffic?
- [ ] mTLS (Mutual TLS) enforced for internal service-to-service communication?
- [ ] Web Application Firewall (WAF) active with OWASP Top 10 blocking rules?
- [ ] DDoS mitigation active at the DNS and CDN edge layer?

## 2. Authentication & Data Protection
- [ ] OAuth 2.0 / OIDC JWT tokens verified cryptographically at the gateway?
- [ ] Role-Based Access Control (RBAC) enforced at the domain service layer?
- [ ] Sensitive data (PII, tokens) encrypted at rest using AES-256 and envelope encryption?
- [ ] Secrets managed via dedicated secret stores (HashiCorp Vault, AWS Secrets Manager)?
