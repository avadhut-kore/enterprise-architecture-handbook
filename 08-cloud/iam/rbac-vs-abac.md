# RBAC vs ABAC: Scaling Enterprise Cloud Authorization

## Executive Summary

As an enterprise grows from tens of microservices to thousands, **Role-Based Access Control (RBAC)** suffers from "role explosion." **Attribute-Based Access Control (ABAC)** solves this by evaluating dynamic metadata attributes.

---

## 1. Role Explosion vs Dynamic ABAC

```mermaid
graph TD
    subgraph Role Explosion: RBAC [UNMAINTAINABLE AT SCALE]
        R1[Role: Payments-Dev-Engineer]
        R2[Role: Payments-Prod-Engineer]
        R3[Role: Inventory-Dev-Engineer]
        R4[Role: Inventory-Prod-Engineer]
        R5[Result: 5,000 Bespoke Roles to Maintain!]
    end

    subgraph Dynamic ABAC: Single Policy [SCALABLE]
        ABACPolicy[Allow Action IF Principal.Tag.Project == Resource.Tag.Project AND Principal.Tag.Env == Resource.Tag.Env]
    end
```

---

## 2. ABAC Implementation in AWS IAM

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["ec2:StartInstances", "ec2:StopInstances"],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Project": "${aws:PrincipalTag/Project}",
          "aws:ResourceTag/Environment": "${aws:PrincipalTag/Environment}"
        }
      }
    }
  ]
}
```
*A single ABAC policy governs access across thousands of engineers and resources based strictly on resource tags.*
