from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA = PROJECT_ROOT / "datasets" / "processed"

print("=" * 60)
print("Normalizing Final CSV Files")
print("=" * 60)

# -------------------------------------------------
# Genes
# -------------------------------------------------

genes = pd.read_csv(DATA / "genes_final.csv", low_memory=False)

for col in ["tax_id", "gene_id", "dgidb_gene_id"]:
    if col in genes.columns:
        genes[col] = pd.to_numeric(
            genes[col],
            errors="coerce"
        ).fillna(0).astype("int64")

genes.to_csv(DATA / "genes_final.csv", index=False)

print("✓ genes_final.csv")

# -------------------------------------------------
# Mutations
# -------------------------------------------------

mut = pd.read_csv(DATA / "mutations_final.csv", low_memory=False)

mut["mutation_id"] = pd.to_numeric(
    mut["mutation_id"],
    errors="coerce"
).fillna(0).astype("int64")

mut["position"] = pd.to_numeric(
    mut["position"],
    errors="coerce"
).fillna(0).astype("int64")

mut["chromosome"] = mut["chromosome"].astype(str)

mut.to_csv(DATA / "mutations_final.csv", index=False)

print("✓ mutations_final.csv")

# -------------------------------------------------
# Drug Response
# -------------------------------------------------

drug = pd.read_csv(DATA / "drug_response_final.csv", low_memory=False)

for c in [
    "cosmic_id",
    "drug_id"
]:
    drug[c] = pd.to_numeric(
        drug[c],
        errors="coerce"
    ).fillna(0).astype("int64")

for c in [
    "ln_ic50",
    "auc",
    "z_score"
]:
    drug[c] = pd.to_numeric(
        drug[c],
        errors="coerce"
    ).fillna(0)

drug.to_csv(DATA / "drug_response_final.csv", index=False)

print("✓ drug_response_final.csv")

# -------------------------------------------------
# Drugs
# -------------------------------------------------

drugs = pd.read_csv(DATA / "drugs_final.csv", low_memory=False)

for c in [
    "drug_id",
    "dgidb_drug_id"
]:
    if c in drugs.columns:
        drugs[c] = pd.to_numeric(
            drugs[c],
            errors="coerce"
        ).fillna(0).astype("int64")

for c in [
    "approved",
    "immunotherapy",
    "anti_neoplastic"
]:
    if c in drugs.columns:
        drugs[c] = (
            drugs[c]
            .fillna(False)
            .astype(bool)
        )

drugs.to_csv(DATA / "drugs_final.csv", index=False)

print("✓ drugs_final.csv")

print("\nNormalization Completed Successfully.")