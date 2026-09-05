# SLA vs SLO vs SLI Architecture & Calculations

## Executive Summary

| Term | Full Name | Audience | Purpose | Example |
| :--- | :--- | :--- | :--- | :--- |
| **SLA** | Service Level Agreement | Customers & Legal | Contractual commitment with financial penalties | 99.9% availability per calendar month (or 10% bill credit) |
| **SLO** | Service Level Objective | Engineering Team | Internal target for architectural reliability | **99.95%** availability over rolling 30-day window |
| **SLI** | Service Level Indicator | Telemetry Systems | Real-time mathematical measurement of service health | $\frac{\text{Successful Requests}}{\text{Total Valid Requests}} \times 100\%$ |

---

## 1. Standard SLI Mathematical Formats

### Availability SLI:
$$\text{SLI}_{\text{avail}} = \frac{\sum \text{HTTP Requests with Status} < 500}{\sum \text{Total HTTP Requests}} \times 100\%$$

### Latency SLI:
$$\text{SLI}_{\text{latency}} = \frac{\sum \text{Requests where Latency} \le 200\text{ ms}}{\sum \text{Total Valid Requests}} \times 100\%$$

---

## 2. Unplanned Downtime Allowance Table

| Availability SLO | Allowed Downtime / Day | Allowed Downtime / Month | Allowed Downtime / Year |
| :--- | :---: | :---: | :---: |
| **99.0%** (Two 9s) | $14.4\text{ mins}$ | $7.31\text{ hours}$ | $3.65\text{ days}$ |
| **99.9%** (Three 9s) | $1.44\text{ mins}$ | $43.83\text{ mins}$ | $8.77\text{ hours}$ |
| **99.95%** (Three and a half 9s) | $43.2\text{ secs}$ | $21.92\text{ mins}$ | $4.38\text{ hours}$ |
| **99.99%** (Four 9s) | $8.64\text{ secs}$ | $4.38\text{ mins}$ | $52.60\text{ mins}$ |
| **99.999%** (Five 9s) | $0.86\text{ secs}$ | $26.30\text{ secs}$ | $5.26\text{ mins}$ |
