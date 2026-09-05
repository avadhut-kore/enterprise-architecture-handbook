# Security Architecture Diagram Checklist

- [ ] Are security trust boundaries explicitly indicated with dashed perimeter subgraphs?
- [ ] Is Zero Trust enforced: are all inter-service communications authenticated via mTLS?
- [ ] Are user identity tokens (ID tokens) clearly distinguished from resource access tokens (Bearer JWTs)?
- [ ] Is envelope encryption and KMS Customer-Managed Key (CMK) lifecycle documented for sensitive data?
- [ ] Are privileged administrative access paths governed by Just-in-Time (JIT) elevation?
