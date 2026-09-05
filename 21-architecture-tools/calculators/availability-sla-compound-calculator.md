# Compound Availability SLA Calculator

## Formula
$$\text{System SLA} = \text{SLA}_{\text{CDN}} \times \text{SLA}_{\text{ALB}} \times \text{SLA}_{\text{Compute}} \times \text{SLA}_{\text{Database}}$$

### Worked Example:
- CDN (99.99%) $\times$ ALB (99.99%) $\times$ EKS (99.95%) $\times$ Aurora (99.99%)
- $0.9999 \times 0.9999 \times 0.9995 \times 0.9999 = 0.9992 = \mathbf{99.92\% \text{ Compound Availability}}$
- Total allowed unplanned downtime = **7.01 hours per year** (down from 52 minutes of a single 99.99% component).
