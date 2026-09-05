# Checklist: Identity Architecture Review Checklist

## Executive Summary
This checklist establishes the required technical and architectural controls evaluated during formal governance reviews.

---

## Verification Criteria
- [ ] Centralized IdP (Entra ID / Okta) serves as Single Source of Truth.
- [ ] FIDO2 / WebAuthn passwordless MFA enforced for interactive users.
- [ ] SCIM 2.0 automated provisioning and instantaneous deprovisioning active.
- [ ] Workload Identity Federation used for 100% of compute pods (zero static keys).
- [ ] JIT privileged role elevation active with peer approval.
