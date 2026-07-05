from app.recommendation.recommendation_service import RecommendationService


class RecommendationTool:

    def __init__(self):
        self.service = RecommendationService()

    def recommend(
        self,
        genes,
        top_k=10
    ):

        return self.service.recommend(
            genes=genes,
            top_k=top_k
        )