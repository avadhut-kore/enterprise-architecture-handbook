# The 15-Stage Monolith Decomposition Playbook

## 1. End-to-End Production Lifecycle

```
Phase 1: Discovery & Baseline
  1. Profile Technical & Business Drivers
  2. Map Monolithic Dependencies & Hotspots
  3. Identify Bounded Contexts & Architectural Seams

Phase 2: Preparation & Boundary Hardening
  4. Implement Ingress API Routing Facade
  5. Refactor Module Boundaries Internally (Modular Monolith)
  6. Deploy Comprehensive Observability & Baselines

Phase 3: Extraction & Data Separation
  7. Deploy Anti-Corruption Layer (ACL)
  8. Extract Target Domain Service Code
  9. Establish Data Ownership & Split Schema
  10. Replicate & Hydrate Data via Log-Based CDC

Phase 4: Validation & Cutover
  11. Shadow Run (Dark Launch) with Live Traffic
  12. Reconcile Cross-System Data Parity
  13. Progressive Canary Traffic Cutover
  14. Stabilize & Monitor Distributed Metrics

Phase 5: Retirement
  15. Prune Extracted Code from Monolith & Decommission
```

---

## 2. Execution Runbook Highlights

### Stage 4: The Ingress Facade
Deploy an API Gateway (Envoy, Kong) in front of the monolith *before* extracting any service. Configure routing rules mapping paths (`/api/v1/orders/*`) so traffic can be dynamically shifted between legacy and modern endpoints with zero client changes.

### Stage 7: The Anti-Corruption Layer
Wrap calls between the new service and the legacy monolith in an ACL. Translate legacy IDs and nested structures into clean domain models.

### Stage 11: Dark Launching
Route 100% of read traffic to the new service asynchronously, comparing responses against the legacy monolith output using automated diff tools (Diffy, Envoy Shadowing).
