# Modernization Strategy Selection Guide & Scoring Model

## 1. Quantitative Selection Algorithm

```
Step 1: Calculate Business Differentiation Score (BDS: 1 to 5)
Step 2: Calculate Technical Debt Index (TDI: 1 to 5)
Step 3: Calculate Change Velocity Requirement (CVR: 1 to 5)
Step 4: Calculate Migration Risk Tolerance (MRT: 1 to 5)
```

### Recommendation Mapping Rules
- **If BDS $\le 2$ and Commodity Capability**: Recommend **Replace (SaaS)** or **Retire**.
- **If CVR $\le 2$, TDI $\le 3$, and High Stability**: Recommend **Retain with API Facade**.
- **If Datacenter Deadline $< 6$ months**: Recommend **Rehost** or **Relocate** as Phase 1, followed by Replatforming.
- **If BDS $\ge 4$, CVR $\ge 4$, and TDI $\ge 4$**: Recommend **Rearchitect via Strangler Fig**.
- **If Monolithic Codebase is Maintainable but deployment is slow**: Recommend **Refactor to Modular Monolith**.
