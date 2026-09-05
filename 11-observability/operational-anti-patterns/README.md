# Operational Anti-Patterns (`operational-anti-patterns/`)

## Executive Summary

Operational anti-patterns create alert fatigue, fragile deployments, catastrophic outages, and severe SRE burnout.

---

## Index of Operational Anti-Patterns
1. **Alert Overload & Alarm Fatigue**: Paging on-call engineers for non-actionable CPU threshold alerts.
2. **Hero-Based Operations**: Relying on a single individual's tribal knowledge to resolve production outages.
3. **Untested Backups (Schrödinger's Backup)**: Taking backups daily without ever testing automated restoration.
4. **Friday Afternoon Deployments**: Pushing large, untested changes right before the weekend without staffing coverage.
5. **Unbounded In-Memory Queues**: Buffering requests in RAM until the process crashes with `OutOfMemoryError`.
6. **Static Capacity Allocation**: Provisioning servers for peak traffic 24/7 without dynamic autoscaling.
7. **Blame-Oriented Post-Mortems**: Blaming human error instead of fixing underlying systemic and tooling flaws.
8. **Logging Everything at DEBUG in Production**: Creating disk exhaustion and multi-thousand-dollar logging bills.
9. **Missing Health Checks**: Load balancers routing traffic to dead or hung backend pods.
10. **Cascading Retry Storms**: Retrying failed calls immediately without exponential backoff and jitter.
11. **Manual Production Changes (ClickOps)**: Modifying cloud infrastructure manually via web consoles.
12. **Bypassing the Staging Gate**: Pushing emergency hotfixes directly to production without testing.
