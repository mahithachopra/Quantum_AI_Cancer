from app.agents.base_agent import BaseAgent

from app.tools.pathway_tool import PathwayTool


class PathwayAgent(BaseAgent):

    name = "Pathway Agent"

    description = "Pathway Reasoning"

    def __init__(self):

        self.tool = PathwayTool()

    def run(self, context):

        context.pathway_analysis = (

            self.tool.analyze(

                context.graph_analysis

            )

        )

        return context