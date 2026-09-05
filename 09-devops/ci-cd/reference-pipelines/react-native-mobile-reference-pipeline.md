# React Native Cross-Platform Reference Pipeline

Continuous delivery pipeline for cross-platform mobile apps.

## 1. Pipeline Flow
```
[Commit] ──► [JS/TS Unit Tests] ──► [Hermes Bytecode Compilation] ──► [Fastlane Build (iOS/Android)]
                                                                               │
[TestFlight / Internal Play Track] ◄── [CodePush OTA Delta Release] ◄──────────┘
```

## 2. Best Practices
- **Hermes Engine**: Precompile JavaScript into bytecode at build time to eliminate mobile launch latency.
- **Over-The-Air (OTA) Updates**: Deploy non-native JS/asset fixes instantly via App Center / Expo Updates without App Store review delays.

## Related Resources
- [Mobile DevOps](../../mobile-devops/README.md)
- [Mobile Architecture](../../../05-mobile/README.md)
