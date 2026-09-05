# Application vs Infrastructure Configuration

## Executive Summary

Conflating application configuration with infrastructure configuration creates massive delivery friction. Modifying a business timeout or feature toggle should not require a 20-minute Terraform deployment.

---

## 1. Separation Matrix

| Dimension | Infrastructure Configuration | Application Configuration |
| :--- | :--- | :--- |
| **Lifespan** | Long-lived (Months to Years) | Ephemeral / Dynamic (Days to Minutes) |
| **Tooling** | Terraform, Bicep, CloudFormation | AWS AppConfig, LaunchDarkly, Consul, ConfigMaps |
| **Change Frequency** | Low (Weekly / Monthly releases) | High (Multiple times per day) |
| **Deployment Gate** | Full IaC pipeline + security scanning | Real-time dynamic poll or lightweight reload |
| **Examples** | VPC CIDRs, DB instance size, KMS key IDs | Feature flags, HTTP timeouts, circuit breaker thresholds |
