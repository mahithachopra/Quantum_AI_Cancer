from pathlib import Path

import pandas as pd

ML_DIR = Path("app/ml/output")
GRAPH_DIR = Path("app/graph_features/output")

training = pd.read_csv(
    ML_DIR / "ml_training_dataset.csv"
)

graph = pd.read_csv(
    GRAPH_DIR / "gene_graph_features.csv"
)

merged = training.merge(
    graph,
    how="left",
    on="gene_symbol"
)

numeric_cols = [
    "graph_degree",
    "pagerank",
    "betweenness",
    "closeness",
    "component",
]

merged[numeric_cols] = merged[numeric_cols].fillna(0)

outfile = ML_DIR / "ml_training_dataset_graph.csv"
merged.to_csv(outfile, index=False)

print("Merged dataset shape:", merged.shape)
print(merged.head())

print(f"\nSaved to {outfile}")