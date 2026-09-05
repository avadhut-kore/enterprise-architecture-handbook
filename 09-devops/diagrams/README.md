# DevOps Architecture Diagrams & Visual Topologies

Curated Mermaid diagrams visualizing the enterprise DevOps delivery lifecycle, infrastructure topologies, and security boundaries.

## 1. Enterprise Continuous Delivery Flow

```mermaid
flowchart LR
    Dev["Developer Workstation"] -->|Git Push| Git["Enterprise Git (GitHub/GitLab)"]
    Git -->|Webhook| CI["Autoscaling CI Runners (K8s ARC)"]
    subgraph CI Pipeline
        Build["Build & Compile"] --> Test["Automated Tests"]
        Test --> Sec["Security Gates (SAST/Trivy)"]
        Sec --> Sign["Sign OCI (Cosign)"]
    end
    CI --> CI Pipeline
    Sign --> Reg["Immutable Artifact Registry"]
    Reg -->|Sync| GitOps["GitOps Controller (ArgoCD)"]
    GitOps -->|Reconcile| K8s["Production Kubernetes Cluster"]
```

## 2. DevSecOps Shift-Left Security Fabric

```mermaid
flowchart TD
    PreCommit["1. Pre-Commit Hook (Gitleaks)"] --> CI_Scan["2. CI Scan (Semgrep SAST & Trivy SCA)"]
    CI_Scan --> ImageSign["3. Image Signing (Cosign & Sigstore Rekor)"]
    ImageSign --> Admission["4. Admission Control (Kyverno / OPA Gatekeeper)"]
    Admission --> Runtime["5. Runtime Protection (Falco eBPF)"]
```

## 3. Internal Developer Platform (IDP) Topology

```mermaid
flowchart TD
    DevUser["Software Engineer"] -->|Self-Service| Portal["Developer Portal (Backstage)"]
    Portal -->|Scaffold / API| PlatformAPI["Platform Orchestration Engine"]
    subgraph Platform Engine
        GitOpsOrch["ArgoCD"]
        IaCOrch["Crossplane / Terraform"]
        SecretOrch["HashiCorp Vault"]
    end
    PlatformAPI --> Platform Engine
    Platform Engine --> Cloud["Multi-Cloud Infrastructure (AWS / Azure / GCP)"]
```

## 4. Progressive Canary Delivery Topology

```mermaid
flowchart LR
    Ingress["Edge Gateway / Ingress"] --> Splitter["Traffic Router (Envoy / Istio)"]
    Splitter -->|90% Traffic| Stable["Stable V1 Pods"]
    Splitter -->|10% Traffic| Canary["Canary V2 Pods"]
    Canary --> Metrics["Prometheus Telemetry"]
    Metrics --> Analyzer["Argo Rollouts Metric Analysis"]
    Analyzer -->|SLO Met| Promote["Promote V2 to 100%"]
    Analyzer -->|Error Spike| Abort["Abort & Rollback V2 Instantly"]
```

## Related Resources
- [Master Architecture Diagrams (INDEX.md)](../../INDEX.md#17-diagrams)
- [Reference Architectures](../reference-architectures/README.md)
