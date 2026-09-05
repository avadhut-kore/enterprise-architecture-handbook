# PCI-DSS v4.0 Integration Architecture Guide

## 1. Overview
This directory details the architectural patterns, network segmentation controls, encryption standards, and compliance checklists required to build, operate, and integrate payment systems compliant with the **Payment Card Industry Data Security Standard (PCI-DSS) version 4.0**.

## 2. Directory Structure
- [scope.md](scope.md): Scoping rules and Cardholder Data Environment (CDE) definition.
- [cardholder-data-environment.md](cardholder-data-environment.md): CDE network topology and isolation.
- [segmentation.md](segmentation.md): Firewall, microsegmentation, and zero-trust segmentation.
- [trust-boundaries.md](trust-boundaries.md): Boundary traversal controls and data flow diagrams.
- [encryption.md](encryption.md): Strong cryptography, AES-256-GCM, and key management.
- [tokenization.md](tokenization.md): Format-preserving tokenization and vault architecture.
- [secrets.md](secrets.md): Secrets management and cryptographic key rotation in CDE.
- [access-control.md](access-control.md): Identity, MFA, and least-privilege RBAC.
- [logging.md](logging.md): Audit logging, sanitization, and immutable WORM storage.
- [monitoring.md](monitoring.md): FIM, IDS/IPS, and 24/7 SIEM monitoring.
- [vulnerability-management.md](vulnerability-management.md): ASV scans, penetration testing, and patch SLAs.
- [third-party-integrations.md](third-party-integrations.md): Service provider governance and AOC management.
- [architecture-checklist.md](architecture-checklist.md): 50-point PCI-DSS v4.0 architecture audit checklist.
- [reference-architecture.md](reference-architecture.md): Zero-scope CDE reference architecture blueprint.
