from app.ai_platform.feature_engineering import FeatureEngineering
from app.ai_platform.prediction_service import PredictionService


class InferenceEngine:

    def __init__(self):

        self.features = FeatureEngineering()

        self.predictor = PredictionService()

    def infer(self, context):

        features = self.features.build(
            context
        )

        recommendations = self.predictor.score_recommendations(
            features,
            context.recommendations
        )

        return recommendations