# Case Study: SSRF Cloud Metadata IAM Credential Exfiltration & 120TB Breach

> **Metadata**: ID: `CS-SEC-02` | Domain: Security / Cloud Infrastructure | Type: Synthetic Forensic Case Study | Complexity: Expert

---

## 01. Executive Summary
A leading enterprise SaaS document analytics provider suffered a catastrophic data breach resulting in the exfiltration of **120 Terabytes of encrypted customer contracts and financial records** stored in Amazon S3. An attacker exploited a **Server-Side Request Forgery (SSRF)** vulnerability in the platform's custom "Export via Webhook" feature. By passing a crafted URL pointing to the unauthenticated AWS Instance Metadata Service (**IMDSv1: `http://169.254.169.254`**), the attacker extracted temporary IAM role credentials assigned to the EC2 container node. Because the node's IAM role was grossly over-permissioned (`AmazonS3FullAccess`), the attacker utilized the stolen credentials to sync entire S3 buckets directly to an external server.

---

## 02. Business & System Context
- **Organization**: Enterprise LegalTech & Document Intelligence SaaS ($120M ARR).
- **Core Workflow**: Customer Contract Ingestion, Optical Character Recognition (OCR), and S3 Storage.
- **Scale**: 850 Fortune 500 Enterprise Customers; 45 Million confidential PDF contracts.

---

## 03. Scope & Stakeholders
- **Incident Commander**: Lead Cloud Security Architect.
- **Key Teams**: Security Operations Center (SOC), Cloud Infrastructure Team, Outside Forensic Counsel.
- **External Dependencies**: AWS Security Team, FBI Cyber Division.

---

## 04. Requirements & NFRs
- **Zero Trust Cloud Boundaries**: Application pods must never be capable of accessing cloud hypervisor metadata.
- **Least Privilege Access**: IAM roles must be strictly scoped to specific S3 object prefixes.
- **Egress Network Filtering**: Restrict outbound pod connections to authorized customer webhook endpoints.

---

## 05. Constraints & Assumptions
- **The "Internal IP is Safe" Fallacy**: The development squad used a naive regex to validate webhook URLs, blocking `localhost` and `127.0.0.1` but failing to block link-local addresses (`169.254.169.254`) or DNS rebinding bypasses.

---

## 06. Architecture Before: The SSRF Metadata Exploit
```mermaid
graph TD
    Attacker[Attacker Browser] --> SaaS[SaaS Web App]
    
    subgraph Vulnerable Cloud Compute Tier (AWS EC2 / EKS)
        SaaS --> WebhookWorker[Webhook Export Microservice]
        WebhookWorker --> NaiveValidator[Flawed Regex Validator: Fails to block 169.254.169.254!]
        
        WebhookWorker -->|SSRF GET http://169.254.169.254/latest/meta-data/iam/security-credentials/| IMDS[AWS IMDSv1: No Token Required!]
        IMDS -->|Returns Temporary AccessKey, SecretKey & Token| WebhookWorker
    end
    
    WebhookWorker -->|Dumps Creds into Webhook Response Body!| Attacker
    
    subgraph Stolen IAM Credential Misuse (Over-Permissioned!)
        Attacker -->|Direct AWS CLI: aws s3 sync s3://customer-contracts/| S3Bucket[(AWS S3: AmazonS3FullAccess)]
        S3Bucket -->|Exfiltrates 120 Terabytes of Data!| Drop[(Attacker Server)]
    end
```

---

## 07. Architecture Decisions
| Decision | Rationale | Downstream Failure |
| :--- | :--- | :--- |
| **AWS IMDSv1 Default Enabled** | Legacy cloud configuration carried over from early EC2 deployments. | IMDSv1 requires no authentication headers; simple HTTP GET requests from any SSRF vulnerability can extract instance credentials. |
| **Node-Level IAM Role with `S3FullAccess`** | Easy for developers: avoided configuring fine-grained IAM Roles for Service Accounts (IRSA). | A compromise of any single microservice on the node granted full admin access to all S3 buckets across the company. |

---

## 08. Timeline
```mermaid
timeline
    title SSRF Metadata Breach Timeline
    Day 1, 04:00 : Attacker creates free trial account on SaaS platform
    Day 1, 04:45 : Attacker tests Webhook Export: submits `http://169.254.169.254/latest/meta-data/`
    Day 1, 04:47 : Response returns AWS IAM role name: `AppClusterNodeRole`
    Day 1, 05:00 : Attacker extracts `AccessKeyId`, `SecretAccessKey`, and `Token`
    Day 1, 06:15 : Attacker configures AWS CLI; initiates `aws s3 sync s3://prod-customer-docs/`
    Day 3, 18:00 : AWS GuardDuty flags anomalous egress volume from external IP; SOC alerted
    Day 3, 19:30 : 120 Terabytes confirmed exfiltrated; IAM credentials revoked
```

---

## 09. Incident Event
The attacker registered a trial account and navigated to "Export Webhooks." The user was prompted to provide a webhook URL. The attacker entered `http://169.254.169.254/latest/meta-data/iam/security-credentials/AppClusterNodeRole`. The application's URL validator only checked that the string began with `http://` and did not contain `localhost`. The backend service dispatched an HTTP GET request to the link-local address. Because IMDSv1 did not require an authentication token, the AWS metadata service returned full temporary AWS credentials in the HTTP response body, which the webhook debugger displayed on the attacker's screen. The attacker ran `aws s3 sync` from an external server, exfiltrating 120TB of confidential data over 60 hours.

---

