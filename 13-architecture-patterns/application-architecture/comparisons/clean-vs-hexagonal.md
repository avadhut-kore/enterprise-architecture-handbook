# Architectural Comparison: Clean Architecture vs Hexagonal (Ports & Adapters)

## 1. Executive Trade-Off Summary
Clean Architecture emphasizes concentric use-case layers; Hexagonal focuses on symmetrical Primary (Driving) and Secondary (Driven) ports.

---

## 2. Structural Comparison Matrix

```
+--------------------------+---------------------------------+---------------------------------+
| Dimension                | Approach A                      | Approach B                      |
+--------------------------+---------------------------------+---------------------------------+
| Primary Dependency Flow  | Direct or Horizontal            | Inverted / Feature-Isolated     |
| Boilerplate Overhead     | Lower initial ceremony          | Higher mapping and interfaces   |
| Refactoring Agility      | High risk of boundary leakage   | Safe, modular boundary changes  |
| Team Cognitive Load      | Familiar to beginners           | Requires architectural maturity |
+--------------------------+---------------------------------+---------------------------------+
```

---

## 3. Decision Framework for Architects
Evaluate based on:
1. **Domain Complexity**: High domain rules demand inverted/clean architectures.
2. **Team Scale**: Multi-team monolithic codebases require Modular Monolith or Vertical Slice.
3. **Operational Maturity**: Do not adopt distributed microservices until a Modular Monolith's boundaries are rigorously tested.
