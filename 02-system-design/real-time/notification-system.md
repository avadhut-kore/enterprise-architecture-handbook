# Notification System Architecture

## 1. Multi-Channel Notification Pipeline
Enterprise notification systems fan out events across multiple delivery channels (iOS APNS, Android FCM, SMS Twilio, Email SendGrid, Web Push).

```mermaid
flowchart TD
    Event[Domain Event: Order Shipped] --> Ingest[Notification API]
    Ingest --> PriorityQueue[Priority Kafka Topics: Critical / High / Low]
    PriorityQueue --> Dedup[Deduplication & Rate Limiter / User Preferences]
    
    Dedup --> WorkerAPNS[iOS APNS Worker]
    Dedup --> WorkerFCM[Android FCM Worker]
    Dedup --> WorkerSMS[SMS Twilio Worker]
    Dedup --> WorkerEmail[Email Worker]
```

---

## 2. Essential Reliability Controls
* **User Notification Settings**: Check user opt-in preferences and "Do Not Disturb" quiet hours (local timezone) before dispatch.
* **Rate Limiting & Digesting**: Prevent notifying a user 50 times in 1 minute; aggregate notifications into a single periodic digest (e.g., "Alice and 14 others liked your post").
