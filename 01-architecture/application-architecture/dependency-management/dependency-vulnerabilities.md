# Dependency Vulnerability Remediation & SBOM

## 1. Software Bill of Materials (SBOM)

An SBOM provides an authoritative, machine-readable inventory of all components, libraries, and transitive dependencies included in an application binary (CycloneDX or SPDX format).

---

## 2. Automated CVE Triage Matrix

```
+--------------------+-----------------------+---------------------------------------+
| CVSS Score Severity| Response SLA Target   | Action Protocol                       |
+--------------------+-----------------------+---------------------------------------+
| Critical (9.0-10.0)| < 24 Hours            | Emergency hotfix deployment           |
| High (7.0-8.9)     | < 7 Days              | Expedited sprint backlog item         |
| Medium (4.0-6.9)   | Next Release Cycle    | Regular maintenance cadence           |
| Low (0.1-3.9)      | Next Quarterly Cycle  | Batch upgrade                         |
+--------------------+-----------------------+---------------------------------------+
```
