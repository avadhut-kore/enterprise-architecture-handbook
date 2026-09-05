# The pacs Domain: Clearing and Settlement Messages

## 1. Deep-Dive: pacs.008 (Customer Credit Transfer)
The `pacs.008` is the workhorse of interbank settlement, moving funds from a debtor bank to a creditor bank on behalf of a retail or commercial client.

### Essential Business Fields
- `GrpHdr/MsgId`: Unique clearing batch identifier.
- `PmtId/EndToEndId`: End-to-end identifier passed unmodified from originator to beneficiary.
- `PmtId/UETR`: Unique End-to-end Transaction Reference (UUIDv4) tracked across SWIFT gpi.
- `IntrBkSttlmAmt`: Interbank settlement amount and ISO currency code.
- `Dbtr / Cdtr`: Debtor and Creditor party details.
