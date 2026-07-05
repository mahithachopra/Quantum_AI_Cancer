from app.evidence_fusion.fusion_engine import FusionEngine
from app.evidence_fusion.recommendation_ranker import RecommendationRanker


class EvidenceFusionTool:

    def __init__(self):

        self.engine=FusionEngine()

        self.ranker=RecommendationRanker()

    def fuse(self,context):

        fused=self.engine.fuse(context)

        return self.ranker.rank(fused)