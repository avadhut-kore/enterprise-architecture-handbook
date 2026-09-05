# React Native Architecture: React Native Performance Optimization

## 1. Architectural Purpose & Problem Context
FlashList virtualization, image caching (react-native-fast-image), and Hermes profiling.

---

## 2. Runtime Mechanics & Bridge/JSI Architecture

```mermaid
flowchart LR
    JS[JavaScript / Hermes Thread] <-->|JSI C++ Direct Memory| Native[Host Native Platform iOS / Android]
    JS --> Fabric[Fabric Renderer]
    Fabric --> NativeUI[Native UI Views]
```

---

## 3. Production Invariants & Best Practices
- Avoid serializing massive JSON strings across the native bridge; use JSI / TurboModules for direct C++ memory binding.
- Store sensitive tokens in iOS Keychain / Android Keystore via `react-native-keychain`; never use `AsyncStorage` for credentials.
