from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Explanation:

    gene: str

    drug: str

    confidence: float

    confidence_level: str

    reasoning: List[str] = field(default_factory=list)

    ai_score: float = 0.0

    graph_score: float = 0.0

    pathway_score: float = 0.0

    civic_score: float = 0.0

    literature_score: float = 0.0

    trial_score: float = 0.0

    graph_connections: int = 0

    pathway_count: int = 0

    literature_count: int = 0

    trial_count: int = 0

    civic_count: int = 0

    evidence: Dict = field(default_factory=dict)