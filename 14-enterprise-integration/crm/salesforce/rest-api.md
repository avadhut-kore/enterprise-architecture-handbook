# Salesforce REST API and Composite Resources

## 1. Composite API Architecture
To avoid exhausting API limits with chatty calls, use the **Composite API** to execute up to 25 dependent subrequests in a single HTTP payload:
```http
POST /services/data/v58.0/composite HTTP/1.1
Host: yourinstance.my.salesforce.com
Content-Type: application/json

{
  "compositeRequest": [
    {
      "method": "POST",
      "url": "/services/data/v58.0/sobjects/Account",
      "referenceId": "newAccount",
      "body": { "Name": "Acme Corp" }
    },
    {
      "method": "POST",
      "url": "/services/data/v58.0/sobjects/Contact",
      "referenceId": "newContact",
      "body": {
        "LastName": "Smith",
        "AccountId": "@{newAccount.id}"
      }
    }
  ]
}
```
