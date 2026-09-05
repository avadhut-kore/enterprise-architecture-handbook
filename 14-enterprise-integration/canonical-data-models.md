# Canonical Data Models (CDM): Architectural Trade-Offs

## 1. Conceptual Comparison

```text
Point-to-Point (O(N^2) Mappings)             Canonical Model (O(N) Mappings)
+-----+         +-----+                     +-----+         +-----+
| Sys |<------->| Sys |                     | Sys |-------->|     |
|  A  |         |  B  |                     |  A  |<--------|     |
+-----+         +-----+                     +-----+         | Can |
   ^   \       /   ^                                        | oni |
   |    \     /    |                                        | cal |
   |     v   v     |                        +-----+         |     |
+-----+         +-----+                     | Sys |-------->| Mod |
| Sys |<------->| Sys |                     |  B  |<--------| el  |
|  C  |         |  D  |                     +-----+         +-----+
+-----+         +-----+                                        ^
                                            +-----+            |
                                            | Sys |------------+
                                            |  C  |<-----------+
                                            +-----+
```

---

## 2. Trade-Off Analysis

| Dimension | Point-to-Point Integration | Canonical Data Model (Enterprise-Wide) | Bounded Context Canonical Model (Recommended) |
|---|---|---|---|
| **Mapping Complexity** | $O(N^2)$ — Becomes unmaintainable past 5 systems. | $O(N)$ — Each system maps once into the canonical schema. | $O(N)$ within a specific domain (e.g., Payments or Claims). |
| **Governance Overhead** | Zero centralized governance; high localized friction. | Extreme friction; committee required for any field modification. | High agility; managed by dedicated domain architecture team. |
| **Performance / CPU** | Minimal; transformations tailored directly to target. | High transformation tax; double-serialization on every hop. | Balanced; applied only where protocol heterogeneity requires it. |
| **Semantic Fidelity** | Preserves exact source semantics without compromise. | Forces compromises; collapses rich source semantics into generic fields. | Preserves domain-specific richness within its bounded context. |

> [!IMPORTANT]
> **Architectural Recommendation**: Never attempt an all-encompassing "Enterprise Canonical Data Model". Define canonical schemas strictly within specific business domains (such as standardizing ISO 20022 across corporate payment channels or FHIR across clinical EHRs).
