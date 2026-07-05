from pathlib import Path

import pandas as pd
from neo4j import GraphDatabase

from app.core.config import settings

OUTPUT_DIR = Path("app/graph_features/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

driver = GraphDatabase.driver(
    settings.NEO4J_URI,
    auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
)

QUERY = """
MATCH (g1:Gene)-[:INVOLVED_IN]->(p:Pathway)<-[:INVOLVED_IN]-(g2:Gene)
WHERE g1.symbol <> g2.symbol
RETURN DISTINCT
    g1.symbol AS source,
    g2.symbol AS target
"""

with driver.session() as session:
    records = session.run(QUERY)
    edges = [record.data() for record in records]

driver.close()

df = pd.DataFrame(edges)

print(df.head())
print()
print("Edges:", len(df))

outfile = OUTPUT_DIR / "gene_edges.csv"
df.to_csv(outfile, index=False)

print(f"\nSaved to {outfile}")