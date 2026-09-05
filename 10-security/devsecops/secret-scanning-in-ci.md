# Secret Scanning in CI/CD & Push Protection

## Executive Summary

Preventing secrets from entering Git requires multi-layered scanning:
1. **Developer Workstation (Shift-Left)**: Pre-commit git hooks using **Gitleaks** evaluate diffs locally before commits are created.
2. **Repository Server (Push Protection)**: GitHub Secret Scanning / GitLab Push Rules inspect git push payloads; if a known high-entropy token pattern is detected, the push is rejected over SSH/HTTPS.
