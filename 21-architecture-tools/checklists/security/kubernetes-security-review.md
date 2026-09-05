# Checklist: Kubernetes Security Review Checklist

## Executive Summary
This checklist establishes the required technical and architectural controls evaluated during formal governance reviews.

---

## Verification Criteria
- [ ] Pod Security Standards (`restricted`) enforced at namespace level.
- [ ] Containers execute as unprivileged non-root users (UID 10001).
- [ ] Container root filesystems configured as read-only.
- [ ] Default-deny NetworkPolicies block unrestricted east-west traffic.
- [ ] Secrets injected dynamically via External Secrets Operator.
