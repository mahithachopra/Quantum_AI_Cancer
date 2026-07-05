from pathlib import Path
import pandas as pd

# --------------------------------------------------
# Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[3]

RAW_FILE = PROJECT_ROOT / "datasets" / "raw" / "ncbi" / "Homo_sapiens.gene_info"

PROCESSED = PROJECT_ROOT / "datasets" / "processed"

GENES_FILE = PROCESSED / "genes.csv"

print("Loading NCBI Gene Info...")

# --------------------------------------------------
# Read file
# --------------------------------------------------

df = pd.read_csv(
    RAW_FILE,
    sep="\t",
    low_memory=False
)

print("Rows:", len(df))
print("Columns:", df.columns.tolist())

# --------------------------------------------------
# Keep required columns
# --------------------------------------------------

df = df[
    [
        "#tax_id",
        "GeneID",
        "Symbol",
        "Synonyms",
        "description",
        "type_of_gene",
        "chromosome"
    ]
]

# Keep only Human
df = df[df["#tax_id"] == 9606]

# Rename columns
df = df.rename(
    columns={
        "#tax_id": "tax_id",
        "GeneID": "gene_id",
        "Symbol": "gene_symbol",
        "Synonyms": "synonyms",
        "description": "description",
        "type_of_gene": "gene_type",
        "chromosome": "chromosome",
    }
)

# Remove duplicates
df = df.drop_duplicates(subset="gene_symbol")

print("Unique NCBI Genes:", len(df))

# --------------------------------------------------
# Load ClinVar genes
# --------------------------------------------------

clinvar = pd.read_csv(GENES_FILE)

# Remove the artificial gene_id from ClinVar
if "gene_id" in clinvar.columns:
    clinvar = clinvar.drop(columns=["gene_id"])

merged = clinvar.merge(
    df,
    on="gene_symbol",
    how="left"
)

print("Matched:", merged["gene_id"].notna().sum())
print("Unmatched:", merged["gene_id"].isna().sum())

# --------------------------------------------------
# Save
# --------------------------------------------------

merged.to_csv(
    PROCESSED / "genes_master.csv",
    index=False
)

print("\nSaved genes_master.csv")
print(merged.head())