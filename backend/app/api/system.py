from fastapi import APIRouter

from app.core.config import settings
import time

from fastapi import Request
from fastapi.encoders import jsonable_encoder

from app.schemas.api_response import APIResponse
from app.services.model_service import ModelService
from app.core.config import settings

router = APIRouter(tags=["System"])
model_service = ModelService()

@router.get("/health")
def health():

    return {

        "status": "healthy"

    }


@router.get("/ready")
def ready():

    return {

        "status": "ready"

    }


@router.get("/version")
def version():

    return {

        "name": settings.API_NAME,

        "version": settings.API_VERSION

    }
@router.get(
    "/models",
    response_model=APIResponse
)
def models(request: Request):

    start = time.perf_counter()

    data = model_service.status()

    elapsed = (
        time.perf_counter() - start
    ) * 1000

    return APIResponse(

        success=True,

        request_id=request.state.request_id,

        api_version=settings.API_VERSION,

        processing_time_ms=round(
            elapsed,
            2
        ),

        data=jsonable_encoder(data)

    )