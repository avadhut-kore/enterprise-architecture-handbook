# Business Application Header (BAH: head.001)

## 1. Role of the BAH
The Business Application Header (`head.001.001.03`) wraps the message payload, carrying routing, digital signature, and cryptographic envelope metadata without polluting the financial document body.

```xml
<AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.03">
  <Fr>
    <FIId><FinInstnId><BICFI>BOFAUS3NXXX</BICFI></FinInstnId></FIId>
  </Fr>
  <To>
    <FIId><FinInstnId><BICFI>CHASUS33XXX</BICFI></FinInstnId></FIId>
  </To>
  <BizMsgIdr>MSG-2026-991827</BizMsgIdr>
  <MsgDefIdr>pacs.008.001.10</MsgDefIdr>
  <CreDt>2026-09-05T12:00:00Z</CreDt>
</AppHdr>
```
