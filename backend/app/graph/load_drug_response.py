from tqdm import tqdm

from postgres_reader import read_table
from connection import get_session
from config import BATCH_SIZE

print("=" * 60)
print("Loading CellLine → Drug Relationships")
print("=" * 60)

df = read_table("drug_response")

session = get_session()

query = """
UNWIND $rows AS row

MATCH (c:CellLine {cosmic_id: toInteger(row.cosmic_id)})
MATCH (d:Drug {name: row.drug_name})

MERGE (c)-[r:RESPONDS_TO]->(d)

ON CREATE SET

r.ln_ic50 = toFloat(row.ln_ic50),
r.auc = toFloat(row.auc),
r.z_score = toFloat(row.z_score),
r.cancer_type = row.cancer_type
"""

for start in tqdm(range(0, len(df), BATCH_SIZE)):

    batch = df.iloc[start:start+BATCH_SIZE]

    session.run(
        query,
        rows=batch.to_dict("records")
    )

session.close()

print("CellLine → Drug Relationships Loaded")