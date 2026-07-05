from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class PatientFeatures:

    genes: List[str]

    graph_features: Dict = field(default_factory=dict)

    pathway_features: Dict = field(default_factory=dict)

    evidence_features: Dict = field(default_factory=dict)

    literature_features: Dict = field(default_factory=dict)

    trial_features: Dict = field(default_factory=dict)


@dataclass
class DrugPrediction:

    gene: str

    drug: str

    probability: float

    confidence: float

    metadata: Dict = field(default_factory=dict)


@dataclass
class PredictionResult:

    predictions: List[DrugPrediction] = field(default_factory=list)