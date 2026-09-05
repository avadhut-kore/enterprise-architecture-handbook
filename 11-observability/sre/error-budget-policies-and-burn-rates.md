# Error Budget Policies & Multi-Window Burn-Rate Alerting

## Executive Summary

Simple threshold alerts (e.g., "Page SRE if error rate $> 1\%$ for 5 minutes") cause extreme alert fatigue during transient network blips and miss slow, catastrophic leaks. **Multi-Window Multi-Burn-Rate Alerting** pages engineers based on how rapidly the Error Budget is being depleted.

---

## 1. Burn Rate Calculation
$$\text{Burn Rate} = \frac{\text{Observed Error Rate}}{1 - \text{SLO Target}}$$
- **Burn Rate 1**: Consumes 100% of the 30-day budget in exactly 30 days (Normal operational limit).
- **Burn Rate 14.4**: Consumes 100% of the 30-day budget in **2 days** (2% of budget consumed per hour).

---

## 2. Google SRE Multi-Window Alerting Standard

| Severity | Burn Rate | Short Window | Long Window | Budget Consumed | Paging Action |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Page (SEV-1)** | **14.4x** | 5 minutes | 1 hour | 2% in 1 hour | **Page On-Call Immediately** (Wake up SRE) |
| **Page (SEV-2)** | **6.0x** | 30 minutes | 6 hours | 5% in 6 hours | **Page On-Call Immediately** |
| **Ticket (SEV-3)**| **1.0x** | 2 hours | 3 days | 10% in 3 days | Create Jira ticket during business hours |
