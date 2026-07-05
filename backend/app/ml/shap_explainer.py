import joblib
import shap
import pandas as pd
import matplotlib.pyplot as plt

from app.ml.config import OUTPUT_DIR

MODEL_DIR = OUTPUT_DIR.parent / "models"
PLOT_DIR = OUTPUT_DIR.parent / "plots"

PLOT_DIR.mkdir(exist_ok=True)

print("Loading model...")

model = joblib.load(
    MODEL_DIR / "xgboost.pkl"
)

X_train = pd.read_csv(
    OUTPUT_DIR / "X_train.csv"
)

X_test = pd.read_csv(
    OUTPUT_DIR / "X_test.csv"
)

print("Building SHAP explainer...")

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X_test)

print("Generating Summary Plot...")

plt.figure(figsize=(10,6))
shap.summary_plot(
    shap_values,
    X_test,
    show=False
)

plt.tight_layout()
plt.savefig(
    PLOT_DIR / "shap_summary.png",
    dpi=300
)
plt.close()

print("Generating Bar Plot...")

plt.figure(figsize=(8,6))
shap.summary_plot(
    shap_values,
    X_test,
    plot_type="bar",
    show=False
)

plt.tight_layout()
plt.savefig(
    PLOT_DIR / "shap_bar.png",
    dpi=300
)
plt.close()

print("Done!")