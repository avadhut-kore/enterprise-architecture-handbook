# Mapping Legacy Financial Formats to ISO 20022

## 1. The SWIFT MT to MX Migration Matrix

| Legacy MT Message | ISO 20022 MX Equivalent | Mapping Complexities |
| :--- | :--- | :--- |
| **MT103** (Single Customer Credit Transfer) | `pacs.008.001.10` | MT103 unstructured Field 59/70 must be parsed into structured street/city XML tags |
| **MT202** (General Financial Transfer) | `pacs.009.001.09` | Cover payments require `pacs.009.COV` variant |
| **MT940** (Customer Statement) | `camt.053.001.10` | Character truncation issues resolved; balance types mapped to ISO codes |
| **NACHA CCD / PPD** | `pacs.008` / `pain.008` | Fixed-width 94-char records converted to XML hierarchical trees |
