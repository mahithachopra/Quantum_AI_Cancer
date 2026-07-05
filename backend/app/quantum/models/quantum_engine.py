from app.quantum.prediction_service import QuantumPredictionService


class QuantumEngine:

    def __init__(self):

        self.service = QuantumPredictionService()

    def predict(

        self,

        features

    ):

        return self.service.predict(

            features

        )