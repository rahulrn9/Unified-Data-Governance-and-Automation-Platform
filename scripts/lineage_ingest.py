import pandas as pd, requests, json

# Configuration
LOG_PATH = "metadata_logs.csv"
ATLAS_BASE = "http://<atlas-host>:21000/api/atlas/v2"
ATLAS_AUTH = ('admin', 'admin')

# Load logs
df = pd.read_csv(LOG_PATH)  # should have columns: source_guid, target_guid, timestamp

for _, row in df.iterrows():
    proc = {
      "entity": {
        "typeName": "Process",
        "attributes": {
          "name": f"etl_{row.source_guid}_to_{row.target_guid}_{row.timestamp}",
          "qualifiedName": f"etl::{row.source_guid}::{row.target_guid}::{row.timestamp}"
        },
        "relationshipAttributes": {
          "inputs": [{"guid": row.source_guid}],
          "outputs": [{"guid": row.target_guid}]
        }
      }
    }
    requests.post(f"{ATLAS_BASE}/entity", auth=ATLAS_AUTH,
                  headers={"Content-Type":"application/json"},
                  data=json.dumps(proc)).raise_for_status()