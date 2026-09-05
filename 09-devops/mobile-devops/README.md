# Mobile DevOps Architecture

Mobile application delivery differs fundamentally from web/cloud backends due to external gatekeepers (Apple App Store, Google Play), immutable installed binaries, and device hardware fragmentation.

## 1. The Mobile Delivery Lifecycle

```
[Mobile Source Commit (Swift / Kotlin / React Native)]
                       │
                       ▼
[Fastlane CI Build Runner (macOS Hardware)]
                       │
                       ▼ 1. Code Signing (Certificates from Vault)
                       ▼ 2. Run Snapshot & Unit Tests
                       ▼ 3. Hermes Bytecode Optimization
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
[BETA TRACK (TestFlight / Play)]  [OTA DELTA BUNDLE (Expo / App Center)]
- Internal QA & Stakeholder dogfood- Instant hotfix for JS/assets
         │                         - Bypasses store review delays
         ▼
[PRODUCTION APP STORE SUBMISSION]
- Phased release rollout (1% -> 2% -> 5% -> 10% -> 100%)
- Real-time crash monitoring (Crashlytics / Sentry)
```

## 2. Invariants for Mobile DevOps
- **Never Store Signing Keys in Repositories**: Store `.p12` certificates and provisioning profiles in HashiCorp Vault or Fastlane Match with encrypted Git backends.
- **Phased Store Releases**: Always utilize 7-day phased rollouts in Apple App Store and staged rollouts in Google Play Console to detect fatal crashes before affecting 100% of users.

## Related Resources
- [Mobile Architecture](../../05-mobile/README.md)
- [React Native Reference Pipeline](../ci-cd/reference-pipelines/react-native-mobile-reference-pipeline.md)
