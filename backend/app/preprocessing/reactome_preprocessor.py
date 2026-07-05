from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[3]

RAW = PROJECT_ROOT / "datasets" / "raw" / "reactome"
OUT = PROJECT_ROOT / "datasets" / "processed"

OUT.mkdir(exist_ok=True)

# -----------------------------
# Gene -> Pathway Mapping
# -----------------------------

mapping = pd.read_csv(
    RAW / "NCBI2Reactome_All_Levels.txt",
    sep="\t",
    header=None,
    low_memory=False
)

mapping.columns = [
    "GeneID",
    "ReactomeID",
    "URL",
    "Pathway",
    "Evidence",
    "Species"
]

mapping = mapping[
    mapping["Species"] == "Homo sapiens"
]

mapping.to_csv(
    OUT / "gene_pathway.csv",
    index=False
)

print("Gene-Pathway:", mapping.shape)

# -----------------------------
# Pathways
# -----------------------------

pathways = pd.read_csv(
    RAW / "ReactomePathways.txt",
    sep="\t",
    header=None
)

pathways.columns = [
    "ReactomeID",
    "Pathway",
    "Species"
]

pathways = pathways[
    pathways["Species"] == "Homo sapiens"
]

pathways.to_csv(
    OUT / "pathways.csv",
    index=False
)

print("Pathways:", pathways.shape)

# -----------------------------
# Pathway Hierarchy
# -----------------------------

relations = pd.read_csv(
    RAW / "ReactomePathwaysRelation.txt",
    sep="\t",
    header=None
)

relations.columns = [
    "Parent",
    "Child"
]

relations.to_csv(
    OUT / "pathway_relations.csv",
    index=False
)

print("Relations:", relations.shape)

print("\nReactome preprocessing completed.")