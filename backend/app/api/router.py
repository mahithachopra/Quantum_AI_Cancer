from fastapi import APIRouter

from app.api import gene
from app.api import mutation
from app.api.recommendation import router as recommendation_router


api_router = APIRouter(prefix="/api/v1")

api_router.include_router(gene.router)
api_router.include_router(mutation.router)
api_router.include_router(recommendation_router)