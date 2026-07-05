from pydantic import BaseModel
from typing import List


class RecommendationResponse(BaseModel):

    gene: str

    drug: str

    confidence: float


class PipelineResponse(BaseModel):

    recommendations: List[RecommendationResponse]