from app.civic.civic_service import CivicService


class CivicTool:

    def __init__(self):

        self.service = CivicService()

    def search(self, genes):

        evidence = {}

        for gene in genes:

            evidence[gene] = self.service.query(gene)

        return evidence