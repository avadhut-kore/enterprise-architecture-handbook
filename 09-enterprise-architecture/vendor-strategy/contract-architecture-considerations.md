# Contract Architecture Considerations for Enterprise Architects

Key legal and architectural clauses that enterprise architects must mandate during vendor contract negotiations.

---

## 1. Mandatory Architectural Contract Clauses
1. **Unrestricted Data Ownership**: All data, metadata, schemas, and AI-derived embeddings remain the exclusive property of the enterprise. Vendor has zero rights to use customer data for model training.
2. **Standardized Data Extraction at Contract End**: Vendor must provide full data export in standard open formats (JSON, Parquet, CSV) within 30 days of termination at zero additional extraction fee.
3. **Availability SLAs with Real Financial Penalties**: Minimum 99.95% monthly uptime backed by cascading fee credits (e.g., 25% credit for <99.9%, 50% credit for <99.0%).
4. **Source Code Escrow**: For critical on-premises software vendors, source code must be held in third-party escrow (e.g., Iron Mountain) and released if the vendor files for bankruptcy.
