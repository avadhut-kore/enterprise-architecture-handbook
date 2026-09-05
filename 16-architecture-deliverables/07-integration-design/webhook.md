# Webhook Ingestion Standards
* Verify HMAC-SHA256 signatures immediately in the ingress filter before parsing payload JSON.
* Acknowledge webhook with `200 OK` within 2,000ms; delegate actual processing to an async background worker.
