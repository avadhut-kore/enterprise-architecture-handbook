# PCI-DSS v4.0 Architecture Review Checklist

## Scoping & Segmentation
- [ ] Has the CDE boundary been formally verified via bi-annual segmentation penetration tests?
- [ ] Are all out-of-scope networks strictly isolated by stateful firewalls?
- [ ] Are ingress and egress traffic restricted to explicit IP/port whitelists?

## Cardholder Data Protection
- [ ] Is Sensitive Authentication Data (CVV, PIN) purged immediately after authorization?
- [ ] Are all stored PANs encrypted using AES-256-GCM with keys managed in an HSM?
- [ ] Are hosted fields or tokenization used to prevent raw PAN ingestion on application servers?

## Access Control & Logging
- [ ] Is MFA enforced for all administrative and remote access into the CDE?
- [ ] Are all card access events and privilege elevations logged to an immutable WORM store?
- [ ] Are log sanitizers actively stripping credit card numbers from stdout/stderr?
