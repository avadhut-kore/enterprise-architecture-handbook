# Reconciliation Monitoring and Break Dashboards

## 1. The Role of Break Dashboards
Reconciliation breaks represent financial or data discrepancies between systems that could not be automatically reconciled by the end-of-day matching engine.

## 2. Key Operational Metrics
- **Unreconciled Volume / Value**: Total dollar amount of open financial breaks.
- **Break Aging**: Categorized by duration ($< 24	ext{h}$, $24	ext{h}-72	ext{h}$, $> 72	ext{h}$). Regulatory compliance requires reporting breaks aging over 72 hours.
- **Auto-Matching Percentage**: Target $\ge 99.5\%$ automated matching rate; any drop indicates upstream schema drift.
