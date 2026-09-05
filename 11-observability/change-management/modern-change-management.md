# Modern Change Management: Standard vs Normal vs Emergency

## Executive Summary

| Change Category | Risk Level | Approval Mechanism | Deployment Window | Target Volume |
|:---|:---:|:---|:---:|:---:|
| **Standard Change** | Low / Pre-approved | 100% Automated CI/CD pipeline tests | Continuous (24/7) | **$\ge 80\%$** of all releases |
| **Normal Change** | Moderate / Complex | Peer Architect Review + Automated CI/CD | Low-traffic maintenance window | $\sim 15\%$ |
| **Emergency Change** | Critical Fix | Incident Commander + Tech Lead verbal | Immediate during active outage | $< 5\%$ |
