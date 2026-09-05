# Enterprise Hub-and-Spoke Network Architecture

The standard topology for multi-account, enterprise-scale cloud deployments, centralizing inspection, security policies, and shared services.

```mermaid
flowchart TD
    subgraph InspectionHub["Hub VPC: Security & Inspection (10.0.0.0/16)"]
        TGW["Transit Gateway (AWS TGW / Azure vWAN)"]
        Firewall["Next-Gen Firewall Cluster (Palo Alto / Fortinet)"]
        NAT_GW["Centralized NAT Gateways (Egress Pool)"]
        SharedSVPC["Shared Services (Active Directory, DNS, CI/CD)"]
    end

    subgraph SpokeA["Spoke VPC A: Payments (10.1.0.0/16)"]
        AppA["Payment Microservices (EKS)"]
    end

    subgraph SpokeB["Spoke VPC B: Core Banking (10.2.0.0/16)"]
        AppB["Banking Ledger (PostgreSQL Aurora)"]
    end

    subgraph SpokeC["Spoke VPC C: Analytics (10.3.0.0/16)"]
        AppC["Spark / Lakehouse Compute"]
    end

    subgraph CorporateOnPrem["On-Premises Corporate DC (172.16.0.0/12)"]
        Mainframe["Legacy Core Mainframe"]
    end

    Internet["Public Internet"] --> NAT_GW
    CorporateOnPrem == DirectConnect / BGP == TGW

    TGW <--> Firewall
    Firewall <--> NAT_GW
    TGW <--> SharedSVPC

    SpokeA <== TGW Attachment ==> TGW
    SpokeB <== TGW Attachment ==> TGW
    SpokeC <== TGW Attachment ==> TGW
```
