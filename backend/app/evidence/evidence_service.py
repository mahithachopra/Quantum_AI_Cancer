from app.tools.civic_tool import CivicTool


class EvidenceService:

    def __init__(self):

        self.civic = CivicTool()

    def search(self, genes):

        return self.civic.search(
            genes
        )