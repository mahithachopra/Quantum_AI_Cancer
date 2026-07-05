from app.agents.base_agent import BaseAgent
from app.tools.explainability_tool import ExplainabilityTool
from app.memory.memory_keys import MemoryKeys


class ExplainabilityAgent(BaseAgent):

    name = "Explainability Agent"

    description = "Generates interpretable explanations"

    def __init__(self):
        self.tool = ExplainabilityTool()

    def run(self, context):


        context.explanations = self.tool.explain(context)
        context.memory.memory.save(

    MemoryKeys.EXPLAINABILITY,

    context.explanations

)

        print("Explainability finished")


        return context