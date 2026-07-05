import joblib

from app.core.config import settings


class MLTool:

    def __init__(self):

        self.rf = joblib.load(
            settings.RF_MODEL
        )

        self.xgb = joblib.load(
            settings.XGB_MODEL
        )

    def predict(self, X):

        rf = self.rf.predict_proba(X)[0, 1]

        xgb = self.xgb.predict_proba(X)[0, 1]

        return {

            "rf": float(rf),

            "xgb": float(xgb),

            "hybrid": float(
                (rf + xgb) / 2
            )

        }