from pathlib import Path
import json

from app.memory import AgentSession
from app.planner import Planner
from app.planner.executor import WorkflowExecutor
from app.registry import RegistryLoader
from app.report.report_service import ReportService


class PipelineService:

    def __init__(self):

        self.registry = RegistryLoader().load()

        self.executor = WorkflowExecutor(

            self.registry

        )

        self.planner = Planner()

        self.report_service = ReportService()

    def analyze(

        self,

        genes

    ):

        session = AgentSession()

        session.context.genes = genes

        workflow = self.planner.create_workflow(

            "Analyze Cancer"

        )

        context = self.executor.execute(

            workflow,

            session.context

        )

        report = self.report_service.build(

            context

        )

        return context, report