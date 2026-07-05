from app.agents.base_agent import BaseAgent
from app.tools.mutation_tool import MutationTool
from app.memory.memory_keys import MemoryKeys


class MutationAgent(BaseAgent):

    name = "Mutation Agent"

    description = "Mutation Analysis"

    def __init__(self):

        self.tool = MutationTool()

    def run(self, context):

        result = self.tool.analyze(
            context.genes
        )

        context.mutation_analysis = result

        context.memory.memory.save(
            MemoryKeys.MUTATION,
            result
        )

        return context