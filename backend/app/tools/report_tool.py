from app.report.report_service import ReportService


class ReportTool:

    def __init__(self):
        self.service = ReportService()

    def generate(self, context):
        return self.service.build(context)