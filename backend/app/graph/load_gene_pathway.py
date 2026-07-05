from tqdm import tqdm

from postgres_reader import read_table
from connection import get_session
from config import BATCH_SIZE

print("=" * 60)
print("Loading Gene-Pathway Relationships")
print("=" * 60)

df = read_table("gene_pathway")

session = get_session()

query = """
UNWIND $rows AS row

MATCH (g:Gene {gene_id: toInteger(row.geneid)})
MATCH (p:Pathway {reactome_id: row.reactome_id})

MERGE (g)-[r:INVOLVED_IN]->(p)

ON CREATE SET
    r.url = row.url,
    r.evidence = row.evidence,
    r.species = row.species
"""

for start in tqdm(range(0, len(df), BATCH_SIZE)):
    batch = df.iloc[start:start+BATCH_SIZE]

    session.run(query, rows=batch.to_dict("records"))

session.close()

print("Gene → Pathway Relationships Loaded")