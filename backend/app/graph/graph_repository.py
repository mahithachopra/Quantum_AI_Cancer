from neo4j import GraphDatabase
from app.core.config import settings

import math


class GraphRepository:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(
                settings.NEO4J_USER,
                settings.NEO4J_PASSWORD
            )
        )

    def close(self):

        self.driver.close()

    def _clean(self, obj):

        if isinstance(obj, dict):

            return {
                k: self._clean(v)
                for k, v in obj.items()
            }

        if isinstance(obj, list):

            return [
                self._clean(v)
                for v in obj
            ]

        if isinstance(obj, float):

            if math.isnan(obj) or math.isinf(obj):

                return None

        return obj

    def get_gene_context(self, gene):

        query = """
MATCH (g:Gene {symbol:$gene})

CALL {
    WITH g
    OPTIONAL MATCH (g)-[:INVOLVED_IN]->(p:Pathway)
    RETURN
    collect(DISTINCT p.name)[0..15] AS pathways
}

CALL {
    WITH g
    OPTIONAL MATCH (d:Drug)-[:TARGETS]->(g)
    RETURN
    collect(
        DISTINCT {
            name:d.name,
            approved:d.approved,
            immunotherapy:d.immunotherapy,
            anti_neoplastic:d.anti_neoplastic,
            target:d.target,
            pathway:d.pathway
        }
    )[0..20] AS drugs
}

CALL {
    WITH g
    OPTIONAL MATCH (g)--(n)
    RETURN
    collect(
        DISTINCT {
            name:coalesce(n.symbol,n.name),
            labels:labels(n)
        }
    )[0..30] AS neighbors
}

RETURN
g.symbol AS gene,
pathways,
drugs,
neighbors
"""

        with self.driver.session() as session:

            result = session.run(
                query,
                gene=gene
            )

            record = result.single()

            if record is None:
                return None

            return self._clean(dict(record))