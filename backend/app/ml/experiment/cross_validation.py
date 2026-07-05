import numpy as np
import pandas as pd

from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_validate

from sklearn.metrics import (
    make_scorer,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)

from app.ml.config import OUTPUT_DIR


class CrossValidator:

    def __init__(self):

        self.X = pd.read_csv(
            OUTPUT_DIR / "X_train.csv"
        )

        self.y = pd.read_csv(
            OUTPUT_DIR / "y_train.csv"
        ).squeeze()

        self.cv = StratifiedKFold(
            n_splits=5,
            shuffle=True,
            random_state=42,
        )

    def evaluate(self, model):

        scoring = {

            "accuracy":
            make_scorer(
                accuracy_score
            ),

            "precision":
            make_scorer(
                precision_score
            ),

            "recall":
            make_scorer(
                recall_score
            ),

            "f1":
            make_scorer(
                f1_score
            ),

            "roc_auc":
            "roc_auc",
        }

        scores = cross_validate(

            model,

            self.X,

            self.y,

            scoring=scoring,

            cv=self.cv,

            n_jobs=-1,

        )

        result = {}

        print()

        print("="*60)

        for metric in scoring.keys():

            mean = scores[
                f"test_{metric}"
            ].mean()

            std = scores[
                f"test_{metric}"
            ].std()

            result[metric] = (

                float(mean),

                float(std),

            )

            print(

                f"{metric:10}"

                f"{mean:.4f}"

                f" ± "

                f"{std:.4f}"

            )

        print("="*60)

        return result