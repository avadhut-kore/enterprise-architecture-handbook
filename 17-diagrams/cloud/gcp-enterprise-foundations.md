# Google Cloud Platform (GCP) Enterprise Foundation Architecture

GCP enterprise resource hierarchy detailing Organization resource, Folder taxonomy, Projects, Shared VPC, and Cloud Interconnect.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph GCPOrg ["Organization: company.com"]
        OrgNode["GCP Organization Node<br/>[Organization Policies & IAM]"]
    end

    subgraph OrgFolders ["Folder Taxonomy"]
        CommonFolder["Folder: Common (Infrastructure)"]
        TeamsFolder["Folder: Business Units"]
        OrgNode --> CommonFolder
        OrgNode --> TeamsFolder
    end

    subgraph CommonProjects ["Common Infrastructure Projects"]
        HostNetProj["Project: net-host-prod<br/>[Shared VPC Host Project]"]
        LoggingProj["Project: logging-audit-prod<br/>[Aggregated Log Sinks]"]
        CommonFolder --> HostNetProj
        CommonFolder --> LoggingProj
    end

    subgraph WorkloadFolders ["Business Unit Projects (Service Projects)"]
        subgraph FinanceFolder ["Folder: Finance"]
            FinProd["Project: finance-app-prod<br/>[Service Project attached to Shared VPC]"]
        end
        subgraph RetailFolder ["Folder: Retail"]
            RetailProd["Project: retail-app-prod<br/>[Service Project attached to Shared VPC]"]
        end
        TeamsFolder --> FinanceFolder
        TeamsFolder --> RetailFolder
    end

    HostNetProj <-->|"Shared VPC Subnets"| FinProd
    HostNetProj <-->|"Shared VPC Subnets"| RetailProd
    FinProd -.->|"Sink to BigQuery"| LoggingProj
```

## PlantUML Specification

```plantuml
@startuml
node "Organization: company.com" as org {
  folder "Common Infrastructure" {
    [Shared VPC Host Project]
    [Centralized Logging Project]
  }
  folder "Workload Folders" {
    [Finance Service Project]
    [Retail Service Project]
  }
}
[Shared VPC Host Project] <--> [Finance Service Project] : Subnet Attachment
[Finance Service Project] --> [Centralized Logging Project] : Audit Logs
@enduml
```

## Architectural Design Considerations

* **Shared VPC Model**: Maintain centralized control over IP addressing, firewall rules, and routes in the host project while delegating application administration to service projects.
* **Organization Policies**: Enforce constraints such as `constraints/compute.skipDefaultVpcCreation` and `constraints/gcp.resourceLocations` across the entire enterprise hierarchy.
* **IAM Least Privilege**: Never grant project-wide primitive roles (`Owner`, `Editor`) in production environments; enforce granular predefined or custom roles.

## Related Documentation & Patterns

* [AWS Well-Architected](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/aws-well-architected.md)
* [Azure Enterprise Landing Zone](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/azure-enterprise-landing-zone.md)
* [Multi-Cloud Topology](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/multi-cloud.md)
