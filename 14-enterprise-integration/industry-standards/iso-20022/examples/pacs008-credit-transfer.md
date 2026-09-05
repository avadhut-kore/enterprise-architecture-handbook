# Implementation Example: pacs.008 Customer Credit Transfer

## 1. Production XML Schema Snippet
```xml
<?xml version="1.0" encoding="UTF-8"?>
<BusMsg xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.03">
  <AppHdr>
    <Fr><FIId><FinInstnId><BICFI>BOFAUS3NXXX</BICFI></FinInstnId></FIId></Fr>
    <To><FIId><FinInstnId><BICFI>CHASUS33XXX</BICFI></FinInstnId></FIId></To>
    <BizMsgIdr>MSG-2026-09-05-001</BizMsgIdr>
    <MsgDefIdr>pacs.008.001.10</MsgDefIdr>
    <CreDt>2026-09-05T12:00:00Z</CreDt>
  </AppHdr>
  <Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.10">
    <FIToFICstmrCdtTrf>
      <GrpHdr>
        <MsgId>GRP-20260905-99182</MsgId>
        <CreDtTm>2026-09-05T12:00:00Z</CreDtTm>
        <NbOfTxs>1</NbOfTxs>
        <SttlmInf>
          <SttlmMtd>CLRG</SttlmMtd>
        </SttlmInf>
      </GrpHdr>
      <CdtTrfTxInf>
        <PmtId>
          <EndToEndId>E2E-2026-001</EndToEndId>
          <UETR>a9b8c7d6-1234-4567-89ab-cdef01234567</UETR>
        </PmtId>
        <IntrBkSttlmAmt Ccy="USD">1500.00</IntrBkSttlmAmt>
        <Dbtr>
          <Nm>Acme Global Corporation</Nm>
        </Dbtr>
        <Cdtr>
          <Nm>Apex Industrial Supplies</Nm>
        </Cdtr>
      </CdtTrfTxInf>
    </FIToFICstmrCdtTrf>
  </Document>
</BusMsg>
```
