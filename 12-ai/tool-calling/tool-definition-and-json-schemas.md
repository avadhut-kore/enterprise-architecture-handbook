# Tool Definitions & JSON Schema Architecture

## 1. The Critical Role of Tool Descriptions

Foundation models select which tool to invoke based entirely on the **semantic text descriptions** provided in the tool schema. Vague or overlapping tool descriptions cause frequent tool misrouting and argument hallucination.

```json
{
  "name": "lookup_customer_balance",
  "description": "Retrieves the current cleared balance and credit limit for an enterprise customer. Use this ONLY for account balance inquiries. Do NOT use this tool for pending wire transfer statuses.",
  "parameters": {
    "type": "object",
    "properties": {
      "customer_id": {
        "type": "string",
        "pattern": "^CUST-[0-9]{6}$",
        "description": "The unique enterprise customer identifier, formatted as 'CUST-' followed by 6 digits."
      },
      "include_credit_limit": {
        "type": "boolean",
        "description": "Whether to include available credit line details in response.",
        "default": false
      }
    },
    "required": ["customer_id"],
    "additionalProperties": false
  }
}
```

---

## 2. Invariants for Production Tool Schemas
1. **Always Set `additionalProperties: false`**: Prevents the model from hallucinating non-existent parameters that could crash backend endpoints.
2. **Explicit Regex Patterns**: Provide format constraints (`pattern: "^[A-Z]{3}-[0-9]+$"`) to force the model to adhere to enterprise ID formats.
