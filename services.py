from typing import Any
 
import requests
from fastapi import FastAPI, HTTPException
 
app = FastAPI()
 
GITHUB_STATUS_URL = "https://www.githubstatus.com/api/v2/status.json"
 
@app.get("/")
def get_github_status() -> dict[str, Any]:
    try:
        response = requests.get(GITHUB_STATUS_URL, timeout=5)
        response.raise_for_status()
        return response.json()
 
    except requests.exceptions.RequestException as exc:
        raise HTTPException(
            status_code=503,
            detail="Could not get GitHub status.",
        ) from exc
 