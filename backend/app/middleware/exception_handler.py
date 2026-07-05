import traceback

from fastapi import Request
from fastapi.responses import JSONResponse

from app.logging import logger


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):
    traceback.print_exc()

    logger.exception(
        f"Unhandled exception on {request.method} {request.url.path}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal Server Error",
        },
    )