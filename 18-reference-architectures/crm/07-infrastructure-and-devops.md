# Infrastructure as Code & DevOps: Enterprise CRM

## 1. Multi-AZ Production Topology (Terraform Snippet)

```hcl
module "aurora_postgresql" {
  source  = "terraform-aws-modules/rds-aurora/aws"
  version = "~> 8.0"

  name           = "crm-production-cluster"
  engine         = "aurora-postgresql"
  engine_version = "15.4"
  instances = {
    writer = { instance_class = "db.r6g.2xlarge" }
    reader = { instance_class = "db.r6g.2xlarge" }
  }

  vpc_id  = module.vpc.vpc_id
  subnets = module.vpc.database_subnets
  storage_encrypted = true
  deletion_protection = true
}
```
