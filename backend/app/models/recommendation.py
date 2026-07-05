from dataclasses import dataclass, field
from typing import List


@dataclass
class Recommendation:

    gene: str
    drug: str

    ai_score: float = 0

    graph_score: float = 0

    pathway_score: float = 0

    civic_score: float = 0

    literature_score: float = 0

    trial_score: float = 0

    confidence: float = 0

    papers: List = field(default_factory=list)

    trials: List = field(default_factory=list)

    civic: List = field(default_factory=list)

    pathways: List = field(default_factory=list)

    explanation: str = ""