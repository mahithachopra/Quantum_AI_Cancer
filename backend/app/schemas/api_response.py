from typing import Any

from pydantic import BaseModel


class APIResponse(BaseModel):

    success: bool

    request_id: str

    api_version: str

    processing_time_ms: float

    data: Any