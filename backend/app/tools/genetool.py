from app.services.gene_service import GeneService

from app.core.postgres import get_db
from app.core.neo4j import get_session


class GeneTool:

    def __init__(self):

        db = next(get_db())

        graph = get_session()

        self.service = GeneService(
            db,
            graph
        )

    def gene(self, symbol):

        return self.service.get_gene(symbol)

    def pathways(self, symbol):

        return self.service.get_gene_pathways(symbol)

    def genes(self):

        return self.service.get_all_genes()