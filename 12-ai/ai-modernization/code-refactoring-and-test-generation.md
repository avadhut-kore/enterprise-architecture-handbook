# Automated Code Refactoring & Synthetic Test Generation

## 1. The Characterization Test Strategy

When modernizing legacy systems, documentation is frequently absent or outdated. The legacy source code itself is the only authoritative specification.

```mermaid
flowchart LR
    LegacyFunc["Legacy Function\n(e.g., COBOL calculate_interest)"] --> TestGen["Test Generation Agent (LLM)"]
    TestGen --> BoundaryTests["Generate 50 Boundary & Edge-Case Inputs"]
    
    BoundaryTests --> RunLegacy["Execute Inputs against Compiled Legacy Binary"]
    RunLegacy --> GroundTruth[("Capture Exact Actual Outputs (Gold Standard)")]
    
    GroundTruth --> ModernFunc["Execute Same Inputs against Modern Refactored Function"]
    ModernFunc --> DiffAssert{"Assert Output Parity (Tolerance = 0.0)"}
    DiffAssert -->|100% Match| Certified["Certified for Migration"]
    DiffAssert -->|Mismatch| Debug["Flag Bug to Engineer"]
```
