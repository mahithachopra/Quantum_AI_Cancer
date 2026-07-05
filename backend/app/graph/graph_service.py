import time

from app.graph.graph_repository import GraphRepository
from app.graph.graph_analytics_service import GraphAnalyticsService

class GraphService:

    def __init__(self):

        self.repo = GraphRepository()
        self.analytics = GraphAnalyticsService()

    def analyze(self, genes: list[str]) -> dict:

        graph = {}

        for gene in genes:
            start = time.perf_counter()

            row = self.repo.get_gene_context(gene)
            print(
        f"{gene} Neo4j query: "
        f"{time.perf_counter() - start:.2f} sec"
    )

            if row is None:

                continue

            graph[gene] = self.analytics.analyze_gene(

    {

        "pathways": row["pathways"],

        "drugs": row["drugs"],

        "neighbors": row["neighbors"]

    }

)
    
        return graph