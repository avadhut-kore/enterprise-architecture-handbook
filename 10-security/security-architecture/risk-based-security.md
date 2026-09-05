# Risk-Based Security Architecture & Economics

## Executive Summary

Security controls are not free: they introduce infrastructure costs, latency overhead, developer friction, and operational complexity. **Risk-Based Security Architecture** uses quantitative economic modeling to determine which security controls justify their implementation costs.

---

## 1. Quantitative Risk Sizing Formulas

$$\text{Single Loss Expectancy (SLE)} = \text{Asset Value (\$)} \times \text{Exposure Factor (\%)} $$

$$\text{Annualized Loss Expectancy (ALE)} = \text{SLE} \times \text{Annualized Rate of Occurrence (ARO)}$$

$$\text{Cost-Benefit Analysis (CBA)} = \text{ALE}_{\text{Before Control}} - \text{ALE}_{\text{After Control}} - \text{Annual Cost of Control}$$

### Worked Example:
- **Asset**: Customer Credit Card Database (\$20,000,000 business value).
- **Threat**: SQL Injection leading to data breach.
- **Exposure Factor (EF)**: 40% (compromise of database records).
  $$\text{SLE} = \$20,000,000 \times 0.40 = \$8,000,000$$
- **ARO without WAF/Tokenization**: 0.1 (once every 10 years).
  $$\text{ALE}_{\text{Before}} = \$8,000,000 \times 0.1 = \$800,000/\text{year}$$
- **Control**: Implement AWS WAF + Field-Level Tokenization (Annual Cost: \$60,000/year).
- **ARO with Control**: 0.005 (once every 200 years).
  $$\text{ALE}_{\text{After}} = \$8,000,000 \times 0.005 = \$40,000/\text{year}$$
- **Net Annual Benefit**:
  $$\text{CBA} = \$800,000 - \$40,000 - \$60,000 = \mathbf{\$700,000/\text{year saved}} \implies \text{Mandated Architecture Control.}$$
