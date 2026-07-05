import pandas as pd
import joblib


from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)

from app.qml.qsvc_model import build_qsvc


from app.core.config import settings

X = pd.read_csv(
    settings.MODEL_DIR / "X_quantum.csv"
)

y = pd.read_csv(
    settings.MODEL_DIR / "y_quantum.csv"
).squeeze()


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print("Training QSVC...")

model = build_qsvc()

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nMetrics\n")

print("Accuracy :", accuracy_score(y_test, pred))
print("Precision:", precision_score(y_test, pred))
print("Recall   :", recall_score(y_test, pred))
print("F1       :", f1_score(y_test, pred))

# QSVC doesn't expose calibrated probabilities by default,
# so compute ROC-AUC from the decision function.
scores = model.decision_function(X_test)
print("ROC-AUC  :", roc_auc_score(y_test, scores))
joblib.dump(
    model,
    settings.QSVC_MODEL
)

print()

print("QSVC model saved.")