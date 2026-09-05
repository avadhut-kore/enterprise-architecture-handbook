# AI Modernization Guardrails & Lethal Pitfalls

## 1. The Hallucinated Modernization Trap

A common failure in AI modernization is assuming an LLM's translation is functionally correct because it compiles cleanly and passes basic syntax checks.

### Lethal Failure Modes
1. **Fixed-Point Precision Distortions**: COBOL `COMP-3` packed decimals handle exact currency mathematics down to the fraction of a cent. Converting this naively to standard IEEE 754 floating-point (`double`) in Java or Python introduces rounding drift that corrupts financial balance sheets.
2. **Silent Business Rule Deletion**: When an LLM refactors complex nested 500-line `IF-ELSE` structures, it frequently "cleans up" edge-case branches that represent critical, undocumented legal compliance rules.
3. **Hallucinated Library APIs**: The model calls non-existent methods on modern target frameworks, resulting in runtime runtime exceptions.
