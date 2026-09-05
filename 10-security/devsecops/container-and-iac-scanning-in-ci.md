# Automated Container & IaC Scanning in CI

## Executive Summary

Container and IaC security checks execute automatically on every pull request using standardized GitHub Actions / GitLab CI templates:
- **Checkov**: Validates Terraform against 1,000+ CIS and security benchmark policies.
- **Trivy**: Scans compiled Docker images for OS and application package vulnerabilities.
