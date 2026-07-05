from app.agents.base_agent import BaseAgent
from app.tools.report_tool import ReportTool
from app.memory.memory_keys import MemoryKeys


class ReportAgent(BaseAgent):

    name = "Report Agent"

    description = "Generates final oncology report"

    def __init__(self):
        self.tool = ReportTool()

    def run(self, context):


        context.report = self.tool.generate(
            context
        )
        context.memory.memory.save(

    MemoryKeys.REPORT,

    context.report

)

        return context