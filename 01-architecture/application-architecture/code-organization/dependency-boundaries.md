# Physical Dependency Boundaries

## 1. Compiler-Enforced Boundaries
Do not rely on developer discipline to avoid calling forbidden layers.
Use separate compiler projects/assemblies:
- The `Domain` project has **0 package dependencies**.
- If a developer tries to call `DbContext` inside `Domain`, the compiler refuses to build because the project reference does not exist.
