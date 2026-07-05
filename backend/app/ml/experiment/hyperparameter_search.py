import json
from pathlib import Path

import joblib
import pandas as pd

from sklearn.model_selection import RandomizedSearchCV

from app.ml.config import OUTPUT_DIR


class HyperparameterSearch:

    def __init__(self):

        self.X = pd.read_csv(
            OUTPUT_DIR / "X_train.csv"
        )

        self.y = pd.read_csv(
            OUTPUT_DIR / "y_train.csv"
        ).squeeze()

    def optimize(
        self,
        model,
        params,
        model_name,
        n_iter=20
    ):

        search = RandomizedSearchCV(

            estimator=model,

            param_distributions=params,

            scoring="roc_auc",

            cv=5,

            random_state=42,

            n_jobs=-1,

            verbose=2,

            n_iter=n_iter,

        )

        search.fit(
            self.X,
            self.y
        )

        print()

        print("="*60)
        print(model_name)
        print("="*60)

        print("Best Score")
        print(search.best_score_)

        print()

        print("Best Parameters")

        print(search.best_params_)

        model_dir = OUTPUT_DIR.parent / "models"
        metric_dir = OUTPUT_DIR.parent / "metrics"

        model_dir.mkdir(exist_ok=True)
        metric_dir.mkdir(exist_ok=True)

        joblib.dump(

            search.best_estimator_,

            model_dir / f"{model_name}_best.pkl"

        )

        with open(

            metric_dir / f"{model_name}_best.json",

            "w"

        ) as f:

            json.dump(

                {

                    "score": float(search.best_score_),

                    "params": search.best_params_

                },

                f,

                indent=4

            )

        return search.best_estimator_