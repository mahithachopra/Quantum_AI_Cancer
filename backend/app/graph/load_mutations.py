from pathlib import Path
import pandas as pd
from tqdm import tqdm

from connection import get_session
from config import BATCH_SIZE

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA = PROJECT_ROOT / "datasets" / "processed"

print("=" * 60)
print("Loading Mutation Nodes")
print("=" * 60)

session = get_session()

query = """
UNWIND $rows AS row

MERGE (
    m:Mutation {
        mutation_key:
            row.mutation_id + "_" +
            row.chromosome + "_" +
            toString(row.position)
    }
)

SET
m.variation_id = toInteger(row.mutation_id),
m.gene_symbol = row.gene_symbol,
m.mutation_type = row.mutation_type,
m.clinical_significance = row.clinical_significance,
m.chromosome = row.chromosome,
m.position = toInteger(row.position),
m.reference = row.reference,
m.alternate = row.alternate,
m.review_status = row.review_status,
m.phenotype = row.phenotype
"""

reader = pd.read_csv(
    DATA / "mutations_final.csv",
    chunksize=BATCH_SIZE,
    low_memory=False
)

total = 8935541
steps = (total // BATCH_SIZE) + 1

for chunk in tqdm(reader, total=steps):

    chunk = chunk.fillna("")

    session.run(
        query,
        rows=chunk.to_dict("records")
    )

session.close()

print("\nMutation Nodes Loaded Successfully")