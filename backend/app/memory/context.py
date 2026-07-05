from dataclasses import dataclass, field
from typing import Dict, List, Any


@dataclass
class AgentContext:

    patient_id: str = ""

    workflow: str = ""
    embeddings = None

    ai_confidence = 0

    current_agent = ""

    feedback = []

    learning_state = {}

    genes: List[str] = field(default_factory=list)

    mutation_analysis: Dict = field(default_factory=dict)

    pathway_analysis: Dict = field(default_factory=dict)

    graph_analysis: Dict = field(default_factory=dict)

    recommendations: List = field(default_factory=list)
    evidence: Dict = field(default_factory=dict)

    drug_combinations: List = field(default_factory=list)

    quantum_analysis: Dict = field(default_factory=dict)

    explainability: Dict = field(default_factory=dict)

    literature: List = field(default_factory=list)

    clinical_trials: List = field(default_factory=list)
    explanations: list = field(default_factory=list)

    fused_recommendations: list = field(default_factory=list)

    report: Dict = field(default_factory=dict)

    metadata: Dict[str, Any] = field(default_factory=dict)
