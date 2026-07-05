import joblib
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from app.qml.config import OUTPUT_DIR


class QuantumPreprocessor:

    def __init__(self):

        self.scaler = StandardScaler()

        self.pca = PCA(
            n_components=6,
            random_state=42
        )

    def preprocess(self):

        from app.core.config import settings

        df = pd.read_csv(
            settings.BASE_DIR /
            "app/ml/output/ml_training_dataset_graph.csv"
)

        X = df.drop(
            columns=[
                "gene_symbol",
                "drug_name",
                "target"
            ]
        )

        # Convert booleans to integers
        X = X.replace({True: 1, False: 0})

        y = df["target"]

        X = self.scaler.fit_transform(X)

        X = self.pca.fit_transform(X)

        pd.DataFrame(X).to_csv(
            OUTPUT_DIR / "X_quantum.csv",
            index=False
        )

        y.to_csv(
            OUTPUT_DIR / "y_quantum.csv",
            index=False
        )

        joblib.dump(
            self.scaler,
            OUTPUT_DIR / "scaler.pkl"
        )

        joblib.dump(
            self.pca,
            OUTPUT_DIR / "pca.pkl"
        )

        print("Quantum dataset created.")
        print("Shape:", X.shape)
if __name__ == "__main__":
    QuantumPreprocessor().preprocess()