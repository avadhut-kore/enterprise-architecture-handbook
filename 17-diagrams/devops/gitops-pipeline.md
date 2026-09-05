# GitOps Continuous Delivery Architecture (ArgoCD / Flux)

Declarative pull-based GitOps deployment architecture maintaining Git as the single source of truth and continuously reconciling live cluster state against desired state.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph GitRepositories ["Git Repositories (Source of Truth)"]
        AppGit["Application Source Repo<br/>(Go / Java code)"]
        ConfigGit["GitOps Deployment Config Repo<br/>(Helm Charts / Kustomize Manifests)"]
    end

    subgraph CIPipeline ["CI Engine (GitHub Actions)"]
        Build["1. Build & Unit Test"]
        Scan["2. Security Scan (Trivy / SAST)"]
        PushImg["3. Push Signed Image to Registry"]
        UpdateManifest["4. Commit New Image Digest to Config Git"]

        AppGit --> Build
        Build --> Scan
        Scan --> PushImg
        PushImg --> UpdateManifest
        UpdateManifest --> ConfigGit
    end

    subgraph ContainerRegistry ["Artifact Storage"]
        Harbor["OCI Container Registry<br/>(Signed Image: app:v2.1.0)"]
        PushImg --> Harbor
    end

    subgraph KubernetesCluster ["Production Kubernetes Cluster (EKS)"]
        ArgoCD["ArgoCD GitOps Operator<br/>(Continuous In-Cluster Controller)"]
        LiveState["Live Production Pods (v2.0.0)"]
        
        ArgoCD -->|"5. Detect Drift (Config vs Live)"| ConfigGit
        ArgoCD -->|"6. Pull Desired Image"| Harbor
        ArgoCD -->|"7. Reconcile & Apply Manifests"| LiveState
    end
```

## PlantUML Specification

```plantuml
@startuml
actor Developer
participant "Application Git" as appRepo
participant "CI Pipeline" as ci
participant "OCI Registry" as reg
participant "GitOps Config Git" as gitopsRepo
participant "ArgoCD Controller" as argo
node "Kubernetes Cluster" as k8s

Developer -> appRepo : Push commit
appRepo -> ci : Trigger build
ci -> ci : Test & Build Container
ci -> reg : Push signed image
ci -> gitopsRepo : Update Helm value (image tag)
argo -> gitopsRepo : Pull desired state
argo -> k8s : Reconcile cluster state (Pull from registry)
@enduml
```

## Architectural Design Considerations

* **Pull vs Push Deployments**: GitOps agents run inside the cluster and pull manifests, eliminating the need to expose Kubernetes API credentials to external CI runners.
* **Drift Detection & Self-Healing**: ArgoCD automatically detects manual configuration changes made directly to the cluster and immediately reverts them back to the Git baseline.
* **Separation of Repositories**: Keep application source code repositories separate from deployment manifest repositories to prevent infinite CI trigger loops.

## Related Documentation & Patterns

* [CI/CD Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/devops/ci-cd-flow.md)
* [Canary Deployment](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/devops/canary.md)
* [Blue-Green Deployment](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/devops/blue-green.md)
