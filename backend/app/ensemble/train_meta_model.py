import joblib
import numpy as np

from sklearn.linear_model import LogisticRegression

from app.ensemble.data_loader import EnsembleDataLoader


loader = EnsembleDataLoader()

X_train, X_test, y_train, y_test = loader.load()

meta = LogisticRegression(
    random_state=42,
    max_iter=1000
)

meta.fit(
    X_train,
    y_train
)

joblib.dump(
    meta,
    "app/ensemble/meta_model.pkl"
)

print("Meta model saved.")