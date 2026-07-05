from sqlalchemy import text
import pandas as pd

from app.core.postgres import SessionLocal
from app.core.neo4j import driver

class FeatureEngineer:

    def __init__(self):
        self.db = SessionLocal()
        self.graph = driver.session()

    def close(self):
        self.db.close()
        self.graph.close()

    # -------------------------
    # Mutation count
    # -------------------------

    def mutation_counts(self):

        query = text("""
            SELECT
                gene_symbol,
                COUNT(*) AS mutation_count
            FROM mutations
            GROUP BY gene_symbol
        """)

        return pd.read_sql(query, self.db.connection())

    # -------------------------
    # Pathway count
    # -------------------------

    def pathway_counts(self):

        cypher = """
        MATCH (g:Gene)-[:INVOLVED_IN]->(p:Pathway)

        RETURN
        g.symbol AS gene_symbol,
        COUNT(p) AS pathway_count
        """

        records = self.graph.run(cypher)

        return pd.DataFrame([r.data() for r in records])

    # -------------------------
    # Drug count
    # -------------------------

    def drug_counts(self):

        cypher = """
        MATCH (g:Gene)<-[:TARGETS]-(d:Drug)

        RETURN
        g.symbol AS gene_symbol,
        COUNT(d) AS drug_count
        """

        records = self.graph.run(cypher)

        return pd.DataFrame([r.data() for r in records])

    # -------------------------
    # Degree Centrality
    # -------------------------

    def degree_features(self):

        cypher = """
MATCH (g:Gene)
OPTIONAL MATCH (g)-[r]-()

RETURN
g.symbol AS gene_symbol,
COUNT(r) AS degree
"""

        records = self.graph.run(cypher)

        return pd.DataFrame([r.data() for r in records])