# Security & Operations Architecture Interview Playbook

## Executive Summary

This playbook contains structured architectural solutions to 14 high-stakes enterprise Security & SRE system design scenarios. Every scenario follows the required architectural reasoning sequence:
$$\text{Requirements} \rightarrow \text{Constraints} \rightarrow \text{NFRs} \rightarrow \text{Options} \rightarrow \text{Trade-offs} \rightarrow \text{Decision} \rightarrow \text{Failure Modes} \rightarrow \text{Cost}$$

---

## 1. Design a Zero Trust Architecture for a Global Bank
- **Requirements**: Eliminate internal network trust; support 50,000 hybrid employees and 200 microservices.
- **NFRs**: Sub-5ms auth overhead; 99.999% availability; strict PCI-DSS & SOC 2 compliance.
- **Architecture**: Identity as the primary perimeter. Workforce access governed by Cloudflare ZTNA with device posture checks and FIDO2 passkeys. Internal microservices communicate over an Istio mTLS service mesh using SPIFFE/SPIRE short-lived X.509 certs. API authorization evaluated locally via Open Policy Agent (OPA) sidecars querying cached Rego bundles.
- **Trade-off**: Higher operational complexity of running a service mesh accepted to achieve complete cryptographic lateral movement defense.

## 2. Design an Enterprise DevSecOps Pipeline with Zero Developer Friction
- **Requirements**: Automate security checks for 1,500 developers deploying 200 times daily.
- **Architecture**: Fast pre-commit secret scanning (Gitleaks $< 2\text{s}$); parallelized pull request CI pipeline running Semgrep SAST and Snyk SCA ($< 3\text{ mins}$); Syft generates CycloneDX SBOM; Cosign signs container image using keyless GitHub OIDC identity. Kyverno validates signatures at cluster admission.
- **Decision**: Strict blocking gates enforced strictly on Critical CVEs with public exploits (EPSS $> 0.1$); advisory warnings on Medium CVEs to protect developer velocity.

## 3. Handle an Unannounced Regional Cloud Datacenter Outage
- **Scenario**: AWS `us-east-1` suffers a total network partition.
- **Architecture**: Route53 Anycast health checks detect regional ALB timeout within 15 seconds. DNS automatically shifts 100% of global traffic to `us-west-2` Warm Standby fleet. Aurora Global Database promotes secondary cluster to read-write primary in $< 60$ seconds.
- **Result**: Measured RTO of 4.5 minutes, RPO of 1.2 seconds, satisfying business Tier-1 commitments.
