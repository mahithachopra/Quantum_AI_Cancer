from app.agents.base_agent import BaseAgent
from app.recommendation.recommendation_service import RecommendationService
from app.tools.ai_platform_tool import AIPlatformTool
from app.memory.memory_keys import MemoryKeys


class DrugAgent(BaseAgent):

    name = "Drug Agent"

    description = "AI Drug Recommendation"

    def __init__(self):

        self.service = RecommendationService()

        self.ai = AIPlatformTool()

    def run(self, context):

        # -------------------------------------------------
        # Step 1: Retrieve candidate drug recommendations
        # -------------------------------------------------

        context.recommendations = self.service.recommend(
            genes=context.genes,
            top_k=10
        )

        # -------------------------------------------------
        # Step 2: AI Platform performs:
        #   • Feature Engineering
        #   • ML/QML Prediction
        #   • Ranking
        #   • Confidence Estimation
        #   • Embedding Generation
        # -------------------------------------------------

        self.ai.predict(context)
        context.memory.memory.save(

    MemoryKeys.RECOMMENDATIONS,

    context.recommendations

)

        return context