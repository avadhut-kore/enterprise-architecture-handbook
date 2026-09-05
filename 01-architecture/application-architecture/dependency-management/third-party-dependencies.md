# Third-Party Dependencies: Selection & Vetting

## 1. The Architectural Vetting Framework

Before introducing an open-source library into an enterprise system, evaluate:

```
+--------------------------+-------------------------------------------------+
| Evaluation Vector        | Vetting Criteria                                |
+--------------------------+-------------------------------------------------+
| License Compatibility    | MIT, Apache 2.0, BSD (Permitted)                |
|                          | GPL, AGPL (Restricted / Prohibited for SaaS)    |
+--------------------------+-------------------------------------------------+
| Project Health & Churn   | Multiple active maintainers, regular releases,  |
|                          | low open issue ratio, backing foundation        |
+--------------------------+-------------------------------------------------+
| Transitive Dependencies  | Avoid libraries that pull 200 secondary packages|
+--------------------------+-------------------------------------------------+
| Security History         | Known CVE frequency and response velocity       |
+--------------------------+-------------------------------------------------+
```
