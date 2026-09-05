# Software Bill of Materials (SBOM) Architecture

## Executive Summary

A Software Bill of Materials (SBOM) is a complete, nested inventory of all software components, third-party libraries, licenses, and dependencies contained within a software artifact.

---

## 1. Enterprise Standard: CycloneDX
- **Generation**: Automated during CI build using **Syft**:
  `syft packages/order-service:latest -o cyclonedx-json > sbom.json`
- **Cataloging & Instant Discovery**: Upload SBOMs to **Dependency-Track**. When a new zero-day vulnerability (like Log4Shell) is disclosed, the enterprise can search its global SBOM database and identify every affected microservice across 10,000 repositories in **seconds**.
