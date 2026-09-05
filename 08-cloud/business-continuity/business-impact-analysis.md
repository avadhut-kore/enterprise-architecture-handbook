# Business Impact Analysis (BIA) & Service Tiering

## Executive Summary

The Business Impact Analysis (BIA) quantifies the financial, regulatory, and reputational impact of system downtime, establishing the **Maximum Tolerable Downtime (MTD)** for each business service.

---

## 1. Enterprise Service Criticality Tiers

| Criticality Tier | Target Systems | Max Tolerable Downtime (MTD) | Mandated DR Pattern |
| :--- | :--- | :---: | :--- |
| **Tier 1: Mission-Critical** | Real-time payment processing, ATM clearing, trading engine | $< 15\text{ Minutes}$ | Multi-Region Active-Active / Warm Standby |
| **Tier 2: Business-Critical** | Customer portal, loan origination, e-commerce checkout | $< 2\text{ Hours}$ | Multi-Region Pilot Light |
| **Tier 3: Business-Operational**| Monthly invoicing, customer service ticketing, internal HR | $< 24\text{ Hours}$ | Automated Backup & Restore |
| **Tier 4: Non-Critical** | Internal knowledge wikis, archived reporting, dev sandboxes | $< 72\text{ Hours}$ | Cold Archive / Rebuild from Git |
