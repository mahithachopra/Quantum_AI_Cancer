import joblib
import numpy as np
from app.core.config import settings

from app.ai_platform.model_loader import ModelLoader
from app.ai_platform.models import (
    PredictionResult,
    DrugPrediction,
)
from app.ai_platform.feature_vectorizer import FeatureVectorizer
from app.qml.quantum_model_loader import QuantumModelLoader


class PredictionService:

    def __init__(self):

        self.loader = ModelLoader()

        self.rf = self.loader.random_forest()
        self.xgb = self.loader.xgboost()
        self.lr = self.loader.logistic()

        self.vectorizer = FeatureVectorizer()

        self.quantum = QuantumModelLoader()
        self.qsvc = self.quantum.qsvc()

        self.scaler = joblib.load(
    settings.SCALER_MODEL
)

        self.pca = joblib.load(
            settings.PCA_MODEL
)
        self.qnn = self.quantum.qnn()

    def _predict_quantum_probability(
        self,
        patient_features
    ):

        #
        # Original 13-dimensional feature vector
        #

        vector = self.vectorizer.vectorize(
            patient_features
        )

        #
        # Apply the SAME preprocessing used during QSVC training
        #

        vector = self.scaler.transform(
            vector
        )

        vector = self.pca.transform(
            vector
        )

        #
        # Quantum prediction
        #

        score = float(
            self.qsvc.decision_function(
                vector
            )[0]
        )

        #
        # Convert decision score into probability-like confidence
        #

        probability = 1.0 / (
            1.0 + np.exp(-score)
        )

        return probability

    def _predict_probability(
        self,
        patient_features
    ):

        vector = self.vectorizer.vectorize(
            patient_features
        )

        rf_prob = float(
            self.rf.predict_proba(vector)[0][1]
        )

        xgb_prob = float(
            self.xgb.predict_proba(vector)[0][1]
        )

        lr_prob = float(
            self.lr.predict_proba(vector)[0][1]
        )

        qsvc_prob = self._predict_quantum_probability(
            patient_features
        )

        probability = np.mean(
            [
                rf_prob,
                xgb_prob,
                lr_prob,
                qsvc_prob
            ]
        )

        return (
            probability,
            rf_prob,
            xgb_prob,
            lr_prob,
            qsvc_prob
        )

    def predict(
        self,
        patient_features
    ):

        (
            probability,
            rf_prob,
            xgb_prob,
            lr_prob,
            qsvc_prob
        ) = self._predict_probability(
            patient_features
        )

        predictions = []

        for gene in patient_features.genes:

            predictions.append(

                DrugPrediction(

                    gene=gene,

                    drug="AI_PREDICTION",

                    probability=probability,

                    confidence=probability,

                    metadata={

                        "rf": rf_prob,

                        "xgb": xgb_prob,

                        "lr": lr_prob,

                        "qsvc": qsvc_prob

                    }

                )

            )

        return PredictionResult(
            predictions=predictions
        )
    def _predict_qnn_probability(
        self,
        patient_features
    ):

        vector = self.vectorizer.vectorize(
            patient_features
        )

        vector = self.scaler.transform(
            vector
        )

        vector = self.pca.transform(
            vector
        )

        pred = self.qnn.predict(vector)

        pred = np.asarray(
            pred
        ).ravel()

        pred = np.where(
            pred == -1,
            0,
            1
        )

        return float(pred[0])

    def score_recommendations(
        self,
        patient_features,
        recommendations
    ):

        (
            probability,
            rf_prob,
            xgb_prob,
            lr_prob,
            qsvc_prob
        ) = self._predict_probability(
            patient_features
        )

        for recommendation in recommendations:

            recommendation["rf_probability"] = round(
                rf_prob,
                4
            )

            recommendation["xgb_probability"] = round(
                xgb_prob,
                4
            )

            recommendation["lr_probability"] = round(
                lr_prob,
                4
            )

            recommendation["qsvc_probability"] = round(
                qsvc_prob,
                4
            )

            recommendation["ai_probability"] = round(
                probability,
                4
            )

            interaction = recommendation.get(
                "interaction_score",
                0.0
            )

            final_score = (
                0.7 * probability +
                0.3 * interaction
            )

            recommendation["final_score"] = round(
                final_score,
                4
            )

        recommendations.sort(
            key=lambda x: x["final_score"],
            reverse=True
        )

        return recommendations