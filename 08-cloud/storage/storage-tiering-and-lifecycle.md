# Storage Lifecycle Management & Tiering Economics

## Executive Summary

Storage costs accumulate silently. Unmanaged object storage accounts can grow to millions of dollars in annual spend. Implementing automated **Lifecycle Policies** and **Intelligent Tiering** is a mandatory FinOps practice.

---

## 1. Lifecycle Transition Waterfall

```mermaid
graph LR
    Day0[Day 0: Standard S3 / Hot Blob - $0.023/GB] -->|30 Days No Access| Day30[Day 30: Infrequent Access / Cool - $0.0125/GB]
    Day30 -->|90 Days No Access| Day90[Day 90: Glacier Flexible / Cold - $0.0036/GB]
    Day90 -->|365 Days Retention| Day365[Day 365: Deep Archive / Archive - $0.00099/GB]
    Day365 -->|7 Years (Regulatory Mandate Expiry)| Expire[AUTOMATED EXPIRATION / DELETE]
```

---

## 2. The Retrieval Fee Trap

- Lower storage tiers charge significantly less for resting storage, but charge **punitive data retrieval fees** ($\$0.01 - \$0.03/\text{GB}$ retrieved) plus per-request API fees.
- **Anti-Pattern**: Moving high-frequency analytical data into Glacier. If an analytics query scans 100 TB of Glacier data, the retrieval fee ($\$1,000 - \$3,000$) far exceeds months of Standard storage savings.
- **Rule**: Use **Intelligent-Tiering** for unpredictable access patterns; restrict Glacier/Archive tiers strictly to immutable compliance backups and audit archives.
