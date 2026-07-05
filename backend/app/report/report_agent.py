from app.agents.base_agent import BaseAgent

from app.report.report_service import ReportService


class ReportAgent(BaseAgent):

    name = "Report Agent"

    description = "Generates final precision oncology report"

    def __init__(self):

        self.service = ReportService()

    def run(self, context):

        print("Running Report Agent")

        report = self.service.build(context)

        context.report = report

        return context