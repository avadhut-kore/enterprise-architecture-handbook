# Software Supply Chain Security (`supply-chain-security/`)

## Executive Summary

Modern software supply chain attacks (e.g., SolarWinds, Log4j, Codecov) compromise software dependencies, build environments, or artifact registries to inject malicious code into trusted software distributions.

---

## Key Guides in this Directory

| Guide | Scope | Core Focus |
| :--- | :--- | :--- |
| [`software-supply-chain-architecture.md`](software-supply-chain-architecture.md) | Threat Landscape | Supply chain attack vectors and architectural defenses |
| [`sbom-generation-and-management.md`](sbom-generation-and-management.md) | Software Bill of Materials | CycloneDX, SPDX, automated ingestion and dependency tracking |
| [`slsa-framework-levels-1-to-4.md`](slsa-framework-levels-1-to-4.md) | Build Provenance | Supply-chain Levels for Software Artifacts (SLSA) |
| [`dependency-pinning-and-private-registries.md`](dependency-pinning-and-private-registries.md) | Package Governance | Artifactory proxying, hash verification, dependency confusion |
