from app.memory import AgentSession

from app.report.report_service import ReportService

session = AgentSession()

session.context.patient_id = "TEST001"

session.context.genes = [

    "EGFR",

    "TP53"

]

service = ReportService()

report = service.build(

    session.context

)

print(report)

print()

print(service.to_json(report))

print()

print(service.to_html(report))