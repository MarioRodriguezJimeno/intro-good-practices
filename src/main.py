from typing import Any
import asyncio
 
import httpx
from fastapi import FastAPI, HTTPException
 
app = FastAPI()
 
GITHUB_STATUS_URL = "https://www.githubstatus.com/api/v2/status.json"
MAX_RETRIES = 5
RETRY_DELAY_SECONDS = 0.1
TIMEOUT_SECONDS = 5.0
 
 
@app.get("/")
async def get_github_status() -> dict[str, Any]:
    last_error_detail: str | None = None
 
    async with httpx.AsyncClient(timeout=TIMEOUT_SECONDS) as client:
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = await client.get(GITHUB_STATUS_URL)
                response.raise_for_status()
                return response.json()
 
            except httpx.ConnectTimeout as exc:
                last_error_detail = (
                    f"Connection timeout while connecting to GitHub Status API. "
                    f"Attempt {attempt}/{MAX_RETRIES}. Error: {exc}"
                )
 
            except httpx.ReadTimeout as exc:
                last_error_detail = (
                    f"Read timeout while waiting for GitHub Status API response. "
                    f"Attempt {attempt}/{MAX_RETRIES}. Error: {exc}"
                )
 
            except httpx.ConnectError as exc:
                last_error_detail = (
                    f"Connection error while calling GitHub Status API. "
                    f"Attempt {attempt}/{MAX_RETRIES}. Error: {exc}"
                )
 
            except httpx.TooManyRedirects as exc:
                raise HTTPException(
                    status_code=502,
                    detail=f"Too many redirects while calling GitHub Status API: {exc}",
                ) from exc
 
            except httpx.HTTPStatusError as exc:
                status_code = exc.response.status_code
 
                if 500 <= status_code < 600:
                    last_error_detail = (
                        f"GitHub Status API returned server error {status_code}. "
                        f"Attempt {attempt}/{MAX_RETRIES}. Error: {exc}"
                    )
                else:
                    raise HTTPException(
                        detail=(
                            f"GitHub Status API returned HTTP error "
                            f"{status_code}: {exc}"
                        ),
                    ) from exc
 
            except ValueError as exc:
                raise HTTPException(
                    status_code=502,
                    detail=(
                        f"GitHub Status API returned an invalid JSON response: {exc}"
                    ),
                ) from exc
 
            except httpx.RequestError as exc:
                last_error_detail = (
                    f"Unexpected request error while calling GitHub Status API. "
                    f"Attempt {attempt}/{MAX_RETRIES}. Error: {exc}"
                )
 
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_DELAY_SECONDS)
 
    assert last_error_detail is not None
 
    raise HTTPException(
        status_code=503,
        detail=(
            f"Could not get GitHub status after {MAX_RETRIES} attempts. "
            f"Last error: {last_error_detail}"
        ),
    )
