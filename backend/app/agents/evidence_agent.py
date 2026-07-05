from app.agents.base_agent import BaseAgent
from app.tools.evidence_tool import EvidenceTool
from app.memory.memory_keys import MemoryKeys


class EvidenceAgent(BaseAgent):

    name = "Evidence Agent"

    description = "Clinical Evidence Retrieval"

    def __init__(self):

        self.tool = EvidenceTool()

    def run(self, context):

        context.evidence = self.tool.search(
            context.genes
        )
        context.memory.memory.save(

    MemoryKeys.EVIDENCE,

    context.evidence

)

        return context