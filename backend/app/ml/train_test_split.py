import pandas as pd
from sklearn.model_selection import train_test_split

from app.ml.config import OUTPUT_DIR


class DatasetSplitter:

    def __init__(self):
        self.df = pd.read_csv(
            "app/ml/output/ml_training_dataset_graph.csv"
        )

    def split(self):

        df = self.df.copy()

        # Keep metadata separately
        metadata = df[
            [
                "gene_symbol",
                "drug_name"
            ]
        ]

        # Remove identifiers
        X = df.drop(
            columns=[
                "gene_symbol",
                "drug_name",
                "target"
            ]
        )

        y = df["target"]

        (
            X_train,
            X_test,
            y_train,
            y_test,
            meta_train,
            meta_test,
        ) = train_test_split(
            X,
            y,
            metadata,
            test_size=0.20,
            stratify=y,
            random_state=42,
        )

        X_train.to_csv(
            OUTPUT_DIR / "X_train.csv",
            index=False
        )

        X_test.to_csv(
            OUTPUT_DIR / "X_test.csv",
            index=False
        )

        y_train.to_csv(
            OUTPUT_DIR / "y_train.csv",
            index=False
        )

        y_test.to_csv(
            OUTPUT_DIR / "y_test.csv",
            index=False
        )

        meta_train.to_csv(
            OUTPUT_DIR / "metadata_train.csv",
            index=False
        )

        meta_test.to_csv(
            OUTPUT_DIR / "metadata_test.csv",
            index=False
        )

        print("=" * 60)
        print("Dataset Split Completed")
        print("=" * 60)

        print()

        print("Training Samples :", len(X_train))
        print("Testing Samples  :", len(X_test))

        print()

        print("Training Class Distribution")

        print(y_train.value_counts())

        print()

        print("Testing Class Distribution")

        print(y_test.value_counts())


if __name__ == "__main__":
    DatasetSplitter().split()