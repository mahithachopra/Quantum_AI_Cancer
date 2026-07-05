from xgboost import XGBClassifier

from app.ml.experiment.hyperparameter_search import HyperparameterSearch

search = HyperparameterSearch()

params = {

    "n_estimators": [100, 200, 300, 500],

    "max_depth": [3, 4, 5, 6, 8],

    "learning_rate": [0.01, 0.03, 0.05, 0.1],

    "subsample": [0.7, 0.8, 0.9, 1.0],

    "colsample_bytree": [0.6, 0.8, 1.0],

    "gamma": [0, 0.1, 0.3, 1]
}

search.optimize(

    XGBClassifier(
        random_state=42,
        eval_metric="logloss"
    ),

    params,

    "xgboost"

)