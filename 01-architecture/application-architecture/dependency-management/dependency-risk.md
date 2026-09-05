# Dependency Risk & Supply Chain Defense

## 1. Supply Chain Attack Vectors

- **Typosquatting**: Malicious actors publish look-alike packages (e.g., `cross-env` vs `crossenv`).
- **Account Takeover**: Maintainer credentials compromised; malicious versions pushed to public registries (npm, PyPI, NuGet).
- **Protestware / Self-Sabotage**: Maintainers introducing breaking changes or destructive code.

---

## 2. Enterprise Defenses

- **Private Artifact Proxies**: Mirror packages in internal registries (Nexus, Artifactory); require approval gates.
- **Lockfiles**: Always commit lockfiles (`package-lock.json`, `poetry.lock`) to ensure cryptographic hash validation of all builds.
