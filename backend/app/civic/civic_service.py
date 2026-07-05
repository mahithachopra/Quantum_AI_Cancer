from app.civic.loader import CivicLoader
from app.civic.search import CivicSearch
from app.civic.parser import CivicParser
from app.civic.evidence_ranker import EvidenceRanker


class CivicService:

    def __init__(self):

        self.data = CivicLoader().load()

        self.search = CivicSearch(self.data)

        self.parser = CivicParser()

        self.ranker = EvidenceRanker()

    def query(self, gene):

        evidence_df = self.search.search_gene(gene)

        print(f"{gene}: {len(evidence_df)} evidence rows")

        records = []

        for _, row in evidence_df.iterrows():

            records.append(
                self.parser.parse_evidence(row)
            )

        print(f"{gene}: {len(records)} parsed")

        return self.ranker.rank(records)