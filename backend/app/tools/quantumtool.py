import joblib

from app.core.config import settings


class QuantumTool:

    def __init__(self):

        self.qsvc = joblib.load(
            settings.QSVC_MODEL
        )

    def classify(self, X):

        prediction = self.qsvc.predict(X)

        score = self.qsvc.decision_function(X)

        return {

            "prediction": prediction.tolist(),

            "score": score.tolist()

        }