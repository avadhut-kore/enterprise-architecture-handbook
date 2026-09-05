# Data Breach Forensics & Legal Notification Architecture

## Executive Summary

- **Forensic Evidence Preservation**: Take immediate live memory dumps and disk snapshots of compromised EC2 instances before shutting them down. Store snapshots in a write-only forensics account.
- **Regulatory Notification Timelines**:
  - **GDPR Article 33**: Formal notification to Supervisory Authority within **72 hours** of becoming aware of the breach.
  - **SEC Cybersecurity Disclosure**: Public reporting via Form 8-K within **4 business days** of determining material impact.
