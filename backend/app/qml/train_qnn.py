import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

from qiskit_machine_learning.algorithms import (
    NeuralNetworkClassifier,
)

from qiskit_algorithms.optimizers import COBYLA

from app.qml.qnn_model import build_qnn


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

from app.core.config import settings

X = pd.read_csv(
    settings.MODEL_DIR / "X_quantum.csv"
)

y = pd.read_csv(
    settings.MODEL_DIR / "y_quantum.csv"
).squeeze()


# --------------------------------------------------
# Train/Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42,

    stratify=y

)


# --------------------------------------------------
# Convert to NumPy (recommended for Qiskit)
# --------------------------------------------------

X_train = X_train.to_numpy(dtype=float)
X_test = X_test.to_numpy(dtype=float)

y_train = y_train.to_numpy(dtype=int)
y_test = y_test.to_numpy(dtype=int)


# --------------------------------------------------
# Build QNN
# --------------------------------------------------

qnn = build_qnn()

classifier = NeuralNetworkClassifier(

    neural_network=qnn,

    optimizer=COBYLA(
        maxiter=100
    )

)


print()
print("=" * 60)
print("Training Quantum Neural Network")
print("=" * 60)


# --------------------------------------------------
# Train
# --------------------------------------------------

classifier.fit(

    X_train,

    y_train

)


# --------------------------------------------------
# Predict
# --------------------------------------------------

pred = classifier.predict(
    X_test
)

pred = np.asarray(
    pred
).ravel()

#
# EstimatorQNN returns {-1, +1}
# Convert to {0, 1}
#

pred = np.where(
    pred == -1,
    0,
    1
)
# --------------------------------------------------
# Debug Output
# --------------------------------------------------

print()

print("Unique y_test:")
print(np.unique(y_test))

print()

print("Unique predictions:")
print(np.unique(pred))

print()


# --------------------------------------------------
# Metrics
# --------------------------------------------------

print(
    "Accuracy :",
    accuracy_score(
        y_test,
        pred
    )
)

print(
    "Precision:",
    precision_score(
        y_test,
        pred,
        average="weighted",
        zero_division=0
    )
)

print(
    "Recall   :",
    recall_score(
        y_test,
        pred,
        average="weighted",
        zero_division=0
    )
)

print(
    "F1       :",
    f1_score(
        y_test,
        pred,
        average="weighted",
        zero_division=0
    )
)


# --------------------------------------------------
# Save Model
# --------------------------------------------------

joblib.dump(
    classifier,
    settings.QNN_MODEL
)

print()

print("QNN model saved.")