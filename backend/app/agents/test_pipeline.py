from app.memory import AgentSession
from app.planner import Planner
from app.registry import RegistryLoader
from app.planner.executor import WorkflowExecutor
from app.report.report_service import ReportService

import json
from pathlib import Path


session = AgentSession()
session.context.genes = [
    "EGFR",
    "TP53",
    "PIK3CA"
]

planner = Planner()
workflow = planner.create_workflow("Analyze Cancer")

registry = RegistryLoader().load()

executor = WorkflowExecutor(registry)

print("\n==========================")
print("FIRST EXECUTION")
print("==========================")

context = executor.execute(
    workflow,
    session.context
)

print("\n==========================")
print("SECOND EXECUTION")
print("==========================")

context = executor.execute(
    workflow,
    session.context
)

print("\n")
print("=" * 80)
print("PIPELINE COMPLETED")
print("=" * 80)

# ----------------------------------
# Build Report
# ----------------------------------

service = ReportService()

report = service.build(context)

# ----------------------------------
# Create output directory
# ----------------------------------

output_dir = Path("outputs")

output_dir.mkdir(exist_ok=True)

# ----------------------------------
# JSON Report
# ----------------------------------

json_report = service.to_json(report)

with open(
    output_dir / "patient_report.json",
    "w"
) as f:

    json.dump(
        json_report,
        f,
        indent=4,
        default=str
    )

# ----------------------------------
# HTML Report
# ----------------------------------

html_report = service.to_html(report)

with open(
    output_dir / "patient_report.html",
    "w"
) as f:

    f.write(html_report)

print("\nReports Generated Successfully\n")

print(output_dir / "patient_report.json")

print(output_dir / "patient_report.html")

print("\nTop Recommendations\n")

for recommendation in report.recommendations[:10]:

    print(

        f"{recommendation.gene:8}"

        f"{recommendation.drug:30}"

        f"{recommendation.confidence:.3f}"

    )
    print("\n")

print("=" * 60)

print("MEMORY CONTENTS")

print("=" * 60)

from pprint import pprint

memory = session.memory.memory.dump()

print("\n========================")

print("MEMORY SUMMARY")

print("========================")

for key, value in memory.items():

    if isinstance(value, dict):

        print(f"{key}: {len(value)} items")

    elif isinstance(value, list):

        print(f"{key}: {len(value)} records")

    else:

        print(f"{key}: {type(value).__name__}")
