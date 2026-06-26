from typing import Any
import time
 
import requests
from fastapi import FastAPI, HTTPException
 
app = FastAPI()
 
GITHUB_STATUS_URL = "https://www.githubstatus.com/api/v2/status.json"
MAX_RETRIES = 5
RETRY_DELAY_SECONDS = 0.1
TIMEOUT_SECONDS = 5
 
 
@app.get("/")
def get_github_status() -> dict[str, Any]:
    last_error_detail = "Unknown error"
 
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(
                GITHUB_STATUS_URL,
                timeout=TIMEOUT_SECONDS,
            )
 
            response.raise_for_status()
            return response.json()
 
        except requests.exceptions.ConnectTimeout as exc:
            last_error_detail = (
                f"Connection timeout while connecting to GitHub Status API. "
                f"Attempt {attempt}/{MAX_RETRIES}. Error: {exc}"
            )
 
        except requests.exceptions.ReadTimeout as exc:
            last_error_detail = (
                f"Read timeout while waiting for GitHub Status API response. "
                f"Attempt {attempt}/{MAX_RETRIES}. Error: {exc}"
            )
 
        except requests.exceptions.ConnectionError as exc:
            last_error_detail = (
                f"Connection error while calling GitHub Status API. "
                f"Attempt {attempt}/{MAX_RETRIES}. Error: {exc}"
            )
 
        except requests.exceptions.SSLError as exc:
            raise HTTPException(
                status_code=502,
                detail=f"SSL error while connecting to GitHub Status API: {exc}",
            ) from exc
 
        except requests.exceptions.TooManyRedirects as exc:
            raise HTTPException(
                status_code=502,
                detail=f"Too many redirects while calling GitHub Status API: {exc}",
            ) from exc
 
        except requests.exceptions.HTTPError as exc:
            status_code = exc.response.status_code if exc.response else None
 
            if status_code is not None and 500 <= status_code < 600:
                last_error_detail = (
                    f"GitHub Status API returned server error {status_code}. "
                    f"Attempt {attempt}/{MAX_RETRIES}. Error: {exc}"
                )
            else:
                raise HTTPException(
                    status_code=502,
                    detail=f"GitHub Status API returned HTTP error {status_code}: {exc}",
                ) from exc
 
        except requests.exceptions.JSONDecodeError as exc:
            raise HTTPException(
                status_code=502,
                detail=f"GitHub Status API returned an invalid JSON response: {exc}",
            ) from exc
 
        except requests.exceptions.RequestException as exc:
            last_error_detail = (
                f"Unexpected request error while calling GitHub Status API. "
                f"Attempt {attempt}/{MAX_RETRIES}. Error: {exc}"
            )
 
        if attempt < MAX_RETRIES:
            time.sleep(RETRY_DELAY_SECONDS)
 
    raise HTTPException(
        status_code=503,
        detail=f"Could not get GitHub status after {MAX_RETRIES} attempts. Last error: {last_error_detail}",
    )