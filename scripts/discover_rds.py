import psycopg2, requests, json

# Configuration
CONN = psycopg2.connect(host='your-rds-endpoint', port=5432, dbname='yourdb', user='username', password='password')
ATLAS_BASE = "http://<atlas-host>:21000/api/atlas/v2"
ATLAS_AUTH = ('admin', 'admin')

def list_tables(schema='public'):
    cur = CONN.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = %s;", (schema,))
    return [row[0] for row in cur.fetchall()]

def register_rds_table(table_name):
    payload = {
      "entity": {
        "typeName": "rdbms_table",
        "attributes": {
          "name": table_name,
          "qualifiedName": f"{table_name}@yourdb",
          "dbName": "yourdb"
        }
      }
    }
    requests.post(f"{ATLAS_BASE}/entity", auth=ATLAS_AUTH,
                  headers={"Content-Type":"application/json"},
                  data=json.dumps(payload)).raise_for_status()

if __name__ == "__main__":
    for tbl in list_tables():
        register_rds_table(tbl)
        print(f"Registered RDS table: {tbl}")