from app.analysis.mutation_service import MutationAnalysisService


class MutationTool:

    def __init__(self):

        self.service = MutationAnalysisService()

    def analyze(self, genes):

        return self.service.analyze(
            genes
        )