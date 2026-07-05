import joblib
import numpy as np


class HybridPredictor:

    def __init__(self):

        self.meta = joblib.load(
            "app/ensemble/meta_model.pkl"
        )

    def predict(self, features):

        probability = self.meta.predict_proba(
            features
        )[0, 1]

        prediction = int(probability >= 0.5)

        return {

            "prediction": prediction,

            "probability": float(probability)

        }


if __name__ == "__main__":

    predictor = HybridPredictor()

    sample = np.random.rand(1, 10)

    print(
        predictor.predict(sample)
    )