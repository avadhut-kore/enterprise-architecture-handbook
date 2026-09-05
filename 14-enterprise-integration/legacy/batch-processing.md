# Mainframe Batch Windows and Event Bridges

## 1. The Dual-Speed Bridge Pattern
```
[Cloud Real-Time Channel] ──> [Memo-Post Cache] (Serves immediate customer balance)
                                     │
                                     ▼ (Accumulates daytime transactions)
                            [Staging Outbox Table]
                                     │
                                     ▼ (Triggered at 02:00 AM)
                            [Generate Mainframe Batch File]
                                     │
                                     ▼
                            [Mainframe JCL Batch Job]
```
