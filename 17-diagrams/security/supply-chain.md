# Software Supply Chain Security & DevSecOps Architecture

End-to-end secure software factory implementing SAST, SCA, container image signing, Software Bill of Materials (SBOM), and SLSA Level 3 provenance.

## Mermaid Architecture Diagram

```mermaid
sequenceDiagram
    autonumber
    actor Dev as Software Engineer
    participant Git as GitHub / GitLab Enterprise
    participant Pipeline as CI/CD Pipeline Runner
    participant SecurityTools as Security Scanners (SAST / SCA)
    participant Cosign as Sigstore / Cosign Signer
    participant Registry as Secure Container Registry (Harbor / ECR)
    participant K8s as Production Cluster (Kyverno / Gatekeeper)

    Dev->>Git: Commit Signed Code (GPG / SSH)
    Git->>Pipeline: Trigger Build Pipeline
    
    Pipeline->>SecurityTools: Execute SAST (Semgrep) & SCA (Snyk / Dependabot)
    SecurityTools-->>Pipeline: No Critical Vulnerabilities Found
    
    Pipeline->>Pipeline: Compile Binary & Build Docker Image
    Pipeline->>Pipeline: Generate SPDX / CycloneDX SBOM
    
    Pipeline->>Cosign: Cryptographically Sign Image & Attestation
    Note over Cosign: Keyless signing with OIDC identity & Fulcio CA
    Cosign-->>Pipeline: Signed Image Digest + Rekor Transparency Entry
    
    Pipeline->>Registry: Push Image + SBOM + Cryptographic Signature
    
    K8s->>Registry: Pull Image for Deployment
    Note over K8s: Admission Controller (Kyverno) enforces policy: Verify Signature
    K8s->>K8s: Image Signature Verified against Cosign Root
    K8s-->>K8s: Allow Pod Scheduling to Production Node
```

## PlantUML Specification

```plantuml
@startuml
actor Developer
participant "Source Git" as git
participant "CI Pipeline" as ci
participant "SAST & SCA Scanner" as scanner
participant "Sigstore / Cosign" as sig
participant "Container Registry" as reg
participant "K8s Admission Webhook" as k8s

Developer -> git : Commit signed code
git -> ci : Trigger CI workflow
ci -> scanner : Scan dependencies & static code
ci -> ci : Build container image & generate SBOM
ci -> sig : Sign container image digest
ci -> reg : Push signed image + SBOM
k8s -> reg : Validate signature before deployment
k8s -> k8s : Run verified container
@enduml
```

## Architectural Design Considerations

* **Shift-Left Security**: Enforce security gates during local development and pre-commit checks; prevent vulnerable code from entering mainline branches.
* **SLSA Framework Compliance**: Target SLSA (Supply-chain Levels for Software Artifacts) Level 3 by ensuring build platforms generate non-falsifiable provenance.
* **Admission Control Policy**: Enforce cluster-level admission controllers (e.g., Kyverno or OPA Gatekeeper) to reject un-signed container images.

## Related Documentation & Patterns

* [API Security](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/api-security.md)
* [Zero Trust](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/zero-trust.md)
* [Security Checklists](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/checklists.md)
