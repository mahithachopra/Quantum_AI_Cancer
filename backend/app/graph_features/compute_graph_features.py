from pathlib import Path

import networkx as nx
import pandas as pd

OUTPUT_DIR = Path("app/graph_features/output")

edges = pd.read_csv(OUTPUT_DIR / "gene_edges.csv")

print("Building graph...")

G = nx.from_pandas_edgelist(
    edges,
    source="source",
    target="target"
)

print(f"Nodes : {G.number_of_nodes():,}")
print(f"Edges : {G.number_of_edges():,}")
print(f"Connected Components : {nx.number_connected_components(G)}")

print("\nComputing Degree...")
degree = dict(G.degree())

print("Computing PageRank...")
pagerank = nx.pagerank(G)

print("Computing Betweenness...")
betweenness = nx.betweenness_centrality(
    G,
    k=500,
    seed=42
)

print("Computing Closeness...")
closeness = nx.closeness_centrality(G)

print("Computing Connected Components...")
components = {}

for cid, comp in enumerate(nx.connected_components(G)):
    for node in comp:
        components[node] = cid

df = pd.DataFrame({
    "gene_symbol": list(G.nodes()),
    "graph_degree": [degree[n] for n in G.nodes()],
    "pagerank": [pagerank[n] for n in G.nodes()],
    "betweenness": [betweenness[n] for n in G.nodes()],
    "closeness": [closeness[n] for n in G.nodes()],
    "component": [components[n] for n in G.nodes()],
})

print(df.head())

outfile = OUTPUT_DIR / "gene_graph_features.csv"
df.to_csv(outfile, index=False)

print(f"\nSaved to {outfile}")