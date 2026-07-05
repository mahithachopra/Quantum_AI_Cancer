from pathlib import Path
import pandas as pd

# ----------------------------------------------------
# Paths
# ----------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[3]

RAW = PROJECT_ROOT / "datasets" / "raw" / "gdsc"
OUT = PROJECT_ROOT / "datasets" / "processed"

OUT.mkdir(exist_ok=True)

# ----------------------------------------------------
# Load Files
# ----------------------------------------------------

print("Loading GDSC...")

gdsc = pd.read_csv(
    RAW / "GDSC2-dataset.csv",
    low_memory=False
)

compounds = pd.read_csv(
    RAW / "Compounds-annotation.csv",
    low_memory=False
)

cell_lines = pd.read_excel(
    RAW / "Cell_Lines_Details.xlsx"
)

print(f"GDSC Rows: {len(gdsc)}")
print(f"Compounds: {len(compounds)}")
print(f"Cell Lines: {len(cell_lines)}")

# ----------------------------------------------------
# Drug Response
# ----------------------------------------------------

drug_response = gdsc[
    [
        "COSMIC_ID",
        "CELL_LINE_NAME",
        "TCGA_DESC",
        "DRUG_ID",
        "DRUG_NAME",
        "PUTATIVE_TARGET",
        "PATHWAY_NAME",
        "LN_IC50",
        "AUC",
        "Z_SCORE",
    ]
].copy()

drug_response.columns = [
    "cosmic_id",
    "cell_line",
    "cancer_type",
    "drug_id",
    "drug_name",
    "target",
    "pathway",
    "ln_ic50",
    "auc",
    "z_score",
]

drug_response.drop_duplicates(inplace=True)

drug_response.to_csv(
    OUT / "drug_response.csv",
    index=False
)

# ----------------------------------------------------
# Drug Table
# ----------------------------------------------------

drugs = (
    gdsc[
        [
            "DRUG_ID",
            "DRUG_NAME",
            "PUTATIVE_TARGET",
            "PATHWAY_NAME",
        ]
    ]
    .drop_duplicates()
)

drugs.columns = [
    "drug_id",
    "drug_name",
    "target",
    "pathway",
]

drugs.to_csv(
    OUT / "drugs.csv",
    index=False
)

# ----------------------------------------------------
# Cell Lines
# ----------------------------------------------------

cell_lines.to_csv(
    OUT / "cell_lines.csv",
    index=False
)

# ----------------------------------------------------
# Summary
# ----------------------------------------------------

print("\n========== SUMMARY ==========")
print("Drug Response :", len(drug_response))
print("Unique Drugs  :", len(drugs))
print("Cell Lines    :", len(cell_lines))
print("=============================")