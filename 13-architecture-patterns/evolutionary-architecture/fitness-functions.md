# Production Architectural Fitness Functions Catalog

## 1. Catalog of Automated Architectural Constraints

| Architectural Dimension | Metric / Constraint | Automated Fitness Function Implementation |
| :--- | :--- | :--- |
| **API Latency SLA** | P99 latency $< 800\text{ms}$ under 500 concurrent users. | Automated k6 load test gate in staging CI/CD pipeline. |
| **Code Modularity** | Bounded context A must never import package B directly. | ArchUnit (Java), NetArchTest (.NET), Dependency-Cruiser (Node.js). |
| **AI Token Cost Ceiling** | Average cost per task must remain $< \$0.05$. | Automated evaluation test suite tracking token counts in pull requests. |
| **RAG Faithfulness** | Groundedness score must be $\ge 0.95$. | DeepEval / Ragas test suite executing against 200 golden questions. |
| **Security Secrets** | Zero plaintext secrets or API keys in source code. | Gitleaks / Trufflehog pre-commit hooks and CI scanner. |
| **Vulnerability SLA** | Zero critical/high CVEs in base container images. | Trivy container vulnerability scanner failing builds on high CVEs. |
| **Cloud FinOps Budget** | Monthly infrastructure spend drift $< 10\%$. | Infracost analyzing Terraform pull request diffs. |
