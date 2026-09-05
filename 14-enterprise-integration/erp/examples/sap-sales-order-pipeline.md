# Implementation Example: SAP S/4HANA Sales Order Creation

## 1. Architecture Context
This service exposes a lightweight REST endpoint to web checkout, verifies inventory availability against a local cache, and calls the SAP S/4HANA OData API (`API_SALES_ORDER_SRV`) using OAuth 2.0.

## 2. Python SAP OData Integration Client
```python
import requests
from requests.auth import HTTPBasicAuth

SAP_HOST = "https://my-s4hana.enterprise.internal"
ODATA_ENDPOINT = f"{SAP_HOST}/sap/opu/odata/sap/API_SALES_ORDER_SRV"

def create_sap_sales_order(order_data: dict, auth_token: str) -> dict:
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    # Step 1: Fetch CSRF Token
    token_resp = requests.get(
        f"{ODATA_ENDPOINT}/$metadata",
        headers={**headers, "X-CSRF-Token": "Fetch"}
    )
    csrf_token = token_resp.headers.get("X-CSRF-Token")
    cookies = token_resp.cookies

    # Step 2: Post Sales Order Payload
    headers["X-CSRF-Token"] = csrf_token
    payload = {
        "SalesOrderType": "OR",
        "SalesOrganization": "1000",
        "DistributionChannel": "10",
        "OrganizationDivision": "00",
        "SoldToParty": order_data["customer_id"],
        "PurchaseOrderByCustomer": order_data["client_order_ref"],
        "to_Item": [{
            "Material": item["sku"],
            "RequestedQuantity": str(item["qty"]),
            "RequestedQuantityUnit": "EA"
        } for item in order_data["items"]]
    }
    
    resp = requests.post(
        f"{ODATA_ENDPOINT}/A_SalesOrder",
        json=payload,
        headers=headers,
        cookies=cookies
    )
    resp.raise_for_status()
    return resp.json()["d"]
```
