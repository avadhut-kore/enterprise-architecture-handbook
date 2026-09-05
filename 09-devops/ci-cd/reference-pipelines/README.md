# Reference CI/CD Pipelines Catalog

Standardized, production-grade reference pipeline blueprints across major enterprise programming languages, frameworks, and repository models.

## Catalog Index

| Architecture / Platform | Key Characteristics | Specification Link |
| :--- | :--- | :--- |
| **.NET 8/9** | NuGet restore, dotnet test, SonarQube, Chiseled Ubuntu container | [dotnet-reference-pipeline.md](./dotnet-reference-pipeline.md) |
| **Java 21 / Spring 3** | Maven/Gradle daemon, ArchUnit, Testcontainers, Jib distroless | [java-reference-pipeline.md](./java-reference-pipeline.md) |
| **Python FastAPI/Django** | Poetry, Ruff, mypy, pytest-xdist, distroless Python | [python-reference-pipeline.md](./python-reference-pipeline.md) |
| **Node.js / TypeScript** | pnpm, Turborepo, ESLint, Vitest, multi-stage Node distroless | [nodejs-typescript-reference-pipeline.md](./nodejs-typescript-reference-pipeline.md) |
| **React / Next.js** | Server Components build, bundle analyzer, edge CDN deployment | [react-frontend-reference-pipeline.md](./react-frontend-reference-pipeline.md) |
| **Angular / Nx** | Enterprise Nx affected build, SSR compilation, CDN push | [angular-frontend-reference-pipeline.md](./angular-frontend-reference-pipeline.md) |
| **React Native** | Fastlane, Hermes bytecode, OTA update bundle, TestFlight | [react-native-mobile-reference-pipeline.md](./react-native-mobile-reference-pipeline.md) |
| **Native Mobile** | iOS Xcode Cloud / Android Gradle signing, keystore Vault | [mobile-native-reference-pipeline.md](./mobile-native-reference-pipeline.md) |
| **Monorepo** | Graph calculation, affected projects, remote build cache | [monorepo-reference-pipeline.md](./monorepo-reference-pipeline.md) |
| **Polyrepo** | Shared pipeline inheritance, cross-repo dependency triggers | [polyrepo-reference-pipeline.md](./polyrepo-reference-pipeline.md) |
