# Native Mobile (iOS & Android) Reference Pipeline

CI/CD architecture for native Swift/Kotlin applications with cryptographic signing.

## 1. Pipeline Flow
```
[Commit] ──► [Fetch Certificates from Vault] ──► [Xcodebuild / Gradle Assemble] ──► [Robo / Snapshot Tests]
                                                                                              │
[App Store / Play Console Production Submission] ◄── [Fastlane Deliver to Beta Track] ◄──────┘
```

## 2. Secret & Signing Governance
- **Zero Raw Certificates in Git**: Store iOS Distribution Certificates and Android Keystores in HashiCorp Vault or AWS Secrets Manager.
- **Fastlane Match**: Git-backed encrypted certificate synchronization with GPG passphrase stored in enterprise secret manager.

## Related Resources
- [Mobile DevOps](../../mobile-devops/README.md)
- [Reference Pipelines Catalog](./README.md)
