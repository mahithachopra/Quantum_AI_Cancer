from app.memory import AgentSession
from app.ai_platform.inference_engine import InferenceEngine

session = AgentSession()

session.context.genes = [
    "EGFR",
    "TP53",
    "PIK3CA"
]

session.context.graph_analysis = {}
session.context.pathway_analysis = []
session.context.evidence = {}
session.context.literature = []
session.context.clinical_trials = []

engine = InferenceEngine()

result = engine.infer(session.context)

print("========== AI PLATFORM ==========")
print(result)
print("Inference completed successfully.")