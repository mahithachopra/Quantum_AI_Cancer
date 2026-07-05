from app.planner import Planner

planner = Planner()

workflow = planner.create_workflow(

    "Analyze EGFR"

)

print()

print(

    workflow.name

)

print()

for task in workflow.ordered_tasks():

    print(

        task.priority,

        task.agent

    )