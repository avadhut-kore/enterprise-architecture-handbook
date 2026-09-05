# Evaluation-Driven Development & CI/CD Deployment Gates

## 1. The Gated Pull Request Pipeline

Just as software engineers write unit tests before merging code, AI engineers practice **Evaluation-Driven Development (EDD)**:

```mermaid
flowchart LR
    Commit["Git Commit: Updated prompt.yaml"] --> GitHubAction["GitHub Actions Runner"]
    GitHubAction --> ExecuteEval["Run DeepEval / Ragas Suite (500 test cases)"]
    ExecuteEval --> AssertMetric{"Assert Non-Negotiable Thresholds"}
    
    AssertMetric -->|Faithfulness < 0.95| Fail["FAIL BUILD: Hallucination regression detected!"]
    AssertMetric -->|Relevance < 0.88| Fail2["FAIL BUILD: Relevance dropped!"]
    AssertMetric -->|All Thresholds Met| Pass["PASS BUILD: Automatically approve PR"]
```

---

## 2. Invariant: Cost and Time Ceilings in CI
Running 500 test cases against frontier models on every git commit costs money and takes time. 
* **Per-Commit Gate (PR Fast Check)**: Run 50 core smoke tests using fast SLMs (execution time $< 90\text{ seconds}$, cost $< \$0.25$).
* **Nightly / Pre-Release Gate**: Run the full 1,000+ golden benchmark suite across the production candidate model before deploying to production.
