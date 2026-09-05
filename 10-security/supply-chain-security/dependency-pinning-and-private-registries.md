# Dependency Pinning & Dependency Confusion Defense

## Executive Summary

1. **Strict Dependency Pinning**: Never use dynamic ranges (`^1.2.0` or `1.x`) in production manifests. Mandate exact version pinning (`1.2.4`) paired with cryptographic package hash locking (`package-lock.json`, `poetry.lock`).
2. **Dependency Confusion Defense**: Prevent public package registries (npm, PyPI) from overriding internal private corporate packages by reserving internal namespace scopes (`@company/package`) and configuring enterprise proxy registries (JFrog Artifactory) to route private scopes strictly to internal repositories.
