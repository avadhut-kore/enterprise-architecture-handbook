# Application Coupling & Architectural Metrics

## 1. Measuring Coupling: Robert C. Martin's Package Metrics

```
+-----------------------------------+----------------------------------------+
| Metric                            | Mathematical Formulation               |
+-----------------------------------+----------------------------------------+
| Afferent Coupling ($C_a$)         | Number of outside classes that depend   |
| (Incoming dependencies)           | on classes inside this package.        |
+-----------------------------------+----------------------------------------+
| Efferent Coupling ($C_e$)         | Number of classes inside this package  |
| (Outgoing dependencies)           | that depend on outside classes.        |
+-----------------------------------+----------------------------------------+
| Instability ($I$)                 | $I = \frac{C_e}{C_a + C_e}$            |
| (0 = Maximally stable, 1 = Unstable)|                                      |
+-----------------------------------+----------------------------------------+
| Abstractness ($A$)                | $A = \frac{N_a}{N_c}$ (Interfaces/Total)|
+-----------------------------------+----------------------------------------+
```

---

## 2. The Main Sequence: Balance of Stability and Abstractness

$$D = |A + I - 1|$$
- **Zone of Pain ($A=0, I=0$)**: Highly concrete, highly stable (e.g., legacy shared database schema). Rigid, difficult to modify because many callers depend on it.
- **Zone of Uselessness ($A=1, I=1$)**: Highly abstract, highly unstable (interfaces that nobody uses).
- **Target**: Stay close to the Main Sequence ($A + I \approx 1$). Stable components must be abstract; concrete components should be volatile.
