# Tenant-Aware Rate Limiting

## 1. Tiered Fair-Share Quotas
Rate limiting must evaluate both global limits and subscription-tier tenant limits:
* Free Tier: Max $10\text{ RPS}$, $1,000\text{ calls/day}$.
* Pro Tier: Max $100\text{ RPS}$, $50,000\text{ calls/day}$.
* Enterprise Tier: Max $2,000\text{ RPS}$, unlimited daily volume.

```lua
-- Redis Lua Token Bucket by Tenant
local key = "rate:tenant:" .. KEYS[1]
local limit = tonumber(ARGV[1])
local current = redis.call("INCR", key)
if current == 1 then
    redis.call("EXPIRE", key, 60)
end
if current > limit then
    return 0 -- Rejected
end
return 1 -- Allowed
```
