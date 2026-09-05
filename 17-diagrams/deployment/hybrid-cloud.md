# Hybrid Cloud Connectivity Deployment

```mermaid
flowchart LR
    subgraph OnPrem["Corporate On-Premises Data Center"]
        LegacyDB["Mainframe & Oracle DB"]
        EdgeRouter["Customer Gateway (DirectConnect Link)"]
    end
    subgraph AWS["AWS Cloud Environment"]
        VGW["Direct Connect Gateway (VGW)"]
        CloudApp["Cloud Microservices (EKS)"]
    end

    LegacyDB --> EdgeRouter
    EdgeRouter == Dedicated 10 Gbps Fiber == VGW
    VGW --> CloudApp
```
