# Privileged Access Management (PAM) & Just-in-Time Elevation

Zero standing privileges architecture detailing Just-in-Time (JIT) access approval, ephemeral SSH/RDP certificates, and full session recording.

## Mermaid Architecture Diagram

```mermaid
sequenceDiagram
    autonumber
    actor Admin as System Administrator
    participant Portal as PAM Web Portal (Teleport / CyberArk)
    participant Approver as Security Operations Approver
    participant Vault as Ephemeral CA / Credential Vault
    participant TargetServer as Production Database Host

    Admin->>Portal: Request 1-Hour SSH Access to Production DB
    Note over Portal: Ticket: INC-9482 (Production Outage Severity 1)
    Portal->>Approver: Dispatch Approval Notification (Slack / PagerDuty)
    Approver->>Portal: Approve Request (MFA Authenticated)
    
    Portal->>Vault: Issue Short-Lived SSH User Certificate (TTL: 60m)
    Vault-->>Portal: Signed Ephemeral Certificate
    Portal-->>Admin: Certificate Injected into Admin's Local SSH Agent
    
    Admin->>TargetServer: SSH Connect (ssh user@db-prod-01)
    TargetServer->>TargetServer: Verify Certificate Signature via Trusted CA
    TargetServer-->>Admin: Session Established
    
    Note over Portal,TargetServer: Session is Proxied and Streamed in Real-Time for Audit
    Portal->>Portal: Record Keystrokes, Commands & Output
    
    Note over Admin,TargetServer: After 60 minutes, Certificate Expires; Session Automatically Terminated
```

## PlantUML Specification

```plantuml
@startuml
autonumber
actor "SysAdmin" as admin
participant "PAM Gateway" as pam
participant "SecOps Manager" as approver
component "Ephemeral CA" as ca
node "Production Server" as host

admin -> pam : Request Access to Server (Reason + Ticket)
pam -> approver : Request Authorization
approver -> pam : Approve Request
pam -> ca : Generate 60-min Ephemeral Certificate
ca -> pam : Ephemeral Cert
pam -> host : Proxy Session + Record Keystrokes
host -> admin : Terminal Session Active
@enduml
```

## Architectural Design Considerations

* **Zero Standing Privileges (ZSP)**: No user or administrator should maintain permanent administrator or root rights on production infrastructure.
* **Dual-Custody Approvals**: Production elevation requests must require explicit secondary authorization for high-criticality systems.
* **Session Recording and Telemetry**: Record terminal sessions, keystrokes, and screen captures; forward logs in real time to immutable WORM storage.

## Related Documentation & Patterns

* [IAM Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/iam.md)
* [Zero Trust](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/zero-trust.md)
* [Security Operations](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/security-monitoring.md)
