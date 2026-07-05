from dataclasses import dataclass
from typing import List


@dataclass
class Embedding:

    entity: str

    entity_type: str

    vector: List[float]

    source: str

    metadata: dict | None = None