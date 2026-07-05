import pandas as pd

from pathlib import Path
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

from app.ml.config import OUTPUT_DIR


class DataPreprocessor:

    def __init__(self):

        self.dataset = pd.read_csv(
            OUTPUT_DIR / "training_dataset.csv"
        )

    def preprocess(self):

        df = self.dataset.copy()

        # Remove duplicates
        df.drop_duplicates(inplace=True)

        # Fill missing values
        imputer = SimpleImputer(strategy="median")

        numeric_cols = df.select_dtypes(
            include=["number"]
        ).columns

        df[numeric_cols] = imputer.fit_transform(
            df[numeric_cols]
        )

        # Scale numeric features
        scaler = StandardScaler()

        feature_cols = [
            c for c in df.columns
            if c != "gene_symbol"
        ]

        df[feature_cols] = scaler.fit_transform(
            df[feature_cols]
        )

        output = OUTPUT_DIR / "training_dataset_scaled.csv"

        df.to_csv(
            output,
            index=False
        )

        print(df.head())

        print(f"\nSaved to {output}")

        return df