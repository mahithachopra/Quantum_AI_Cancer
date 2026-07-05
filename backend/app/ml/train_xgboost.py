import json
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from xgboost import XGBClassifier

from app.ml.config import OUTPUT_DIR


MODEL_DIR = OUTPUT_DIR.parent / "models"
METRIC_DIR = OUTPUT_DIR.parent / "metrics"
PLOT_DIR = OUTPUT_DIR.parent / "plots"

MODEL_DIR.mkdir(exist_ok=True)
METRIC_DIR.mkdir(exist_ok=True)
PLOT_DIR.mkdir(exist_ok=True)


X_train = pd.read_csv(OUTPUT_DIR / "X_train.csv")
X_test = pd.read_csv(OUTPUT_DIR / "X_test.csv")

y_train = pd.read_csv(OUTPUT_DIR / "y_train.csv").squeeze()
y_test = pd.read_csv(OUTPUT_DIR / "y_test.csv").squeeze()


model = XGBClassifier(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.9,
    colsample_bytree=0.8,
    random_state=42,
    eval_metric="logloss",
)

print("Training XGBoost...")

model.fit(X_train, y_train)

prediction = model.predict(X_test)

probability = model.predict_proba(X_test)[:, 1]


metrics = {

    "accuracy": float(
        accuracy_score(y_test, prediction)
    ),

    "precision": float(
        precision_score(y_test, prediction)
    ),

    "recall": float(
        recall_score(y_test, prediction)
    ),

    "f1": float(
        f1_score(y_test, prediction)
    ),

    "roc_auc": float(
        roc_auc_score(y_test, probability)
    ),
}


print("\nMetrics\n")

for k, v in metrics.items():
    print(f"{k:12} {v:.4f}")

print()

print(classification_report(y_test, prediction))

print()

print(confusion_matrix(y_test, prediction))


joblib.dump(
    model,
    MODEL_DIR / "xgboost.pkl"
)

with open(
    METRIC_DIR / "xgboost_metrics.json",
    "w",
) as f:

    json.dump(
        metrics,
        f,
        indent=4,
    )


importance = pd.Series(
    model.feature_importances_,
    index=X_train.columns,
).sort_values()


plt.figure(figsize=(8, 5))

importance.plot.barh()

plt.tight_layout()

plt.savefig(
    PLOT_DIR / "xgboost_feature_importance.png",
    dpi=300,
)

print()

print("Model Saved")

print("Metrics Saved")

print("Feature Importance Saved")