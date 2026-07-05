from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class BiologicalEntity:

    name: str

    entity_type: str

    graph_features: Dict = field(default_factory=dict)

    pathway_features: Dict = field(default_factory=dict)

    literature_features: Dict = field(default_factory=dict)

    evidence_features: Dict = field(default_factory=dict)

    trial_features: Dict = field(default_factory=dict)

    embedding = None