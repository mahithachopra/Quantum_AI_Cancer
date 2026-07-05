from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.pipeline import router as pipeline_router
from app.api.system import router as system_router
from app.middleware.request_id import RequestIDMiddleware
from app.middleware.logging import LoggingMiddleware

app = FastAPI(
    title=settings.API_NAME,
    version=settings.API_VERSION,
    description="Production API for Quantum-Assisted AI Cancer Therapeutic Recommendation Platform",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
)

app.add_middleware(RequestIDMiddleware)
app.add_middleware(LoggingMiddleware)

app.include_router(
    pipeline_router,
    prefix="/api",
    tags=["Prediction"],
)

app.include_router(
    system_router,
    prefix="/api",
)
