from app.agents.mutation_agent import MutationAgent
from app.agents.pathway_agent import PathwayAgent
from app.agents.graph_agent import GraphAgent
from app.agents.drug_agent import DrugAgent
from app.agents.literature_agent import LiteratureAgent
from app.agents.clinical_trial_agent import ClinicalTrialAgent
from app.agents.evidence_agent import EvidenceAgent
from app.agents.evidence_fusion_agent import EvidenceFusionAgent
from app.agents.explainability_agent import ExplainabilityAgent
from app.agents.report_agent import ReportAgent


class AgentFactory:

    @staticmethod
    def create(name):

        mapping = {

    "Mutation Agent": MutationAgent,

    "Graph Agent": GraphAgent,

    "Drug Agent": DrugAgent,

    "Pathway Agent": PathwayAgent,

    "Evidence Agent": EvidenceAgent,

    "Literature Agent": LiteratureAgent,

    "Clinical Trial Agent": ClinicalTrialAgent,

    "Evidence Fusion Agent": EvidenceFusionAgent,
    "Explainability Agent": ExplainabilityAgent,
    "Report Agent": ReportAgent,



}
        if name not in mapping:

            raise ValueError(f"{name} not implemented yet.")

        return mapping[name]()