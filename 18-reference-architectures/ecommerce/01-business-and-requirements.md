# Business Architecture & Requirements: E-Commerce Platform

## 1. Business Context & Flash-Sale Dynamics
- **Peak Retail Traffic Asymmetry**: During major shopping events (Black Friday, Singles' Day), traffic spikes by 50x to 100x within 60 seconds of a flash-sale launch.
- **Zero Overselling Mandate**: Selling more units than physically available in warehouses results in canceled orders, customer churn, and merchant penalties.

---

## 2. Scale Model & Capacity Assumptions

| Scale Dimension | Baseline Traffic | Flash-Sale Peak (100x Surge) |
| :--- | :--- | :--- |
| **Monthly Active Users (MAU)**| 5,000,000 MAU | 50,000,000 MAU |
| **Concurrent Active Sessions**| 25,000 sessions | 1,500,000 sessions |
| **Product Catalog SKUs** | 1,000,000 SKUs | 10,000,000 SKUs |
| **Steady-State Orders / Sec** | 50 orders/sec | 5,000 orders/sec |
| **Peak Cart Checkout / Sec** | 200 checkouts/sec | 25,000 checkouts/sec |
| **CDN Edge Request Rate** | 10,000 req/sec | 600,000 req/sec |

---

## 3. Measurable NFR Budgets

| NFR Metric | Target Budget | Measurement & Enforcement Point |
| :--- | :--- | :--- |
| **Catalog Search P95 Latency** | $< 80\text{ ms}$ | OpenSearch cluster with warm field-data caches |
| **Add-to-Cart P99 Latency** | $< 100\text{ ms}$ | In-memory Redis session cluster |
| **Checkout Submit P99 Latency** | $< 1.5\text{ s}$ | End-to-end payment authorization + Saga commit |
| **Platform Availability** | 99.99% ($< 4.3\text{ min}$/mo)| Multi-AZ active-active Kubernetes clusters |
| **Inventory Oversell Rate** | 0.00% (Strict Zero Tolerance) | Distributed Redis lock with atomic Lua script |
| **PCI-DSS Compliance Scope** | SAQ A (Zero Cardholder Data in CDE) | Hosted iFrame tokenization (Stripe Elements / Adyen) |
