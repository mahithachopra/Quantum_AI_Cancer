from pathlib import Path
import pandas as pd

# --------------------------------------------------
# Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[3]

RAW = PROJECT_ROOT / "datasets" / "raw" / "dgibd"
OUT = PROJECT_ROOT / "datasets" / "processed"

OUT.mkdir(exist_ok=True)

# --------------------------------------------------
# Load DGIdb
# --------------------------------------------------

print("Loading DGIdb...")

df = pd.read_csv(
    RAW / "interactions.tsv",
    sep="\t",
    low_memory=False
)

print("Rows :", len(df))

# --------------------------------------------------
# Keep Required Columns
# --------------------------------------------------

gene_drug = df[
    [
        "gene_name",
        "drug_name",
        "interaction_type",
        "interaction_score",
        "approved",
        "immunotherapy",
        "anti_neoplastic",
    ]
].copy()

gene_drug.columns = [
    "gene_symbol",
    "drug_name",
    "interaction_type",
    "interaction_score",
    "approved",
    "immunotherapy",
    "anti_neoplastic",
]

gene_drug.drop_duplicates(inplace=True)

gene_drug.to_csv(
    OUT / "gene_drug.csv",
    index=False
)

# --------------------------------------------------
# Drug Table
# --------------------------------------------------

drugs = df[
    [
        "drug_concept_id",
        "drug_name",
        "approved",
        "immunotherapy",
        "anti_neoplastic",
    ]
].drop_duplicates()

drugs.columns = [
    "drug_id",
    "drug_name",
    "approved",
    "immunotherapy",
    "anti_neoplastic",
]

drugs.to_csv(
    OUT / "dgidb_drugs.csv",
    index=False
)

# --------------------------------------------------
# Gene Table
# --------------------------------------------------

genes = df[
    [
        "gene_concept_id",
        "gene_name",
    ]
].drop_duplicates()

genes.columns = [
    "gene_id",
    "gene_symbol",
]

genes.to_csv(
    OUT / "dgidb_genes.csv",
    index=False
)

# --------------------------------------------------
# Summary
# --------------------------------------------------

print("\n========== SUMMARY ==========")
print("Gene-Drug Interactions :", len(gene_drug))
print("Unique Drugs           :", len(drugs))
print("Unique Genes           :", len(genes))
print("=============================")