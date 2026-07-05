from app.graph.graph_service import GraphService


class GraphTool:

    def __init__(self):

        self.service = GraphService()

    def analyze(self, genes):

        return self.service.analyze(genes)