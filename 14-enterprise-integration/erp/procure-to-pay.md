# Procure-to-Pay (P2P) Integration Architecture

## 1. P2P Integration Phases
1. **Requisition & Purchase Order (PO)**: Initiated in Ariba/Coupa, synced to ERP (`PO_CREATED`).
2. **Goods Receipt (GR)**: Logged at loading dock via mobile RFID scanner.
3. **Invoice Receipt (IR)**: Ingested via OCR / Peppol e-invoicing network.
4. **Three-Way Matching**: Automated validation:
   $$	ext{PO Quantity} == 	ext{GR Quantity} == 	ext{IR Quantity}$$
   $$	ext{PO Unit Price} == 	ext{IR Unit Price}$$
5. **Payment Disbursement**: Transmitted via ISO 20022 `pain.001` XML to corporate bank.
