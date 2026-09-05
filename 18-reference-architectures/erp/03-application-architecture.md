# Application Architecture: Enterprise ERP

## 1. Automated Three-Way Matching Engine
Before an Accounts Payable vendor invoice is approved for disbursement:
1. **Purchase Order (PO)**: Validates quantities, unit prices, and payment terms approved by purchasing.
2. **Goods Receipt (GR)**: Validates physical delivery quantities confirmed by warehouse receiving.
3. **Vendor Invoice (VI)**: Validates billed amounts.
- If $(\text{PO Price} == \text{VI Price})$ and $(\text{GR Quantity} == \text{VI Quantity})$ within configured tolerance ($\le 0.5\%$), the invoice is auto-posted to the General Ledger without human intervention.
