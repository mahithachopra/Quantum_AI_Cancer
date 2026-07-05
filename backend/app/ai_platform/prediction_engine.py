from app.ai_platform.inference_engine import InferenceEngine


class PredictionEngine:

    def __init__(self):

        self.engine = InferenceEngine()

    def predict(self, context):

        return self.engine.infer(
            context
        )