from tqdm import tqdm

from postgres_reader import read_table
from connection import get_session
from config import BATCH_SIZE

print("=" * 60)
print("Loading Pathway Nodes")
print("=" * 60)

df = read_table("pathways")

session = get_session()

query = """
UNWIND $rows AS row

MERGE (p:Pathway {reactome_id: row.reactome_id})

SET
p.name = row.pathway,
p.species = row.species
"""

for start in tqdm(range(0, len(df), BATCH_SIZE)):
    batch = df.iloc[start:start+BATCH_SIZE]

    session.run(
        query,
        rows=batch.to_dict("records")
    )

session.close()

print("✓ Pathways Loaded")