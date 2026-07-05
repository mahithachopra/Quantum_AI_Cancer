from pathlib import Path
import joblib


class ModelLoader:

    def __init__(self):

        self.models = {}

        self.base = Path(__file__).resolve().parent.parent

    def load(self, key, relative):

        if key in self.models:
            return self.models[key]

        model = joblib.load(
            self.base / relative
        )

        self.models[key] = model

        print(f"{key} loaded.")

        return model

    def random_forest(self):

        return self.load(
            "rf",
            "ml/models/random_forest.pkl"
        )

    def xgboost(self):

        return self.load(
            "xgb",
            "ml/models/xgboost.pkl"
        )

    def logistic(self):

        return self.load(
            "logistic",
            "ml/models/logistic.pkl"
        )