from datetime import datetime

from app.literature.journal_ranker import JournalRanker
from app.literature.disease_matcher import DiseaseMatcher


class LiteratureScorer:

    def __init__(self):

        self.journal = JournalRanker()

        self.disease = DiseaseMatcher()

    def score(self, paper):

        score = 0

        # Gene match

        if paper.gene.lower() in paper.title.lower():

            score += 0.30

        # Drug match

        if paper.drug.lower() in paper.title.lower():

            score += 0.25

        # Disease match

        score += (
            self.disease.score(
                paper.disease,
                paper
            )
            * 0.20
        )

        # Journal quality

        score += (
            self.journal.score(
                paper.journal
            )
            * 0.15
        )

        # Publication recency

        current = datetime.now().year

        diff = max(
            0,
            current - paper.year
        )

        recency = max(
            0,
            1 - diff / 10
        )

        score += recency * 0.10

        return round(score, 3)