## 10. Symptoms & Evidence
- **Fact**: Amazon GuardDuty generated alert `UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.OutsideAWS`.
- **Fact**: AWS CloudTrail logs showed 850,000 `S3:GetObject` API calls originating from an unfamiliar DigitalOcean IP address using temporary role credentials assigned to an EC2 instance.
- **Inference**: Cloud infrastructure security cannot rely on application-level URL parsing; it must be enforced at the cloud metadata and IAM boundary.

---

## 11. Failure Forensics
```
[Attacker enters Webhook URL: http://169.254.169.254/.../security-credentials/]
                               │
                               ▼
[Backend server executes: http.Get("http://169.254.169.254/...")]
                               │
                               ▼
[AWS Hypervisor IMDSv1 responds with STS Session Credentials]
                               │
                               ▼
[App echoes response to UI: AWS_ACCESS_KEY_ID & AWS_SECRET_ACCESS_KEY]
                               │
                               ▼
[Attacker runs AWS CLI from home: Over-permissioned Role allows S3 Read]
                               │
                               ▼
[120 Terabytes of Customer Contracts Exfiltrated Directly from S3]
```

---

## 12. Root Cause Analysis (5-Whys)
1. **Why was customer data stolen?** -> An external attacker executed `S3:GetObject` calls using legitimate AWS IAM credentials.
2. **Why did the attacker have IAM credentials?** -> The credentials were stolen via an SSRF vulnerability accessing the AWS metadata service.
3. **Why did the metadata service give credentials to an HTTP GET request?** -> The instance used IMDSv1 instead of session-token-enforced IMDSv2.
4. **Why could the stolen role credentials access all S3 buckets?** -> The instance was assigned a broad, node-level `AmazonS3FullAccess` policy instead of least-privilege pod-scoped roles.
5. **Why was the pod allowed to reach the metadata IP?** -> Kubernetes lacked network policies blocking egress traffic to the link-local IP `169.254.169.254/32`.

---

## 13. Contributing Factors
- **Failure to Adopt IMDSv2**: AWS released IMDSv2 (requiring a `PUT` token handshake) in 2019, yet the infrastructure team left IMDSv1 active across all production AMIs.
- **No Egress Network Policy**: Kubernetes pods had unrestricted egress access to all internal VPC and link-local networks.

---

## 14. Architecture After: IMDSv2, IRSA & Calico Egress Guardrails
```mermaid
graph TD
    Attacker[Malicious User] --> SaaS[SaaS Web App]
    
    subgraph Hardened Container Environment (Zero Trust)
        SaaS --> Pod[Webhook Worker Pod]
        
        subgraph Calico Network Policy (Firewall)
            Pod -.->|BLOCKED: Egress to 169.254.169.254 REJECTED!| Drop[Drop Packet]
        end
        
        subgraph AWS IMDSv2 (Session Token Required)
            Pod -.->|Requires PUT X-aws-ec2-metadata-token| IMDSv2[IMDSv2 Protected]
        end
        
        Pod -->|Least Privilege IRSA: Only /exports/ Prefix| S3[(Amazon S3)]
    end
```

---

## 15. Recovery & Remediation
- **Immediate Mitigation**: Revoked the compromised IAM role sessions in AWS IAM; deactivated the webhook export endpoint.
- **Permanent Architectural Fix**:
  - **Enforce IMDSv2 Globally**: Applied an AWS Organization Service Control Policy (SCP) mandating `HttpTokens=required` across all EC2 instances, completely neutralizing simple GET-based SSRF metadata attacks:
    ```json
    {"ec2:Attribute/HttpTokens": "required"}
    ```
  - **Egress Network Policies**: Deployed **Calico NetworkPolicies** in Kubernetes explicitly blocking traffic to `169.254.169.254/32` from all application workloads.
  - **IAM Roles for Service Accounts (IRSA)**: Eliminated node-level IAM roles. Each Kubernetes pod now assumes a strictly scoped role granting access only to its specific tenant prefix (`s3://bucket/tenant-id/*`).

---

## 16. Business & Technical Impact
- **Financial**: $25M enterprise liability insurance claim; $8M in legal defense and forensic compliance costs.
- **Customer Churn**: 32 Enterprise Fortune 500 customers cancelled contracts within 90 days of mandatory breach disclosure.
- **Compliance**: Undertook full SOC 2 Type II audit recertification and federal regulatory reporting.

---

## 17. What Went Well
- GuardDuty anomaly alerts triggered within 18 hours of large-scale exfiltration, allowing containment before all 400TB of data was stolen.
- S3 server access logs were intact, enabling investigators to provide every customer with an exact list of compromised documents.

---

## 18. Lessons Learned
- **Architecture**: Defense in depth is non-negotiable. Application URL validation will eventually fail; cloud metadata services must be protected by network policies and IMDSv2.
- **Least Privilege**: Never attach broad S3 permissions to a shared compute node. Always use pod-level identity (IRSA / Workload Identity).

---

## 19. Architectural Recommendations
| Horizon | Action Item | Owner | Target |
| :--- | :--- | :--- | :--- |
| **Immediate** | Mandate IMDSv2 (`HttpTokens=required`) across 100% of AWS EC2 instances | Cloud Sec Lead | Zero IMDSv1 instances |
| **30 Days** | Deploy Calico network policies blocking `169.254.169.254` across all clusters | Platform SRE | 100% pod egress block |
| **60 Days** | Migrate all application workloads to IAM Roles for Service Accounts (IRSA) | Lead EA | Zero node-level roles |
