# Incident Severity Matrix & Paging SLAs

## Executive Summary

| Severity | Customer Impact | Target MTTM | Paging Policy | Update Frequency |
|:---|:---|:---:|:---|:---:|
| **SEV-1** | Core revenue-generating transaction down for $> 5\%$ of users | **$< 30\text{ mins}$** | Immediate 24/7 phone page to on-call + IC | Every 15 minutes |
| **SEV-2** | Critical service degraded; redundancy lost; major admin tool down | **$< 60\text{ mins}$** | Immediate 24/7 phone page to squad on-call | Every 30 minutes |
| **SEV-3** | Minor customer feature broken with acceptable workaround | **$< 4\text{ hours}$** | Business hours Slack alert / email | Daily |
| **SEV-4** | Cosmetic UI bug or minor internal operational defect | Next sprint | Jira ticket created | Standard sprint |
