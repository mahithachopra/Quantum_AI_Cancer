import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="quantum_cancer",
    user="postgres",
    password="postgres123",
    port=5432
)

cur = conn.cursor()

# -------------------------
# Genes
# -------------------------

cur.execute("""
CREATE TABLE IF NOT EXISTS genes (

    gene_symbol TEXT PRIMARY KEY,

    tax_id INTEGER,

    gene_id BIGINT,

    synonyms TEXT,

    description TEXT,

    gene_type TEXT,

    chromosome TEXT,

    dgidb_gene_id TEXT
);
""")

# -------------------------
# Mutations
# -------------------------

cur.execute("""
CREATE TABLE IF NOT EXISTS mutations (

    id BIGSERIAL PRIMARY KEY,

mutation_id BIGINT,

    gene_symbol TEXT,

    mutation_type TEXT,

    clinical_significance TEXT,

    chromosome TEXT,

    position BIGINT,

    reference TEXT,

    alternate TEXT,

    review_status TEXT,

    phenotype TEXT
);
""")

# -------------------------
# Pathways
# -------------------------

cur.execute("""
CREATE TABLE IF NOT EXISTS pathways (

    reactome_id TEXT PRIMARY KEY,

    pathway TEXT,

    species TEXT
);
""")

# -------------------------
# Gene Pathway
# -------------------------

cur.execute("""
CREATE TABLE IF NOT EXISTS gene_pathway (

    geneid BIGINT,

    reactome_id TEXT,

    url TEXT,

    pathway TEXT,

    evidence TEXT,

    species TEXT
);
""")

# -------------------------
# Drugs
# -------------------------

cur.execute("""
CREATE TABLE IF NOT EXISTS drugs (

    drug_name TEXT PRIMARY KEY,

    drug_id BIGINT,

    target TEXT,

    pathway TEXT,

    dgidb_drug_id TEXT,

    approved BOOLEAN,

    immunotherapy BOOLEAN,

    anti_neoplastic BOOLEAN
);
""")

# -------------------------
# Gene Drug
# -------------------------

cur.execute("""
CREATE TABLE IF NOT EXISTS gene_drug (

    gene_symbol TEXT,

    drug_name TEXT,

    interaction_type TEXT,

    interaction_score REAL,

    approved BOOLEAN,

    immunotherapy BOOLEAN,

    anti_neoplastic BOOLEAN
);
""")

# -------------------------
# Drug Response
# -------------------------

cur.execute("""
CREATE TABLE IF NOT EXISTS drug_response (

    cosmic_id BIGINT,

    cell_line TEXT,

    cancer_type TEXT,

    drug_id BIGINT,

    drug_name TEXT,

    target TEXT,

    pathway TEXT,

    ln_ic50 REAL,

    auc REAL,

    z_score REAL
);
""")

# -------------------------
# Cell Lines
# -------------------------

cur.execute("""
CREATE TABLE IF NOT EXISTS cell_lines (

    id SERIAL PRIMARY KEY,

    sample_name TEXT,

    cosmic_id BIGINT,

    cancer_type TEXT
);
""")

conn.commit()

cur.close()

conn.close()

print("Database schema created successfully.")