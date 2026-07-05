from app.memory import AgentSession
from app.agents.mutation_agent import MutationAgent
from app.agents.graph_agent import GraphAgent
from app.agents.pathway_agent import PathwayAgent
from app.agents.drug_agent import DrugAgent
from app.agents.evidence_agent import EvidenceAgent
from app.agents.literature_agent import LiteratureAgent
from app.agents.clinical_trial_agent import ClinicalTrialAgent
from app.evidence_fusion.fusion_engine import FusionEngine

session = AgentSession()

session.context.genes = [
    "EGFR",
    "TP53",
    "PIK3CA"
]

MutationAgent().run(session.context)
GraphAgent().run(session.context)
PathwayAgent().run(session.context)
DrugAgent().run(session.context)
EvidenceAgent().run(session.context)
LiteratureAgent().run(session.context)
ClinicalTrialAgent().run(session.context)

engine = FusionEngine()

results = engine.fuse(session.context)

print("\n===== Evidence Fusion =====\n")

for r in results[:10]:

    print(f"Gene       : {r.gene}")
    print(f"Drug       : {r.drug}")
    print(f"AI Score   : {r.ai_score:.3f}")
    print(f"CIViC      : {r.civic_score:.3f}")
    print(f"Literature : {r.literature_score:.3f}")
    print(f"Trials     : {r.trial_score:.3f}")
    print(f"Graph      : {r.graph_score:.3f}")
    print(f"Pathway    : {r.pathway_score:.3f}")
    print(f"Confidence : {r.confidence:.3f}")
    print("-" * 60)