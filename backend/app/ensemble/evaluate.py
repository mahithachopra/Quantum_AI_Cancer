from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    f1_score
)

from app.ensemble.data_loader import EnsembleDataLoader

import joblib


loader = EnsembleDataLoader()

X_train, X_test, y_train, y_test = loader.load()

model = joblib.load(
    "app/ensemble/meta_model.pkl"
)

pred = model.predict(X_test)

prob = model.predict_proba(X_test)[:, 1]

print()

print("=" * 60)

print("Hybrid Ensemble")

print("=" * 60)

print("Accuracy :", accuracy_score(y_test, pred))

print("F1 :", f1_score(y_test, pred))

print("ROC AUC :", roc_auc_score(y_test, prob))