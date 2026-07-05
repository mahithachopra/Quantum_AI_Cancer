from app.repositories.postgres_repository import PostgresRepository
from app.repositories.neo4j_repository import Neo4jRepository


class GeneService:

    def __init__(self, db, graph):
        self.pg = PostgresRepository(db)
        self.graph = Neo4jRepository(graph)

    def get_all_genes(self):

        query = """
        SELECT
            gene_symbol,
            description,
            chromosome,
            gene_type
        FROM genes
        ORDER BY gene_symbol
        LIMIT 100
        """

        return self.pg.fetch_all(query)

    def get_gene(self, symbol):

        query = """
        SELECT *
        FROM genes
        WHERE gene_symbol=:symbol
        """

        return self.pg.fetch_one(
            query,
            {"symbol": symbol}
        )

    def get_gene_pathways(self, symbol):

        cypher = """
        MATCH (g:Gene {symbol:$symbol})

        -[:INVOLVED_IN]->

        (p:Pathway)

        RETURN
        p.reactome_id AS pathway_id,
        p.name AS pathway
        ORDER BY pathway
        """

        return self.graph.run(
            cypher,
            {"symbol": symbol}
        )