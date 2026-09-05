# Multi-AZ VPC / VNet CIDR Allocation Architecture

```text
VPC: 10.20.0.0/16
├── AZ-a:
│   ├── Public Subnet: 10.20.1.0/24
│   ├── Private App Subnet: 10.20.10.0/24
│   └── Private Data Subnet: 10.20.20.0/24
├── AZ-b:
│   ├── Public Subnet: 10.20.2.0/24
│   ├── Private App Subnet: 10.20.11.0/24
│   └── Private Data Subnet: 10.20.21.0/24
└── AZ-c:
    ├── Public Subnet: 10.20.3.0/24
    ├── Private App Subnet: 10.20.12.0/24
    └── Private Data Subnet: 10.20.22.0/24
```
