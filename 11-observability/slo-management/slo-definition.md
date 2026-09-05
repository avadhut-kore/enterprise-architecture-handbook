# Defining Realistic Service Level Objectives (SLOs)

## 1. Executive Summary
Setting an SLO is not a competitive sport where "more nines is always better." Demanding four nines ($99.99\%$) when three nines ($99.9\%$) satisfies users costs **ten times more infrastructure and engineering budget** while throttling feature velocity.

An SLO must be set just above the threshold where **users begin to be unhappy**, leaving maximum room for product experimentation.

---

## 2. The Downtime Mathematics Matrix

Understanding the true time implications of "nines" across operational time windows:

| Target SLO | Allowed Downtime / 30-Day Month | Allowed Downtime / 365-Day Year | Allowed Downtime / 24-Hour Day | Typical Infrastructure Cost Multiplier |
| :--- | :--- | :--- | :--- | :--- |
| **99.0% (Two Nines)** | **7 Hours, 18 Minutes** | 3.65 Days | 14.4 Minutes | $1.0\times$ (Standard multi-AZ) |
| **99.5%** | **3 Hours, 39 Minutes** | 1.83 Days | 7.2 Minutes | $1.5\times$ (Redundant instances) |
| **99.9% (Three Nines)** | **43.8 Minutes** | 8.76 Hours | 1.44 Minutes | **$3.0\times$ (High-availability failover)** |
| **99.95%** | **21.9 Minutes** | 4.38 Hours | 43.2 Seconds | $5.0\times$ (Automated sub-minute failover) |
| **99.99% (Four Nines)** | **4.38 Minutes** | 52.6 Minutes | 8.64 Seconds | **$10.0\times$ (Active-Active multi-region)** |
| **99.999% (Five Nines)**| **26.3 Seconds** | 5.26 Minutes | 0.86 Seconds | **$25.0\times+$ (Telco/Mainframe grade)** |

---

## 3. The Downstream Dependency Ceiling Rule

A service cannot be more reliable than the mathematical product of its critical synchronous dependencies:

$$\text{SLO}_{\text{service}} \le \prod_{i=1}^{N} \text{SLO}_{\text{dependency } i}$$

### Concrete Example
- If Service A calls:
  - AWS US-East-1 RDS (99.95% SLA)
  - Stripe Payment API (99.9% SLA)
  - Cloudflare CDN (99.99% SLA)
- Maximum Theoretical Composite Availability:
  $$\text{SLO}_{\max} = 0.9995 \times 0.9990 \times 0.9999 = 0.9984 \text{ (99.84\%)}$$
- **Architectural Reality**: Service A **cannot promise 99.99% availability** to its users unless calls to Stripe and RDS are made asynchronous or protected by local fallback caches!
