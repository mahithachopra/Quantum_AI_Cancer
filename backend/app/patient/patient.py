from dataclasses import dataclass, field
from typing import List

from app.representation.entity import BiologicalEntity


@dataclass
class Patient:

    patient_id: str

    genes: List[BiologicalEntity] = field(default_factory=list)

    drugs: List = field(default_factory=list)

    pathways: List = field(default_factory=list)

    evidence: List = field(default_factory=list)

    literature: List = field(default_factory=list)

    trials: List = field(default_factory=list)

    embedding = None