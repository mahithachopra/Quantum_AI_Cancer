from tqdm import tqdm

from postgres_reader import read_table

from connection import get_session

from config import BATCH_SIZE

print("Reading PostgreSQL...")

genes = read_table("genes")

session = get_session()

query = """

UNWIND $rows AS row

MERGE (g:Gene {symbol:row.gene_symbol})

SET

g.gene_id=row.gene_id,

g.tax_id=row.tax_id,

g.description=row.description,

g.synonyms=row.synonyms,

g.chromosome=row.chromosome,

g.gene_type=row.gene_type

"""

for start in tqdm(range(0, len(genes), BATCH_SIZE)):

    batch = genes.iloc[start:start+BATCH_SIZE]

    session.run(

        query,

        rows=batch.to_dict("records")

    )

session.close()

print("Genes Loaded")