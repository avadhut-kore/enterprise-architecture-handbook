# Risk Acceptance & Compensating Controls

When an architecture exception is granted, the business must formally accept financial and security liability.

---

## 1. Compensating Controls Architecture

If an application cannot meet an enterprise standard, it must deploy compensating controls to neutralize the blast radius:

```mermaid
flowchart LR
    NonStandard["Non-Standard Legacy App<br/>(Running unsupported Java 8, vulnerable to CVEs)"] --> WAF["Compensating Control 1:<br/>Dedicated Web Application Firewall with Virtual Patching Rules"]
    NonStandard --> Enclave["Compensating Control 2:<br/>Isolated Zero-Trust Micro-segmentation (No egress to corporate network)"]
    NonStandard --> EDR["Compensating Control 3:<br/>Continuous Endpoint Threat Telemetry with 24/7 SOC Alerting"]
```

---

## 2. Formal Risk Acceptance Signature
The Business Unit VP must sign a formal legal liability statement:
> *"I accept the operational and security risks associated with running System X on unpatched software. In the event of a breach or compliance fine resulting from this exception, my business unit assumes financial responsibility for remediation."*
