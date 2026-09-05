# Case Study 06: Legacy Mainframe & Cloud Distributed Tracing

## 1. Executive Summary
A Tier-1 retail bank was executing a core banking modernization program, migrating its frontend digital channels to AWS while retaining its **IBM z/OS Mainframe (CICS, DB2, and COBOL)** as the central system of record. 

When digital transactions experienced intermittent 10-second delays, cloud engineers blamed the mainframe team, while mainframe systems programmers insisted their CICS response times were nominal ($< 20\text{ms}$).

The bank bridged this cultural and technical divide by implementing **Unified OpenTelemetry Tracing over IBM MQ RFH2 Headers**, providing the world's first single-pane trace spanning from an iPhone app to a mainframe COBOL copybook.

---

## 2. End-to-End Mainframe Trace Flow

```mermaid
sequenceDiagram
    autonumber
    participant Mobile as Banking Mobile App
    participant CloudGateway as AWS API Gateway (Envoy)
    participant AccountSvc as Account Microservice (Spring Boot)
    participant MQ as IBM MQ On-Premises Queue Manager
    participant CICS as IBM z/OS Mainframe (CICS / COBOL)

    Mobile->>CloudGateway: Transfer $500 (traceparent injected)
    CloudGateway->>AccountSvc: Forward Transfer Request
    Note over AccountSvc: Starts OpenTelemetry Span: "InitiateWireTransfer"
    AccountSvc->>MQ: Enqueue MQ Message\n(Injects W3C traceparent into MQ RFH2 Header)
    Note over MQ: MQ Channel transit over DirectConnect (WAN Latency)
    MQ->>CICS: Trigger CICS Transaction 'TX01'
    Note over CICS: COBOL Program reads RFH2 header;<br/>Records CPU Microseconds & DB2 wait time
    CICS-->>MQ: Return Response with Transaction Performance Block
    MQ-->>AccountSvc: Dequeue Response
    Note over AccountSvc: Enriches Span: mainframe.cics_cpu_ms=18, mainframe.db2_wait_ms=12
    AccountSvc-->>CloudGateway: Return Success
    CloudGateway-->>Mobile: Transfer Complete
```

---

## 3. The Uncovered Root Cause
Distributed tracing instantly resolved the 10-second mystery:
- **Cloud Microservice execution**: 45ms.
- **Mainframe COBOL execution**: 18ms.
- **The Culprit**: **IBM MQ Queue Depth Saturation on the on-premises gateway**. MQ channel listener threads were starved for connections due to an outdated TCP buffer configuration, causing messages to sit idle in the inbound transmission queue for 9.8 seconds before being delivered to CICS!

---

## 4. Quantitative Results

| Operational Dimension | Before Mainframe Tracing | After Mainframe Tracing |
| :--- | :--- | :--- |
| **Cross-Team Mean Time to Innocent (MTTI)** | 3.5 Days of War-Room Arguing | **Instant (< 60 Seconds)** |
| **Mainframe Capacity Billing (MIPS)** | Uncorrelated with specific APIs | **Directly mapped to digital channel endpoints** |
| **Migration Risk Confidence** | Low (Fear of breaking legacy core) | **High (100% side-by-side transaction validation)** |
