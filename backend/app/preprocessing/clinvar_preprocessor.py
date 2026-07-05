from pathlib import Path
import gzip
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[3]

RAW_FILE = PROJECT_ROOT / "datasets" / "raw" / "clinvar" / "variant_summary.txt.gz"

OUTPUT_DIR = PROJECT_ROOT / "datasets" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Read ClinVar
# -----------------------------

print("Loading ClinVar...")

with gzip.open(RAW_FILE, "rt", encoding="utf-8") as f:
    df = pd.read_csv(
        f,
        sep="\t",
        low_memory=False
    )

print("Rows :", len(df))
print("Columns :", len(df.columns))

# -----------------------------
# Keep required columns
# -----------------------------

required_columns = [

    "VariationID",
    "GeneSymbol",
    "Type",
    "ClinicalSignificance",
    "Chromosome",
    "Start",
    "ReferenceAllele",
    "AlternateAllele",
    "ReviewStatus",
    "PhenotypeList"

]

df = df[required_columns]

# -----------------------------
# Cleaning
# -----------------------------

df = df.drop_duplicates()

df = df.dropna(subset=["GeneSymbol"])

df = df[df["GeneSymbol"] != "-"]

df["ClinicalSignificance"] = (
    df["ClinicalSignificance"]
    .fillna("Unknown")
)

df["PhenotypeList"] = (
    df["PhenotypeList"]
    .fillna("Unknown")
)

# -----------------------------
# Save cleaned dataset
# -----------------------------

df.to_csv(
    OUTPUT_DIR / "clinvar_clean.csv",
    index=False
)

print("Saved clinvar_clean.csv")

# -----------------------------
# Gene Table
# -----------------------------

genes = (

    df[["GeneSymbol"]]

    .drop_duplicates()

    .rename(
        columns={
            "GeneSymbol": "gene_symbol"
        }
    )

)

genes = (
    df[["GeneSymbol"]]
    .drop_duplicates()
    .rename(columns={"GeneSymbol": "gene_symbol"})
)

genes.to_csv(
    OUTPUT_DIR / "genes.csv",
    index=False
)

print("Saved genes.csv")

# -----------------------------
# Mutation Table
# -----------------------------

mutations = df.copy()

mutations = mutations.rename(

    columns={

        "VariationID": "mutation_id",

        "GeneSymbol": "gene_symbol",

        "Type": "mutation_type",

        "ClinicalSignificance": "clinical_significance",

        "Chromosome": "chromosome",

        "Start": "position",

        "ReferenceAllele": "reference",

        "AlternateAllele": "alternate",

        "ReviewStatus": "review_status",

        "PhenotypeList": "phenotype"

    }

)

mutations.to_csv(
    OUTPUT_DIR / "mutations.csv",
    index=False
)

print("Saved mutations.csv")

# -----------------------------
# Clinical Significance Table
# -----------------------------

clinical = (

    df[["ClinicalSignificance"]]

    .drop_duplicates()

    .rename(
        columns={
            "ClinicalSignificance":
            "clinical_significance"
        }
    )

)

clinical.insert(
    0,
    "id",
    range(1, len(clinical) + 1)
)

clinical.to_csv(
    OUTPUT_DIR /
    "clinical_significance.csv",
    index=False
)

print("Saved clinical_significance.csv")

print("\nCompleted Successfully")

print("\nDataset Summary")

print("Genes :", len(genes))
print("Mutations :", len(mutations))
print("Clinical Labels :", len(clinical))
print("Project Root :", PROJECT_ROOT)
print("RAW FILE :", RAW_FILE)
print("Exists :", RAW_FILE.exists())