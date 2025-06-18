import json

# Mock implementation - extend to parse actual audit logs
log_file = "audit_logs.json"
with open(log_file) as f:
    logs = json.load(f)

# Aggregate usage metrics
usage = {}
for entry in logs:
    asset = entry['asset']
    usage[asset] = usage.get(asset, 0) + 1

print("Usage summary:", usage)