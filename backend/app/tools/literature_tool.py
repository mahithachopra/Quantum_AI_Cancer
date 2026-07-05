from app.literature.literature_service import LiteratureService
from app.literature.paper_ranker import PaperRanker
from app.literature.paper_summarizer import PaperSummarizer


class LiteratureTool:

    def __init__(self):
        self.service = LiteratureService()
        self.ranker = PaperRanker()
        self.summarizer = PaperSummarizer()

    def search(self, graph, recommendations, pathways):

        papers = self.service.retrieve(
            graph,
            recommendations,
            pathways
        )

        print("Retrieved papers:", len(papers))

        ranked = self.ranker.rank(papers)

        print("Ranked papers:", len(ranked))

        summaries = [
            self.summarizer.summarize(paper)
            for paper in ranked
        ]

        print("Summaries:", len(summaries))

        return summaries