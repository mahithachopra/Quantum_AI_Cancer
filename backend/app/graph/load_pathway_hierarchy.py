from pathlib import Path
import pandas as pd
from tqdm import tqdm

from connection import get_session
from config import BATCH_SIZE

PROJECT_ROOT = Path(__file__).resolve().parents[3]

RAW = PROJECT_ROOT / "datasets" / "raw" / "reactome"

relations = pd.read_csv(
    RAW / "ReactomePathwaysRelation.txt",
    sep="\t",
    header=None,
    names=["parent", "child"]
)

print("=" * 60)
print("Loading Pathway Hierarchy")
print("=" * 60)

session = get_session()

query = """
UNWIND $rows AS row

MATCH (p1:Pathway {reactome_id: row.parent})
MATCH (p2:Pathway {reactome_id: row.child})

MERGE (p1)-[:PARENT_OF]->(p2)
"""

for i in tqdm(range(0, len(relations), BATCH_SIZE)):
    batch = relations.iloc[i:i+BATCH_SIZE]

    session.run(
        query,
        rows=batch.to_dict("records")
    )

session.close()

print("✓ Pathway hierarchy loaded")