from pathlib import Path

import pandas as pd

from app.ml.config import OUTPUT_DIR


class TargetBuilder:

    def __init__(self):

        self.df = pd.read_csv(
            OUTPUT_DIR / "gene_drug_training_dataset.csv"
        )

    def build(self):

        df = self.df.copy()

        print("Original rows:", len(df))

        # Keep only drugs with experimental response
        df = df[df["response_count"] > 0].copy()

        print("Rows with GDSC:", len(df))

        # Lower ln(IC50) = better sensitivity
        threshold = df["avg_ln_ic50"].median()

        print(f"Median ln(IC50): {threshold:.4f}")

        df["target"] = (
            df["avg_ln_ic50"] <= threshold
        ).astype(int)

        # Remove response columns to avoid data leakage
        df.drop(
            columns=[
                "avg_ln_ic50",
                "avg_auc",
                "avg_z_score",
                "response_count",
            ],
            inplace=True,
        )

        output = OUTPUT_DIR / "ml_training_dataset.csv"

        df.to_csv(
            output,
            index=False,
        )

        print()

        print(df["target"].value_counts())

        print()

        print(df.head())

        print()

        print(f"Saved to {output}")


if __name__ == "__main__":
    TargetBuilder().build()