from pathlib import Path
import psycopg2

# -----------------------------------------------------
# PostgreSQL Connection
# -----------------------------------------------------

conn = psycopg2.connect(
    host="localhost",
    database="quantum_cancer",
    user="postgres",
    password="postgres123",
    port=5432,
)

conn.autocommit = False
cur = conn.cursor()

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA = PROJECT_ROOT / "datasets" / "processed"

# -----------------------------------------------------
# Clean Tables
# -----------------------------------------------------

print("=" * 60)
print("Cleaning Database...")
print("=" * 60)

cur.execute("""
TRUNCATE TABLE
gene_drug,
gene_pathway,
drug_response,
cell_lines,
mutations,
drugs,
pathways,
genes
RESTART IDENTITY CASCADE;
""")

conn.commit()

print("✓ Tables cleaned.\n")

# -----------------------------------------------------
# Column Mapping
# -----------------------------------------------------

TABLE_COLUMNS = {

    "genes": [
        "gene_symbol",
        "tax_id",
        "gene_id",
        "synonyms",
        "description",
        "gene_type",
        "chromosome",
        "dgidb_gene_id",
    ],

    "mutations": [
        "mutation_id",
        "gene_symbol",
        "mutation_type",
        "clinical_significance",
        "chromosome",
        "position",
        "reference",
        "alternate",
        "review_status",
        "phenotype",
    ],

    "pathways": [
        "reactome_id",
        "pathway",
        "species",
    ],

    "gene_pathway": [
        "geneid",
        "reactome_id",
        "url",
        "pathway",
        "evidence",
        "species",
    ],

    "drugs": [
    "drug_id",
    "drug_name",
    "target",
    "pathway",
    "dgidb_drug_id",
    "approved",
    "immunotherapy",
    "anti_neoplastic",
],

    "gene_drug": [
        "gene_symbol",
        "drug_name",
        "interaction_type",
        "interaction_score",
        "approved",
        "immunotherapy",
        "anti_neoplastic",
    ],

    "drug_response": [
        "cosmic_id",
        "cell_line",
        "cancer_type",
        "drug_id",
        "drug_name",
        "target",
        "pathway",
        "ln_ic50",
        "auc",
        "z_score",
    ],

    "cell_lines": [
        "sample_name",
        "cosmic_id",
        "cancer_type",
    ],
}
# -----------------------------------------------------
# COPY Helper
# -----------------------------------------------------

def copy_csv(table, filename):

    filepath = DATA / filename

    print(f"Loading {table}...")

    if not filepath.exists():
        raise FileNotFoundError(filepath)

    columns = TABLE_COLUMNS.get(table)

    if columns:
        column_sql = "(" + ",".join(columns) + ")"
    else:
        column_sql = ""

    sql = f"""
    COPY {table} {column_sql}
    FROM STDIN
    WITH (
        FORMAT CSV,
        HEADER TRUE,
        DELIMITER ',',
        QUOTE '"'
    );
    """

    try:

        with open(filepath, "r", encoding="utf-8") as f:
            cur.copy_expert(sql, f)

        conn.commit()

        cur.execute(f"SELECT COUNT(*) FROM {table};")
        rows = cur.fetchone()[0]

        print(f"✓ {table} loaded ({rows:,} rows)\n")

    except Exception as e:

        conn.rollback()

        print(f"\n❌ Failed loading {table}")
        print(e)

        raise

# -----------------------------------------------------
# Load Order
# -----------------------------------------------------

FILES = [

    ("genes", "genes_final.csv"),

    ("mutations", "mutations_final.csv"),

    ("pathways", "pathways_final.csv"),

    ("gene_pathway", "gene_pathway_final.csv"),

    ("drugs", "drugs_final.csv"),

    ("gene_drug", "gene_drug_final.csv"),

    ("drug_response", "drug_response_final.csv"),

    ("cell_lines", "cell_lines_final.csv"),
]

print("=" * 60)
print("Importing CSV Files")
print("=" * 60)

for table, filename in FILES:
    copy_csv(table, filename)

print("=" * 60)
print("DATABASE IMPORT COMPLETED")
print("=" * 60)

cur.close()
conn.close()