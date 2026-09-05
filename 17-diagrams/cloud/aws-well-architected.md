# AWS Multi-Account Organization & Well-Architected Topology

AWS Control Tower multi-account architecture aligning with the 6 Pillars of the AWS Well-Architected Framework across security, shared services, and workload accounts.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph RootOU ["Root Management Account (AWS Organizations)"]
        RootAccount["Payer / Billing Account<br/>[AWS Control Tower / SCPs]"]
    end

    subgraph CoreOU ["Core Services Organizational Unit (OU)"]
        subgraph SecurityOU ["Security OU"]
            SecLog["Log Archive Account<br/>(Central S3 WORM)"]
            SecAudit["Security Tooling Account<br/>(GuardDuty, SecurityHub)"]
        end
        subgraph InfrastructureOU ["Shared Infrastructure OU"]
            NetHub["Network Transit Hub Account<br/>(AWS Transit Gateway / DirectConnect)"]
            SharedSvc["Shared Services Account<br/>(CI/CD Runners, Artifact Registry)"]
        end
    end

    subgraph WorkloadOU ["Workloads Organizational Unit (OU)"]
        subgraph ProdOU ["Production OU"]
            ProdApp["App Production Account<br/>(EKS, Aurora, Private Subnets)"]
        end
        subgraph NonProdOU ["Non-Production OU"]
            DevApp["App Dev/Test Account<br/>(Sandbox VPC)"]
        end
    end

    RootAccount --> CoreOU
    RootAccount --> WorkloadOU
    NetHub <-->|"TGW Attachments"| ProdApp
    NetHub <-->|"TGW Attachments"| DevApp
    ProdApp -.->|"Stream Audit Logs"| SecLog
    DevApp -.->|"Stream Audit Logs"| SecLog
```

## PlantUML Specification

```plantuml
@startuml
package "AWS Organization" {
  node "Management Account" as root
  package "Core OU" {
    node "Network Hub (TGW)" as net
    node "Log Archive (S3 WORM)" as log
    node "Security Tooling" as sec
  }
  package "Workloads OU" {
    node "Production Account" as prod
    node "Non-Production Account" as dev
  }
}
root --> net
root --> prod
net <--> prod : Transit Gateway
prod --> log : Audit Logs
@enduml
```

## Architectural Design Considerations

* **Service Control Policies (SCPs)**: Attach guardrails at the Root and OU levels to disable root user logins, prevent disabling of GuardDuty, and restrict unauthorized AWS regions.
* **Network Isolation**: Workload accounts contain zero internet gateways; all ingress and egress traffic traverses the central Network Hub account via AWS Transit Gateway.
* **Least Privilege Workload Accounts**: Developers have zero console access to Production accounts; releases occur exclusively via automated CI/CD pipelines.

## Related Documentation & Patterns

* [Azure Enterprise Landing Zone](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/azure-enterprise-landing-zone.md)
* [GCP Enterprise Foundations](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/gcp-enterprise-foundations.md)
* [Network: Transit Gateway](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/transit-network.md)
