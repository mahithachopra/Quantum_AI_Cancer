from app.agents.base_agent import BaseAgent
from app.tools.graph_tool import GraphTool
from app.memory.memory_keys import MemoryKeys


class GraphAgent(BaseAgent):

    name = "Graph Agent"

    description = "Knowledge Graph Analysis"

    def __init__(self):

        self.tool = GraphTool()

    def run(self, context):


        context.graph_analysis = self.tool.analyze(
            context.genes
        )

        context.memory.memory.save(
            MemoryKeys.GRAPH,
            context.graph_analysis
        )

        return context