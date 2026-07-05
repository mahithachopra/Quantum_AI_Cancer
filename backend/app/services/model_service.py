from pathlib import Path

from app.core.config import settings


class ModelService:

    def status(self):

        return {

            "classical": {

                "random_forest": settings.RF_MODEL.exists(),

                "xgboost": settings.XGB_MODEL.exists(),

                "logistic": settings.LR_MODEL.exists(),

            },

            "quantum": {

                "qsvc": settings.QSVC_MODEL.exists(),

                "qnn": settings.QNN_MODEL.exists(),

                "scaler": settings.SCALER_MODEL.exists(),

                "pca": settings.PCA_MODEL.exists(),

            }

        }