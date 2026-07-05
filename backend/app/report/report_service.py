from app.report.report_builder import ReportBuilder
from app.report.json_renderer import JSONRenderer
from app.report.html_renderer import HTMLRenderer
from app.report.pdf_renderer import PDFRenderer


class ReportService:

    def __init__(self):

        self.builder = ReportBuilder()

        self.json = JSONRenderer()

        self.html = HTMLRenderer()

        self.pdf = PDFRenderer()

    def build(self, context):

        return self.builder.build(context)

    def to_json(self, report):

        return self.json.render(report)

    def to_html(self, report):

        return self.html.render(report)

    def to_pdf(self, report):

        return self.pdf.render(report)