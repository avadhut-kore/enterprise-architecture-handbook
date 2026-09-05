# Production Readiness Review (PRR) Checklist

## Executive Summary

This checklist must be ratified by the SRE Lead and Solution Architect prior to opening production customer traffic.

---

## 1. Architecture & Capacity
- [ ] Deployed across a minimum of 3 Availability Zones.
- [ ] Auto-scaling configured with minimum capacity sized for $N+1$ AZ failure.
- [ ] Load testing executed to $200\%$ of projected peak traffic with passing latency SLAs.

## 2. Security
- [ ] STRIDE threat model completed and ratified by ARB.
- [ ] Zero static credentials in code or containers; Workload Identity Federation active.
- [ ] All database connections encrypted with TLS 1.3 and envelope-encrypted at rest.

## 3. Observability & Alerting
- [ ] Structured JSON logging emitted to central log aggregator with distributed trace IDs.
- [ ] Golden Signals dashboard live in Grafana (Latency, Traffic, Errors, Saturation).
- [ ] Multi-window SLO burn-rate alerts configured in PagerDuty; zero noisy CPU-only pages.

## 4. Operational Ownership
- [ ] Primary and secondary on-call engineers assigned in PagerDuty rotation.
- [ ] Verified operational runbooks published for all high-priority alerts.
- [ ] Service tier (Tier 1 vs Tier 2) registered in Enterprise Service Catalog.

## 5. Deployment & Disaster Recovery
- [ ] Progressive canary deployment pipeline active with automated metric rollback.
- [ ] Database migrations adhere to expand-contract backward compatibility rules.
- [ ] Automated daily snapshots replicated cross-region; restore tested within last 30 days.
