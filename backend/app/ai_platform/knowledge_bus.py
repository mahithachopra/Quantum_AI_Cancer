from app.ai_platform.embedding_engine import EmbeddingEngine
from app.ai_platform.prediction_engine import PredictionEngine
from app.ai_platform.ranking_engine import RankingEngine
from app.ai_platform.confidence_engine import ConfidenceEngine


class AIKnowledgeBus:

    def __init__(self):

        self.embedding = EmbeddingEngine()

        self.prediction = PredictionEngine()

        self.ranking = RankingEngine()

        self.confidence = ConfidenceEngine()

    def embed(self, context):

        return self.embedding.embed(context)

    def predict(self, context):

        return self.prediction.predict(context)

    def rank(self, context):

        return self.ranking.rank(context)

    def confidence_score(self, context):

        return self.confidence.compute(context)