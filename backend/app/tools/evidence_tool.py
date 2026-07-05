from app.evidence.evidence_service import EvidenceService


class EvidenceTool:

    def __init__(self):

        self.service = EvidenceService()

    def search(self, genes):

        return self.service.search(
            genes
        )