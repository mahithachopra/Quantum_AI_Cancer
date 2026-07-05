from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.recommendation.recommendation_service import RecommendationService

router = APIRouter(
    prefix="/recommend",
    tags=["Recommendation"]
)

service = RecommendationService()


class RecommendationRequest(BaseModel):
    mutations: List[str]
    top_k: int = 10


@router.post("/")
def recommend(request: RecommendationRequest):

    results = service.recommend(
        genes=request.mutations,
        top_k=request.top_k
    )

    return {
        "input_mutations": request.mutations,
        "recommendations": results
    }