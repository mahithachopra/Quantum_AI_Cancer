from tqdm import tqdm

from postgres_reader import read_table
from connection import get_session
from config import BATCH_SIZE

print("=" * 60)
print("Loading Drug → Gene Relationships")
print("=" * 60)

df = read_table("gene_drug")

# Remove invalid rows
df = df.dropna(subset=["drug_name", "gene_symbol"])
df = df[df["drug_name"].astype(str).str.strip() != ""]

session = get_session()

query = """
UNWIND $rows AS row

MATCH (d:Drug {name: row.drug_name})
MATCH (g:Gene {symbol: row.gene_symbol})

MERGE (d)-[r:TARGETS]->(g)

ON CREATE SET
    r.interaction_type = row.interaction_type,
    r.interaction_score = toFloat(row.interaction_score),
    r.approved = row.approved,
    r.immunotherapy = row.immunotherapy,
    r.anti_neoplastic = row.anti_neoplastic
"""

for start in tqdm(range(0, len(df), BATCH_SIZE)):

    batch = df.iloc[start:start + BATCH_SIZE]

    session.run(
        query,
        rows=batch.to_dict("records")
    )

session.close()

print("\nDrug → Gene relationships loaded successfully.")