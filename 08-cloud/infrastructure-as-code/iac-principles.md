# Infrastructure as Code Principles: Declarative vs Imperative

## Executive Summary

Enterprise cloud infrastructure must be provisioned using **declarative**, **idempotent**, and **immutable** mechanisms.

---

## 1. Declarative vs Imperative Comparison

```mermaid
graph TD
    subgraph Imperative: How to do it (Scripts: Bash / AWS CLI)
        Step1[1. Run 'aws ec2 run-instances'] --> Step2[2. Wait 30 seconds]
        Step2 --> Step3[3. Run 'aws ec2 create-tags']
        Step3 --> Failure[If Step 2 crashes: SCRIPT FAILS HALFWAY / ORPHANED RESOURCES!]
    end

    subgraph Declarative: What the end state should be (Terraform / Bicep)
        Desired[Desired State: '3 EC2 Instances with Tag Environment=Prod']
        Desired --> Engine[Engine Calculates Diff between Actual and Desired State]
        Engine --> Converge[Converges State Idempotently]
    end
```

---

## 2. The Three Invariant Rules of Enterprise IaC

1. **Idempotency**: Running the IaC pipeline ten times consecutively against an existing environment must produce the exact same result as running it once, without making any modifications if no drift has occurred.
2. **Immutability**: Rather than executing configuration management scripts (Ansible/Puppet) to mutate live production servers in-place, IaC destroys old instances and instantiates new immutable instances.
3. **No Out-of-Band Modifications**: Manual modifications executed directly inside the AWS Management Console or Azure Portal are strictly forbidden. Any manual change will be overwritten during the next automated IaC execution.
