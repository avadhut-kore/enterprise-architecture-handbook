# Enterprise Modernization Assessment Framework

## 1. Assessment Philosophy & Methodology
Before writing code or selecting cloud services, architects must conduct a rigorous, multi-dimensional assessment of the candidate application portfolio. The assessment evaluates technical fitness against business value to determine the appropriate modernization path.

```
       ┌─────────────────────────────────────────────────────────────┐
       │             Business Value vs. Technical Debt               │
       │                                                             │
  High │  [ REFACTOR / REARCHITECT ]       [ RETAIN / OPTIMIZE ]     │
       │  High business value,             High business value,      │
B      │  high technical debt.             low technical debt.       │
U      │  Primary candidate for            Keep running smoothly.    │
S      │  modernization investment.                                  │
I      ├─────────────────────────────────────────────────────────────┤
N      │  [ RETIRE / REPLACE ]             [ REHOST / ENCAPSULATE ]  │
E      │  Low business value,              Low business value,       │
S      │  high technical debt.             low technical debt.       │
S      │  Decommission or buy SaaS.        Move to low-cost cloud.   │
  Low  └─────────────────────────────────────────────────────────────┘
                     High                                Low
                             TECHNICAL DEBT
```

---

## 2. The 8 Assessment Dimensions

### 2.1 Business Assessment
- **Business Criticality**: Is this system Tier-0 (revenue-generating, 24/7 required) or Tier-3 (internal administrative tool)?
- **Revenue & Transaction Velocity**: Dollar value and transaction volume processed per hour.
- **Change Velocity & Time-to-Market**: How frequently does the business demand updates (daily vs. biannually)?
- **Regulatory & Compliance Scope**: Does the system handle PCI-DSS, HIPAA, GDPR, or SOX data?
- **Competitive Differentiator**: Is this bespoke IP or a generic commodity process (e.g., payroll)?

### 2.2 Application Architecture Assessment
- **Architecture Style**: Monolith, Modular Monolith, SOA, Client-Server (VB6/PowerBuilder), Mainframe.
- **Coupling & Cohesion**: Modularity index, circular package dependencies, global state usage.
- **Code Quality & Technical Debt**: Test coverage percentage, cyclomatic complexity, dead code volume.
- **Framework Currency**: Running on supported runtimes (e.g., .NET 8 vs. .NET Framework 3.5, Java 21 vs. Java 6).

### 2.3 Data Assessment
- **Data Volume & Growth**: Total storage size, daily delta growth, table row counts.
- **Schema Complexity**: Number of tables, stored procedures, triggers, views, foreign key depth.
- **Data Sharing**: Are other applications querying this database directly (`Shared Database` anti-pattern)?
- **Consistency Requirements**: Strict ACID vs. acceptable eventual consistency window.

### 2.4 Infrastructure & Hosting Assessment
- **Current Hosting**: Physical bare-metal, VMware on-premise, colocation, public cloud VM.
- **Hardware Lifecycle**: Approaching end-of-life (EOL), specialized proprietary hardware (IBM z, AS/400).
- **Capacity Utilization**: Average vs. peak CPU/Memory; ability to autoscale during traffic spikes.
- **Disaster Recovery (DR)**: Current RPO (Recovery Point Objective) and RTO (Recovery Time Objective).

### 2.5 Integration Assessment
- **Protocols & Formats**: REST, SOAP, XML, EBCDIC, Fixed-width flat files, SFTP, Proprietary MQ.
- **Integration Topology**: Point-to-point, centralized ESB, event streaming (Kafka), batch file drops.
- **Upstream & Downstream Dependencies**: Direct count of dependent consumer applications.

### 2.6 Security & Compliance Assessment
- **Identity & Authentication**: Hardcoded DB credentials, LDAP, Kerberos, SAML, OAuth 2.0.
- **Encryption**: Data at rest (AES-256) and in transit (TLS 1.2/1.3); legacy unencrypted telnet/FTP.
- **Vulnerability Posture**: Known CVEs in third-party libraries; unsupported OS patches.

### 2.7 Operational & SRE Assessment
- **Deployment Frequency**: Minutes (CI/CD) vs. months (manual change advisory board).
- **Telemetry & Observability**: Structured JSON logs, distributed tracing, metrics vs. unstructured text files.
- **Incident History**: Mean Time to Detect (MTTD) and Mean Time to Resolve (MTTR).

### 2.8 Organizational & Team Assessment
- **Institutional Knowledge**: Do original authors still work at the company? Is documentation missing?
- **Skills Gap**: COBOL/PL-SQL skills vs. modern cloud-native TypeScript/Go/Java skills.
- **Team Ownership**: Clear single team ownership vs. orphaned legacy code.

---

## 3. Modernization Scoring Matrix

| Assessment Factor | Evaluation Metric | Low Risk / High Fit (Score: 1) | Medium Risk (Score: 3) | High Risk / Complex (Score: 5) |
| :--- | :--- | :--- | :--- | :--- |
| **Dependencies** | Downstream consumer count | $0 - 2$ systems | $3 - 8$ systems | $> 8$ tightly coupled systems |
| **Database Sharing**| Direct cross-app SQL queries | Dedicated DB | Read-only shared access | Multiple apps writing to shared tables |
| **Test Coverage** | Automated unit & regression tests | $> 75\%$ coverage | $25\% - 75\%$ coverage | $< 25\%$ or zero automated tests |
| **Release Cadence**| Deployment cycle time | Weekly / Bi-weekly | Monthly | Quarterly / Semi-annually |
| **Statefulness** | Session & in-memory state | 100% Stateless | Sticky sessions on disk | Heavy local file caching, singletons |
| **Documentation** | Architectural & domain knowledge | Fully documented | Partial wiki / tribal | Zero docs; original team gone |

$$	ext{Composite Complexity Score} = \sum_{i=1}^{n} w_i 	imes S_i$$
- **Score 6 - 12**: Ideal candidate for rapid rehosting or initial capability extraction pilot.
- **Score 13 - 22**: Standard enterprise migration; requires formal wave planning and transition architectures.
- **Score 23 - 30**: High-risk mission-critical core; mandates multi-year Strangler Fig and dual-run parity verification.
