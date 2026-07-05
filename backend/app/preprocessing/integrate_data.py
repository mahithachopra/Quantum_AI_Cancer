from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[3]

PROCESSED = PROJECT_ROOT / "datasets" / "processed"
OUTPUT = PROJECT_ROOT / "datasets" / "processed"

print("=" * 60)
print("Building Master Tables")
print("=" * 60)

# =====================================================
# GENES
# =====================================================

genes_master = pd.read_csv(PROCESSED / "genes_master.csv")

dgidb_genes = pd.read_csv(PROCESSED / "dgidb_genes.csv")

dgidb_genes = dgidb_genes.rename(
    columns={
        "gene_id": "dgidb_gene_id"
    }
)

genes = genes_master.merge(
    dgidb_genes,
    on="gene_symbol",
    how="left"
)

genes.drop_duplicates(
    subset="gene_symbol",
    inplace=True
)

genes.to_csv(
    OUTPUT / "genes_final.csv",
    index=False
)

print(f"Genes : {len(genes)}")
# -----------------------------
# Fix numeric columns
# -----------------------------

genes["tax_id"] = (
    pd.to_numeric(genes["tax_id"], errors="coerce")
    .fillna(0)
    .astype(int)
)

genes["gene_id"] = (
    pd.to_numeric(genes["gene_id"], errors="coerce")
    .fillna(0)
    .astype(int)
)

if "dgidb_gene_id" in genes.columns:
    genes["dgidb_gene_id"] = (
        pd.to_numeric(genes["dgidb_gene_id"], errors="coerce")
        .fillna(0)
        .astype(int)
    )

# =====================================================
# DRUGS
# =====================================================

gdsc = pd.read_csv(PROCESSED / "drugs.csv", low_memory=False)

dgidb = pd.read_csv(PROCESSED / "dgidb_drugs.csv", low_memory=False)

# Rename IDs before merge
gdsc = gdsc.rename(columns={
    "drug_id": "gdsc_drug_id"
})

dgidb = dgidb.rename(columns={
    "drug_id": "dgidb_drug_id"
})

# Merge
drugs = gdsc.merge(
    dgidb,
    on="drug_name",
    how="outer"
)

# Create unified drug_id
drugs["drug_id"] = drugs["gdsc_drug_id"]

drugs["drug_id"] = (
    pd.to_numeric(
        drugs["drug_id"],
        errors="coerce"
    )
    .fillna(0)
    .astype("int64")
)

drugs["dgidb_drug_id"] = (
    pd.to_numeric(
        drugs["dgidb_drug_id"],
        errors="coerce"
    )
    .fillna(0)
    .astype("int64")
)

for col in [
    "approved",
    "immunotherapy",
    "anti_neoplastic"
]:
    drugs[col] = (
        drugs[col]
        .fillna(False)
        .astype(bool)
    )

# Final column order
drugs = drugs[
    [
        "drug_id",
        "drug_name",
        "target",
        "pathway",
        "dgidb_drug_id",
        "approved",
        "immunotherapy",
        "anti_neoplastic",
    ]
]

drugs.drop_duplicates(
    subset="drug_name",
    inplace=True
)

drugs.to_csv(
    OUTPUT / "drugs_final.csv",
    index=False
)

print(f"Drugs : {len(drugs)}")

# =====================================================
# MUTATIONS
# =====================================================

mutations = pd.read_csv(PROCESSED / "mutations.csv")

mutations.to_csv(
    OUTPUT / "mutations_final.csv",
    index=False
)

print(f"Mutations : {len(mutations)}")

# =====================================================
# PATHWAYS
# =====================================================

pathways = pd.read_csv(PROCESSED / "pathways.csv")

pathways.to_csv(
    OUTPUT / "pathways_final.csv",
    index=False
)

print(f"Pathways : {len(pathways)}")

# =====================================================
# GENE PATHWAY
# =====================================================

gp = pd.read_csv(PROCESSED / "gene_pathway.csv")

gp.to_csv(
    OUTPUT / "gene_pathway_final.csv",
    index=False
)

print(f"Gene Pathway : {len(gp)}")

# =====================================================
# GENE DRUG
# =====================================================

gd = pd.read_csv(PROCESSED / "gene_drug.csv")

gd.to_csv(
    OUTPUT / "gene_drug_final.csv",
    index=False
)

print(f"Gene Drug : {len(gd)}")

# =====================================================
# DRUG RESPONSE
# =====================================================

response = pd.read_csv(
    PROCESSED / "drug_response.csv"
)

response.to_csv(
    OUTPUT / "drug_response_final.csv",
    index=False
)

print(f"Drug Response : {len(response)}")

# =====================================================
# CELL LINES
# =====================================================

print("\nProcessing Cell Lines...")

cells = pd.read_csv(
    PROCESSED / "cell_lines.csv",
    low_memory=False
)

# -----------------------------------------------------
# Clean Column Names
# -----------------------------------------------------

cells.columns = (
    cells.columns
    .str.replace("\n", " ", regex=False)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

print("Available Columns:")
print(cells.columns.tolist())

# -----------------------------------------------------
# Select Required Columns
# -----------------------------------------------------

cells = cells[
    [
        "Sample Name",
        "COSMIC identifier",
        "Cancer Type (matching TCGA label)"
    ]
].copy()

# -----------------------------------------------------
# Rename Columns
# -----------------------------------------------------

cells.rename(
    columns={
        "Sample Name": "sample_name",
        "COSMIC identifier": "cosmic_id",
        "Cancer Type (matching TCGA label)": "cancer_type",
    },
    inplace=True,
)

# -----------------------------------------------------
# Data Cleaning
# -----------------------------------------------------

cells["sample_name"] = (
    cells["sample_name"]
    .astype(str)
    .str.strip()
)

cells["cosmic_id"] = (
    pd.to_numeric(
        cells["cosmic_id"],
        errors="coerce"
    )
    .fillna(0)
    .astype("int64")
)

cells["cancer_type"] = (
    cells["cancer_type"]
    .fillna("Unknown")
    .astype(str)
    .str.strip()
)

# -----------------------------------------------------
# Remove Duplicates
# -----------------------------------------------------

cells.drop_duplicates(
    subset=["sample_name", "cosmic_id"],
    inplace=True
)

# -----------------------------------------------------
# Save
# -----------------------------------------------------

cells.to_csv(
    OUTPUT / "cell_lines_final.csv",
    index=False
)

print(f"Cell Lines : {len(cells)}")
print(cells.head())
print("\nMaster tables created successfully.")