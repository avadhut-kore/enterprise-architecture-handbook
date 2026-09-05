# Cutover Strategies Comparative Framework

## 1. The Strategy Spectrum

| Strategy | Mechanical Description | Downtime | Risk Profile | Reversibility | Best Suited For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Big Bang** | Switch 100% of traffic in a single maintenance window | Hours | Very High | Low to None | Small monolithic apps, breaking schema changes |
| **Phased (Canary)** | Shift traffic incrementally (1% $ightarrow$ 5% $ightarrow$ 25% $ightarrow$ 100%) | Zero | Low | Immediate | Stateless APIs, microservices, web apps |
| **Parallel Run** | Run both systems concurrently; verify outputs before switch | Zero | Medium | High | High-risk financial ledgers, payroll engines |
| **Shadow Traffic** | Mirror real traffic asynchronously to new system; discard responses | Zero | Very Low | High | Pre-cutover load and regression testing |
| **Cohort / Tenant**| Migrate tenant-by-tenant or branch-by-branch | Zero | Low | High | Multi-tenant SaaS, regional banking branches |
