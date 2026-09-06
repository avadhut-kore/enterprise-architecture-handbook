#!/usr/bin/env python3
"""
NFR Matrix Generator - Automated Non-Functional Requirements Document Scaffolder
Generates structured, measurable NFR tables for system design reviews.

Usage:
    python nfr_matrix_generator.py --system-name "Payment Gateway Service" --tier Tier-1 --out-file nfr-matrix.md
"""

import argparse
import datetime
import os

NFR_TEMPLATE = r"""# Non-Functional Requirements (NFR) Specification: {system_name}

> **Criticality Tier**: {tier}  
> **Date**: {date}  
> **Target Audience**: Solution Architects, Tech Leads, SRE / Security Engineers  

---

## 1. Quality Attribute Matrix

| Category | Quality Attribute | Metric / SLI | Target Objective (SLO) | Measurement Mechanism | Architecture Mitigation / Control |
|---|---|---|---|---|---|
| **Performance** | Latency (p95) | HTTP Request Duration | $< 150\text{{ms}}$ | OpenTelemetry APM Trace | Redis caching, non-blocking asynchronous I/O |
| **Performance** | Latency (p99) | HTTP Request Duration | $< 350\text{{ms}}$ | OpenTelemetry APM Trace | Request hedging, database query index optimization |
| **Performance** | Peak Throughput | Transactions Per Sec | $\ge {tps}\text{{ TPS}}$ | Prometheus / Grafana rate() | Horizontal Pod Autoscaler (HPA), KEDA queue-based scaling |
| **Reliability** | System Availability | Successful Request Ratio | $\ge {availability}\%$ ({nines}) | Synthetic Blackbox Canary | Multi-AZ deployment, active-active failover, circuit breakers |
| **Reliability** | Error Budget | Monthly Allowed Downtime | $\le {downtime}$ | Prometheus Alertmanager | Feature freeze policy when error budget depleted |
| **Resilience** | Disaster Recovery RTO | Time to Restore Service | $\le {rto}$ | DR Game Day Drill | Automated Terraform rebuild, DNS failover rerouting |
| **Resilience** | Disaster Recovery RPO | Maximum Data Loss | $\le {rpo}$ | Cross-Region WAL Lag | Asynchronous replication stream, automated snapshot logs |
| **Security** | Transport Security | Cipher Protocol | TLS 1.3 Exclusively | Edge WAF SSL Inspection | Disable legacy TLS 1.0/1.1/1.2; enforce mTLS 1.3 internally |
| **Security** | Data at Rest | Encryption Standard | AES-256-GCM Envelope | Cloud KMS Audit Logs | Customer Managed Keys (CMK) with automated 365-day rotation |
| **Security** | Authentication | Token Lifespan | OAuth 2.0 JWT $\le 60\text{{m}}$ | IAM Identity Provider | Short-lived access tokens, refresh token rotation |
| **FinOps** | Unit Cost | Cost per Transaction | $\le \${unit_cost}$ | AWS Cost Allocation Tags | Spot instances for batch queues, VPC Endpoints for S3 |

---

## 2. Architectural Verification & Acceptance Criteria
* [ ] Automated load tests in staging confirm system sustains projected peak TPS without pod crashloops.
* [ ] Latency budgets verified with p95 and p99 trace assertions in CI/CD performance testing.
* [ ] Chaos engineering drills verify circuit breaker trips and isolates failing dependencies.
* [ ] Security penetration tests confirm zero plaintext credential leakage.
"""

TIER_DEFAULTS = {
    "Tier-1": {"availability": "99.99", "nines": "Four Nines", "downtime": "4.38 mins/month", "rto": "15 minutes", "rpo": "1 minute", "tps": "10,000", "unit_cost": "0.005"},
    "Tier-2": {"availability": "99.95", "nines": "Standard Enterprise", "downtime": "21.9 mins/month", "rto": "1 hour", "rpo": "15 minutes", "tps": "2,500", "unit_cost": "0.01"},
    "Tier-3": {"availability": "99.5", "nines": "Internal Non-Critical", "downtime": "3.65 hours/month", "rto": "4 hours", "rpo": "4 hours", "tps": "500", "unit_cost": "0.02"}
}

def main():
    parser = argparse.ArgumentParser(description="Generate NFR specification matrix.")
    parser.add_argument("--system-name", required=True, help="Name of the system or microservice")
    parser.add_argument("--tier", choices=["Tier-1", "Tier-2", "Tier-3"], default="Tier-1", help="Criticality tier")
    parser.add_argument("--out-file", default="nfr-matrix.md", help="Output markdown filename")

    args = parser.parse_args()
    defaults = TIER_DEFAULTS[args.tier]

    content = NFR_TEMPLATE.format(
        system_name=args.system_name,
        tier=args.tier,
        date=datetime.date.today().isoformat(),
        availability=defaults["availability"],
        nines=defaults["nines"],
        downtime=defaults["downtime"],
        rto=defaults["rto"],
        rpo=defaults["rpo"],
        tps=defaults["tps"],
        unit_cost=defaults["unit_cost"]
    )

    with open(args.out_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[OK] Successfully generated NFR Matrix: {args.out_file}")

if __name__ == "__main__":
    main()
