# Implementation Example: Salesforce to ERP Account Sync Bridge

## 1. Change Data Capture Subscriber (Python)
```python
import json
from cometd import Client

BAYEUX_URL = "https://my-enterprise.my.salesforce.com/cometd/58.0"

def listen_to_cdc():
    client = Client(BAYEUX_URL)
    # Authenticate with OAuth Bearer Token
    client.headers = {"Authorization": "Bearer oauth_token_here"}
    
    # Subscribe to Account Change Data Capture channel
    client.subscribe("/data/AccountChangeEvent")
    
    for message in client.listen():
        payload = message["data"]["payload"]
        change_type = payload["ChangeEventHeader"]["changeType"]
        record_ids = payload["ChangeEventHeader"]["recordIds"]
        
        if change_type == "CREATE":
            print(f"New Account created: {record_ids}, syncing to ERP...")
            # Forward payload to Kafka topic: crm.account.events
```
