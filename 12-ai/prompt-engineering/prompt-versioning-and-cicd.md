# Prompt Versioning & CI/CD Deployment Pipelines

## 1. Semantic Versioning (SemVer) for Prompts

Prompts must follow semantic versioning conventions to communicate impact to consuming microservices:
* **MAJOR (v2.0.0)**: Breaking output schema changes, major behavioral role alterations, or modified mandatory variable placeholders.
* **MINOR (v1.2.0)**: Added few-shot examples, improved phrasing that enhances accuracy without altering expected output structure.
* **PATCH (v1.1.1)**: Typo fixes, minor formatting adjustments, or defensive delimiter hardening.

---

## 2. The Automated Prompt CI/CD Pipeline

```mermaid
flowchart TD
    Dev["Developer modifies prompt.yaml"] --> PR["Create Git Pull Request"]
    PR --> CI["GitHub Actions / GitLab CI Triggered"]
    
    subgraph QualityGates ["Automated Quality Gates"]
        Linter["1. YAML & Variable Schema Linting"] --> Eval["2. Golden Set Benchmark Execution (200 test cases)"]
        Eval --> Judge["3. LLM-as-a-Judge Evaluation"]
        Judge --> Assert{"Score Thresholds Met?\n- Accuracy >= 92%\n- Hallucination <= 1%\n- Token Count <= Budget"}
    end

    CI --> QualityGates
    Assert -->|Pass| Merge["Merge PR & Deploy to Staging Registry"]
    Assert -->|Fail| Reject["Block PR & Emit Failure Report"]
```
