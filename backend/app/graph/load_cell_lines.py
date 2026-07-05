from tqdm import tqdm

from postgres_reader import read_table
from connection import get_session
from config import BATCH_SIZE

print("=" * 60)
print("Loading Cell Line Nodes")
print("=" * 60)

df = read_table("cell_lines")

session = get_session()

query = """
UNWIND $rows AS row

MERGE (c:CellLine {name: row.sample_name})

SET

c.cosmic_id = row.cosmic_id,
c.cancer_type = row.cancer_type
"""

for start in tqdm(range(0, len(df), BATCH_SIZE)):
    batch = df.iloc[start:start+BATCH_SIZE]

    session.run(
        query,
        rows=batch.to_dict("records")
    )

session.close()

print("✓ Cell Lines Loaded")