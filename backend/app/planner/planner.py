from app.planner.workflow import Workflow
from app.planner.task import Task


class Planner:

    def create_workflow(self, goal: str):

        workflow = Workflow(name=goal)

        workflow.add_task(
            Task(
                name="Mutation Analysis",
                agent="Mutation Agent",
                priority=1
            )
        )

        workflow.add_task(
            Task(
                name="Knowledge Graph",
                agent="Graph Agent",
                priority=2
            )
        )

        workflow.add_task(
            Task(
                name="Pathway Analysis",
                agent="Pathway Agent",
                priority=3
            )
        )

        workflow.add_task(
            Task(
                name="Drug Recommendation",
                agent="Drug Agent",
                priority=4
            )
        )

        workflow.add_task(
            Task(
                name="Clinical Evidence",
                agent="Evidence Agent",
                priority=5
            )
        )

        workflow.add_task(
            Task(
                name="Literature Search",
                agent="Literature Agent",
                priority=6
            )
        )

        workflow.add_task(
            Task(
                name="Clinical Trials",
                agent="Clinical Trial Agent",
                priority=7
            )
        )

        workflow.add_task(
            Task(
                name="Evidence Fusion",
                agent="Evidence Fusion Agent",
                priority=8
            )
        )
        workflow.add_task(
    Task(
        name="Explainability",
        agent="Explainability Agent",
        priority=8
    )
)       
        workflow.add_task(
            Task(
                name="Clinical Report",
                agent="Report Agent",
                priority=10
            )
        )

        return workflow