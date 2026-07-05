import re
import pandas as pd
from sqlalchemy import text

from app.core.postgres import SessionLocal


class DrugNormalizer:

    @staticmethod
    def normalize(name):

        if pd.isna(name):
            return ""

        name = str(name).upper()

        # Remove common prefixes
        name = re.sub(r"CHEMBL:", "", name)

        # Remove punctuation
        name = re.sub(r"[^A-Z0-9 ]", "", name)

        # Remove extra spaces
        name = re.sub(r"\s+", " ", name)

        return name.strip()


def build_mapping():

    db = SessionLocal()

    print("Loading DGIdb drugs...")

    gene_drug = pd.read_sql(
        text("""
        SELECT DISTINCT drug_name
        FROM gene_drug
        """),
        db.connection()
    )

    print("Loading GDSC drugs...")

    gdsc = pd.read_sql(
        text("""
        SELECT DISTINCT drug_name
        FROM drug_response
        """),
        db.connection()
    )

    gene_drug["normalized"] = gene_drug["drug_name"].apply(
        DrugNormalizer.normalize
    )

    gdsc["normalized"] = gdsc["drug_name"].apply(
        DrugNormalizer.normalize
    )

    merged = gene_drug.merge(
        gdsc,
        on="normalized",
        how="inner",
        suffixes=("_dgidb", "_gdsc")
    )

    print("\nRecovered Matches:", len(merged))

    print("\nFirst 20 Matches\n")

    print(
        merged[
            [
                "drug_name_dgidb",
                "drug_name_gdsc",
                "normalized"
            ]
        ].head(20)
    )

    db.close()


if __name__ == "__main__":
    build_mapping()