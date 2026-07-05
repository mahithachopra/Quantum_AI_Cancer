from app.agents.base_agent import BaseAgent
from app.tools.evidence_fusion_tool import EvidenceFusionTool
from app.memory.memory_keys import MemoryKeys


class EvidenceFusionAgent(BaseAgent):

    name="Evidence Fusion Agent"

    description="Multi-source evidence fusion"

    def __init__(self):

        self.tool=EvidenceFusionTool()

    def run(self,context):


        context.fused_recommendations=self.tool.fuse(context)
        context.memory.memory.save(

    MemoryKeys.FUSION,

    context.fused_recommendations

)

        return context