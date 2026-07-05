import pandas as pd
from sqlalchemy import text

from app.core.postgres import SessionLocal
from app.ml.config import OUTPUT_DIR


class GeneDrugDatasetBuilder:

    def __init__(self):
        self.db = SessionLocal()

    def build(self):

        print("Loading gene features...")

        genes = pd.read_csv(
            OUTPUT_DIR / "training_dataset.csv"
        )

        print("Loading gene-drug interactions...")

        gene_drug = pd.read_sql(
            text("""
            SELECT
                gene_symbol,
                drug_name,
                interaction_score,
                approved,
                immunotherapy,
                anti_neoplastic
            FROM gene_drug
            """),
            self.db.connection(),
        )

        print("Loading drug response...")

        response = pd.read_sql(
    text("""
    SELECT
        drug_name,
        AVG(ln_ic50) AS avg_ln_ic50,
        AVG(auc) AS avg_auc,
        AVG(z_score) AS avg_z_score,
        COUNT(*) AS response_count
    FROM drug_response
    GROUP BY drug_name
    """),
    self.db.connection(),
)

        print("Merging datasets...")

        df = gene_drug.merge(
            genes,
            on="gene_symbol",
            how="left"
        )

        df = df.merge(
            response,
            on="drug_name",
            how="left"
        )

        import numpy as np

        # Fill numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df[numeric_cols] = df[numeric_cols].fillna(0)

        # Fill string/object columns
        string_cols = df.select_dtypes(include=["object", "string"]).columns
        df[string_cols] = df[string_cols].fillna("")

        output = OUTPUT_DIR / "gene_drug_training_dataset.csv"

        df.to_csv(
            output,
            index=False
        )

        print()

        print(df.head())

        print()

        print(df.shape)

        print()

        print(f"Saved to {output}")

        self.db.close()


if __name__ == "__main__":
    GeneDrugDatasetBuilder().build()