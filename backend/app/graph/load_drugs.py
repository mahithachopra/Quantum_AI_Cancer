from tqdm import tqdm

from postgres_reader import read_table
from connection import get_session
from config import BATCH_SIZE

print("=" * 60)
print("Loading Drug Nodes")
print("=" * 60)

df = read_table("drugs")

session = get_session()

query = """
UNWIND $rows AS row

MERGE (d:Drug {name: row.drug_name})

SET

d.drug_id = row.drug_id,
d.target = row.target,
d.pathway = row.pathway,
d.dgidb_drug_id = row.dgidb_drug_id,
d.approved = row.approved,
d.immunotherapy = row.immunotherapy,
d.anti_neoplastic = row.anti_neoplastic
"""

for start in tqdm(range(0, len(df), BATCH_SIZE)):
    batch = df.iloc[start:start+BATCH_SIZE]

    session.run(
        query,
        rows=batch.to_dict("records")
    )

session.close()

print("✓ Drugs Loaded")