from fastapi import FastAPI
import requests

app = FastAPI()
ATLAS_BASE = "http://<atlas-host>:21000/api/atlas/v2"
ATLAS_AUTH = ('admin', 'admin')

@app.get("/search")
def search(q: str):
    resp = requests.get(f"{ATLAS_BASE}/search/basic?query={q}", auth=ATLAS_AUTH)
    return resp.json()