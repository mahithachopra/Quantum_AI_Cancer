from dataclasses import dataclass


@dataclass
class FusionRecommendation:

    gene: str

    drug: str

    ai_score: float

    civic_score: float

    literature_score: float

    trial_score: float

    graph_score: float

    pathway_score: float

    confidence: float = 0.0