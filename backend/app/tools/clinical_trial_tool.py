from app.clinical_trials.clinical_trial_service import ClinicalTrialService


class ClinicalTrialTool:

    def __init__(self):
        self.service = ClinicalTrialService()

    def search(self, recommendations):
        return self.service.search(recommendations)