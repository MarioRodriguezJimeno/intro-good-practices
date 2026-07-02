from typing import Any
import asyncio
import json
import logging
import random
import time
 
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
 
logger = logging.getLogger(__name__)
 
app = FastAPI()
 
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="GITHUB_STATUS_")
 
    url: str = "https://www.githubstatus.com/api/v2/status.json"
    max_retries: int = Field(default=5, ge=1)
    retry_delay_seconds: float = Field(default=0.1, ge=0)
    retry_jitter_seconds: float = Field(default=0.05, ge=0)
    timeout_seconds: float = Field(default=5.0, gt=0)
    overall_timeout_seconds: float = Field(default=26.0, gt=0)
    slow_response_seconds: float = Field(default=1.0, gt=0)
 
 
settings = Settings()
 
 
def get_retry_delay(attempt: int) -> float:
    return settings.retry_delay_seconds * (2 ** (attempt - 1)) + random.uniform(
        0,
        settings.retry_jitter_seconds,
    )
 
 
@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
 
 
@app.get("/v1/github/status")
async def get_github_status() -> dict[str, Any]:
    try:
        async with asyncio.timeout(settings.overall_timeout_seconds):
            return await fetch_github_status()
 
    except TimeoutError as exc:
        raise HTTPException(
            status_code=504,
            detail=(
                "GitHub Status request exceeded the overall timeout "
                f"of {settings.overall_timeout_seconds} seconds."
            ),
        ) from exc
 
 
async def fetch_github_status() -> dict[str, Any]:
    last_error_detail: str | None = None
 
    async with httpx.AsyncClient(timeout=settings.timeout_seconds) as client:
        for attempt in range(1, settings.max_retries + 1):
            try:
                start_time = time.perf_counter()
 
                response = await client.get(settings.url)
                response.raise_for_status()
 
                elapsed_time = time.perf_counter() - start_time
 
                if elapsed_time > settings.slow_response_seconds:
                    logger.warning(
                        "GitHub Status API slow response: %.3f seconds",
                        elapsed_time,
                    )
 
                return response.json()
 
            except httpx.ConnectTimeout as exc:
                last_error_detail = (
                    "Connection timeout while connecting to GitHub Status API. "
                    f"Attempt {attempt}/{settings.max_retries}. Error: {exc}"
                )
 
            except httpx.ReadTimeout as exc:
                last_error_detail = (
                    "Read timeout while waiting for GitHub Status API response. "
                    f"Attempt {attempt}/{settings.max_retries}. Error: {exc}"
                )
 
            except httpx.WriteTimeout as exc:
                last_error_detail = (
                    "Write timeout while sending request to GitHub Status API. "
                    f"Attempt {attempt}/{settings.max_retries}. Error: {exc}"
                )
 
            except httpx.PoolTimeout as exc:
                last_error_detail = (
                    "Pool timeout while waiting for an available HTTP connection. "
                    f"Attempt {attempt}/{settings.max_retries}. Error: {exc}"
                )
 
            except httpx.ConnectError as exc:
                last_error_detail = (
                    "Connection error while calling GitHub Status API. "
                    f"Attempt {attempt}/{settings.max_retries}. Error: {exc}"
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
                        f"Attempt {attempt}/{settings.max_retries}. Error: {exc}"
                    )
                else:
                    raise HTTPException(
                        status_code=status_code,
                        detail=(
                            "GitHub Status API returned HTTP error "
                            f"{status_code}: {exc}"
                        ),
                    ) from exc
 
            except json.JSONDecodeError as exc:
                raise HTTPException(
                    status_code=502,
                    detail=(
                        "GitHub Status API returned an invalid JSON response: "
                        f"{exc}"
                    ),
                ) from exc
 
            except httpx.DecodingError as exc:
                raise HTTPException(
                    status_code=502,
                    detail=(
                        "GitHub Status API response could not be decoded: "
                        f"{exc}"
                    ),
                ) from exc
 
            except httpx.RequestError as exc:
                last_error_detail = (
                    "Request error while calling GitHub Status API. "
                    f"Attempt {attempt}/{settings.max_retries}. Error: {exc}"
                )
 
            logger.warning(
                "Retry %d/%d: %s",
                attempt,
                settings.max_retries,
                last_error_detail,
            )
 
            if attempt < settings.max_retries:
                await asyncio.sleep(get_retry_delay(attempt))
 
    assert last_error_detail is not None
 
    raise HTTPException(
        status_code=503,
        detail=(
            f"Could not get GitHub status after {settings.max_retries} attempts. "
            f"Last error: {last_error_detail}"
        ),
    )