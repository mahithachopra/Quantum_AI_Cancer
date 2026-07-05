import time

from app.agents.base_agent import BaseAgent
from app.tools.clinical_trial_tool import ClinicalTrialTool
from app.memory.memory_keys import MemoryKeys


class ClinicalTrialAgent(BaseAgent):

    name = "Clinical Trial Agent"

    description = "ClinicalTrials.gov Retrieval"

    def __init__(self):
        self.tool = ClinicalTrialTool()

    def run(self, context):

        start = time.perf_counter()

        trials = self.tool.search(
            context.recommendations
        )

        print(
            f"Clinical trials search: "
            f"{time.perf_counter() - start:.2f} sec"
        )

        context.clinical_trials = trials

        context.memory.memory.save(
            MemoryKeys.CLINICAL_TRIALS,
            trials
        )

        return context