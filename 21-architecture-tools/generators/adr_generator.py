#!/usr/bin/env python3
"""
ADR Generator - Automated Architecture Decision Record Scaffolder
Generates standardized, production-grade ADRs compliant with DOCUMENTATION-STANDARD.md.

Usage:
    python adr_generator.py --title "Adopt Kafka for Order Streaming" --author "Alice Architect" --status ACCEPTED --out-dir ./adrs
"""

import argparse
import datetime
import os
import re
import sys

ADR_TEMPLATE = """# ADR-{number:04d}: {title}

## Status
**{status}** — Decision Date: {date}  
**Decision Maker(s)**: {author}  
**Consulted**: {consulted}  
**Informed**: {informed}  

---

## 1. Context & Problem Statement
{problem}

---

## 2. Decision Drivers (Forces & NFRs)
* **Latency Budget**: Must complete under 200ms p99.
* **Throughput**: Must scale to {throughput} requests/sec.
* **Availability Target**: 99.95% uptime SLA.
* **Security & Compliance**: Zero trust posture, data encrypted at rest and in transit.

---

## 3. Considered Options
1. **Option A (Chosen)**: {title}
2. **Option B (Alternative)**: Traditional Synchronous HTTP/REST API.
3. **Option C (Alternative)**: Batch File / Database Polling.

---

## 4. Decision & Rationale
We decided to proceed with **Option A: {title}** because:
* It satisfies our core throughput and latency NFRs without tight temporal coupling.
* It provides isolated failure domains and natural backpressure buffering.
* It aligns with our enterprise technology roadmap and team capabilities.

---

## 5. Architectural Blueprint & Data Flow
```mermaid
sequenceDiagram
    autonumber
    participant Client as Client Application
    participant Gateway as API Gateway
    participant Engine as {title}
    participant Storage as Primary Datastore

    Client->>Gateway: Submit Mutation Request
    Gateway->>Engine: Forward Event / Transaction
    Engine->>Storage: Commit State
    Storage-->>Engine: State Committed
    Engine-->>Gateway: Success Acknowledged
    Gateway-->>Client: 200 OK
```

---

## 6. Consequences & Trade-off Matrix

| Dimension | Positive Consequences (Gains) | Negative Consequences (Sacrifices / Costs) |
|---|---|---|
| **Performance** | Asynchronous decoupling eliminates blocking thread starvation. | Introduces eventual consistency window. |
| **Complexity** | Clean separation of domain boundaries. | Requires managing distributed failure modes and retry queues. |
| **FinOps Cost** | Linear resource scaling with autoscaling. | Added broker/cluster infrastructure management spend. |

---

## 7. Validation & Architecture Fitness Functions
* [ ] Automated schema validation enforced in CI/CD pipeline.
* [ ] Load tests executed to verify throughput under 2x projected peak.
* [ ] Chaos injection verified automated failover under 30 seconds.

---

## 8. References & Prior Art
* Enterprise Architecture Handbook: `01-architecture/`
* Architecture Governance Standard: `01-architecture/architecture-governance/`
"""

def sanitize_filename(title: str) -> str:
    cleaned = re.sub(r'[^\w\s-]', '', title.lower())
    return re.sub(r'[-\s]+', '-', cleaned).strip('-')

def get_next_adr_number(out_dir: str) -> int:
    if not os.path.exists(out_dir):
        return 1
    existing_files = os.listdir(out_dir)
    numbers = []
    for f in existing_files:
        match = re.match(r'^(?:adr-)?(\d+)', f, re.IGNORECASE)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers) + 1 if numbers else 1

def main():
    parser = argparse.ArgumentParser(description="Generate standardized Architecture Decision Records (ADR).")
    parser.add_argument("--title", required=True, help="Title of the architecture decision")
    parser.add_argument("--author", default="Solution Architect", help="Primary author / decision maker")
    parser.add_argument("--status", choices=["PROPOSED", "ACCEPTED", "SUPERSEDED", "REJECTED"], default="ACCEPTED", help="ADR status")
    parser.add_argument("--problem", default="Describe the technical or business problem that forces this decision.", help="Problem statement context")
    parser.add_argument("--throughput", default="5,000", help="Target throughput requirement")
    parser.add_argument("--consulted", default="Security Team, Platform SRE", help="Stakeholders consulted")
    parser.add_argument("--informed", default="Engineering Squads, Product Owner", help="Stakeholders informed")
    parser.add_argument("--out-dir", default=".", help="Target directory to save the ADR")

    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    adr_num = get_next_adr_number(args.out_dir)
    filename = f"adr-{adr_num:04d}-{sanitize_filename(args.title)}.md"
    file_path = os.path.join(args.out_dir, filename)

    content = ADR_TEMPLATE.format(
        number=adr_num,
        title=args.title,
        status=args.status,
        date=datetime.date.today().isoformat(),
        author=args.author,
        consulted=args.consulted,
        informed=args.informed,
        problem=args.problem,
        throughput=args.throughput
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[OK] Successfully generated ADR: {file_path}")

if __name__ == "__main__":
    main()
