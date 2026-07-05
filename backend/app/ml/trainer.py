from pathlib import Path

import joblib
import json
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)

from app.ml.config import OUTPUT_DIR


MODEL_DIR = OUTPUT_DIR.parent / "models"
METRIC_DIR = OUTPUT_DIR.parent / "metrics"

MODEL_DIR.mkdir(exist_ok=True)
METRIC_DIR.mkdir(exist_ok=True)


class Trainer:

    def __init__(self, model, name):

        self.model = model
        self.name = name

        self.X_train = pd.read_csv(
            OUTPUT_DIR / "X_train.csv"
        )

        self.X_test = pd.read_csv(
            OUTPUT_DIR / "X_test.csv"
        )

        self.y_train = pd.read_csv(
            OUTPUT_DIR / "y_train.csv"
        ).squeeze()

        self.y_test = pd.read_csv(
            OUTPUT_DIR / "y_test.csv"
        ).squeeze()

    def train(self):

        print(f"\nTraining {self.name}")

        self.model.fit(
            self.X_train,
            self.y_train,
        )

        prediction = self.model.predict(
            self.X_test
        )

        probability = self.model.predict_proba(
            self.X_test
        )[:, 1]

        metrics = {

            "accuracy":
            accuracy_score(
                self.y_test,
                prediction,
            ),

            "precision":
            precision_score(
                self.y_test,
                prediction,
            ),

            "recall":
            recall_score(
                self.y_test,
                prediction,
            ),

            "f1":
            f1_score(
                self.y_test,
                prediction,
            ),

            "roc_auc":
            roc_auc_score(
                self.y_test,
                probability,
            ),
        }

        for k, v in metrics.items():

            print(f"{k:12} {v:.4f}")

        joblib.dump(
            self.model,
            MODEL_DIR / f"{self.name}.pkl",
        )

        with open(
            METRIC_DIR / f"{self.name}.json",
            "w",
        ) as f:

            json.dump(
                metrics,
                f,
                indent=4,
            )

        return metrics