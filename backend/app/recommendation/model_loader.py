import joblib

from app.core.config import settings


class ModelLoader:

    def __init__(self):

        self.rf = joblib.load(
            settings.RF_MODEL
        )

        self.xgb = joblib.load(
            settings.XGB_MODEL
        )

    def predict(self, X):

        expected = list(
            self.rf.feature_names_in_
        )

        X = X[expected]

        rf = self.rf.predict_proba(
            X
        )[0, 1]

        xgb = self.xgb.predict_proba(
            X
        )[0, 1]

        return {

            "rf_probability": float(rf),

            "xgb_probability": float(xgb),

            "hybrid_probability": float(
                (rf + xgb) / 2
            )

        }