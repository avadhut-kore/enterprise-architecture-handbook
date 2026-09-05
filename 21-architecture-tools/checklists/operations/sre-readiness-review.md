# Checklist: SRE Readiness Review Checklist

## Executive Summary
This operational checklist must be validated prior to production promotion.

---

## Verification Criteria
- [ ] Quantitative SLIs defined for Availability and Latency.
- [ ] Realistic SLOs (e.g. 99.95%) approved by Product Owner.
- [ ] Error budget policy documented: releases freeze when budget is spent.
- [ ] Distributed tracing context propagated via OpenTelemetry.
- [ ] Zero non-actionable CPU threshold paging alerts.
