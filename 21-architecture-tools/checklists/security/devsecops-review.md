# Checklist: DevSecOps Pipeline Review Checklist

## Executive Summary
This checklist establishes the required technical and architectural controls evaluated during formal governance reviews.

---

## Verification Criteria
- [ ] Pre-commit hooks block hardcoded secrets locally (Gitleaks).
- [ ] SAST (Semgrep) and SCA (Snyk) scans execute on every pull request.
- [ ] Pull requests automatically blocked on Critical/High CVEs.
- [ ] Automated CycloneDX SBOM generation active in build pipeline.
- [ ] Container images cryptographically signed via Cosign keyless signing.
