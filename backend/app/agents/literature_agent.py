import time
from app.agents.base_agent import BaseAgent
from app.tools.literature_tool import LiteratureTool
from app.memory.memory_keys import MemoryKeys


class LiteratureAgent(BaseAgent):

    name = "Literature Agent"

    description = "Biomedical Evidence Agent"

    def __init__(self):

        self.tool = LiteratureTool()

    def run(self, context):

        start = time.perf_counter()

        papers = self.tool.search(
            context.graph_analysis,
            context.recommendations,
            context.pathway_analysis
        )

        print(
            f"Literature search: "
            f"{time.perf_counter() - start:.2f} sec"
        )

        context.literature = papers

        context.memory.memory.save(
            MemoryKeys.LITERATURE,
            papers
        )

        return context