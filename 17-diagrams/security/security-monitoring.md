# Security Operations Center (SOC), SIEM & SOAR Architecture

End-to-end security telemetry pipeline uniting multi-cloud log ingest, automated event correlation, and SOAR automated playbook response.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph IngestionSources ["Telemetry Ingestion"]
        CloudLogs["Cloud Audit Logs (CloudTrail, Activity Logs)"]
        NetLogs["VPC Flow Logs & Firewall Traffic"]
        EDRLogs["Host EDR Agents (CrowdStrike / Defender)"]
        AppLogs["Application Security Logs (WAF, Auth Events)"]
    end

    subgraph CollectionPipeline ["Streaming & Normalization"]
        Kafka["Event Streaming Buffer (Kafka / Event Hubs)"]
        OCSF["Data Normalization (OCSF / CEF Format)"]
        CloudLogs --> Kafka
        NetLogs --> Kafka
        EDRLogs --> Kafka
        AppLogs --> Kafka
        Kafka --> OCSF
    end

    subgraph SIEMAnalytics ["Analytics & Correlation Engine"]
        SIEM["Central SIEM (Microsoft Sentinel / Splunk)"]
        UEBA["Behavioral Analytics (UEBA Engine)"]
        ThreatFeed["Threat Intelligence Feeds (STIX/TAXII)"]

        OCSF --> SIEM
        UEBA <--> SIEM
        ThreatFeed --> SIEM
    end

    subgraph IncidentResponse ["Automated Response (SOAR)"]
        SOAR["SOAR Engine (Cortex XSOAR / Sentinel Playbooks)"]
        SecOps["SOC Analysts (Tier 1-3)"]

        SIEM -->|"Trigger Incident Alert"| SOAR
        SOAR -->|"Dispatch High-Severity Ticket"| SecOps
        SOAR -->|"Automated Containment: Block IP at WAF"| BlockWAF["WAF / Firewall API"]
        SOAR -->|"Automated Containment: Revoke Compromised Session"| RevokeIdP["Enterprise IdP API"]
    end

    classDef collect fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef siem fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    classDef soar fill:#ffebee,stroke:#c62828,stroke-width:2px;
    class Kafka,OCSF collect;
    class SIEM,UEBA,ThreatFeed siem;
    class SOAR,BlockWAF,RevokeIdP soar;
```

## PlantUML Specification

```plantuml
@startuml
package "Log Producers" {
  [Firewall Logs]
  [CloudTrail]
  [EDR Telemetry]
}
package "Ingestion & SIEM" {
  [Kafka Buffer]
  [SIEM Analytics Engine]
}
package "Automated Remediation (SOAR)" {
  [SOAR Playbook Engine]
  [Firewall Blacklist Action]
  [IdP Revoke User Action]
}

[Log Producers] --> [Kafka Buffer]
[Kafka Buffer] --> [SIEM Analytics Engine]
[SIEM Analytics Engine] --> [SOAR Playbook Engine] : Correlation Rule Matched
[SOAR Playbook Engine] --> [Firewall Blacklist Action] : Auto-contain IP
[SOAR Playbook Engine] --> [IdP Revoke User Action] : Force User MFA Reset
@enduml
```

## Architectural Design Considerations

* **Standardized Schema**: Adopt Open Cybersecurity Schema Framework (OCSF) to harmonize events across multiple cloud providers and vendors.
* **Mean Time to Remediate (MTTR)**: Automate initial containment steps (quarantine host, block IP, revoke token) via SOAR playbooks to achieve sub-minute response times.
* **Log Immutability**: Write security audit trails directly to write-once-read-many (WORM) storage with strict legal hold policies.

## Related Documentation & Patterns

* [Threat Model](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/threat-model.md)
* [Zero Trust](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/zero-trust.md)
* [Network Security](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/network-security.md)
