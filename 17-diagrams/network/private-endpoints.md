# Private Endpoints & Zero-Exgress PaaS Network Architecture

Zero-exgress network architecture detailing AWS PrivateLink and Azure Private Endpoints to access cloud PaaS services entirely within private VPC networks without traversing the public internet.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph PrivateVPC ["Private Workload VPC (10.0.0.0/16) - Zero Internet Gateway"]
        subgraph AppSubnets ["Private Application Subnets"]
            AppPod["Backend Application Pods"]
        end

        subgraph EndpointSubnets ["Dedicated PrivateLink Subnets"]
            VPCES3["Interface VPC Endpoint: S3<br/>(Private IP: 10.0.2.14)"]
            VPCEVault["Interface VPC Endpoint: Secrets Manager<br/>(Private IP: 10.0.2.15)"]
            VPCEDB["Interface VPC Endpoint: Database Service<br/>(Private IP: 10.0.2.16)"]
        end

        AppPod -->|"Private DNS Lookup"| VPCES3
        AppPod -->|"Private DNS Lookup"| VPCEVault
        AppPod -->|"Private DNS Lookup"| VPCEDB
    end

    subgraph AWSManagedServices ["AWS Cloud Managed PaaS Tier"]
        CloudS3["Amazon S3 Storage Buckets"]
        CloudVault["AWS Secrets Manager"]
        CloudDB["Amazon Aurora PostgreSQL"]

        VPCES3 -.->|"AWS Internal Hyperplane"| CloudS3
        VPCEVault -.->|"AWS Internal Hyperplane"| CloudVault
        VPCEDB -.->|"AWS Internal Hyperplane"| CloudDB
    end

    classDef vpc fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef paas fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    class AppPod,VPCES3,VPCEVault,VPCEDB vpc;
    class CloudS3,CloudVault,CloudDB paas;
```

## PlantUML Specification

```plantuml
@startuml
package "Private VPC (No IGW)" {
  node "Private App Subnet" {
    component "Application Pod" as app
  }
  node "Interface Endpoint Subnet" {
    component "Interface Endpoint S3 (10.0.2.14)" as epS3
    component "Interface Endpoint Vault (10.0.2.15)" as epVault
  }
}
package "AWS Managed PaaS" {
  database "Amazon S3 Bucket" as s3
  component "Secrets Manager" as vault
}

app -> epS3 : Internal TLS (10.0.2.14)
app -> epVault : Internal TLS (10.0.2.15)
epS3 ..> s3 : Private Hyperplane Link
epVault ..> vault : Private Hyperplane Link
@enduml
```

## Architectural Design Considerations
* **Zero Internet Route**: Private endpoints allow removing NAT Gateways and Internet Gateways entirely from private database and application subnets, slashing data egress costs.
* **Endpoint Policies**: Attach strict IAM resource policies directly to VPC Endpoints to restrict access exclusively to designated corporate AWS accounts or S3 buckets.
* **Private DNS Integration**: Enable Private DNS resolution so existing application connection strings (e.g., `s3.amazonaws.com`) automatically resolve to private subnet IP addresses without code changes.

## Related Documentation & Patterns
* [Zero Trust Network](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/zero-trust-network.md)
* [Public & Private Subnets](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/public-private-subnet.md)
* [Security: Secrets Management](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/secrets-management.md)
