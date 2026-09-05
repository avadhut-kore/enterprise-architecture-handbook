# Mermaid Quadrant Charts & Decision Matrices

Quadrant charts map architectural initiatives, technical debt, and technology options across two competing axes (e.g., Value vs Complexity).

## Technical Debt Remediation Priority Matrix

```mermaid
quadrantChart
    title Technical Debt Remediation Priority Matrix
    x-axis Low Effort --> High Effort
    y-axis Low Business Value --> High Business Value
    quadrant-1 Quick Wins (Do First)
    quadrant-2 Major Projects (Strategic Plan)
    quadrant-3 Low Priority (Defer)
    quadrant-4 Money Pit (Avoid / Reconsider)
    "Upgrade Spring Boot 3": [0.25, 0.75]
    "Migrate Oracle to Aurora": [0.85, 0.90]
    "Adopt OTel SDK": [0.35, 0.80]
    "Rewrite Frontend in Rust": [0.90, 0.15]
    "Clean Stale Feature Flags": [0.15, 0.40]
    "Consolidate Monolith Logging": [0.30, 0.50]
```

## Architectural Guidelines
* Perfect for presenting architecture roadmaps and rationalization decisions to executive sponsors.
