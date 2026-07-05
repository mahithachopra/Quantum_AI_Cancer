from app.literature.literature_scorer import LiteratureScorer


class PaperRanker:

    def __init__(self):

        self.scorer = LiteratureScorer()

    def rank(self, papers):

        for paper in papers:

            paper.score = self.scorer.score(
                paper
            )

        papers.sort(

            key=lambda x: x.score,

            reverse=True

        )

        return papers