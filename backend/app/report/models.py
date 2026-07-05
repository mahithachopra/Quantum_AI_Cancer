from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Report:

    patient_id: str

    genes: List[str]

    recommendations: List[Any] = field(default_factory=list)

    evidence: Dict = field(default_factory=dict)

    literature: List = field(default_factory=list)

    clinical_trials: List = field(default_factory=list)

    pathways: List = field(default_factory=list)

    graph: Dict = field(default_factory=dict)

    explanations: List = field(default_factory=list)

    metadata: Dict = field(default_factory=dict)