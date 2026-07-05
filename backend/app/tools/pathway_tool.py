from app.pathway.pathway_service import PathwayService


class PathwayTool:

    def __init__(self):

        self.service = PathwayService()

    def analyze(self, graph_analysis):

        return self.service.analyze(
            graph_analysis
        )