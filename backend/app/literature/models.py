from dataclasses import dataclass, field
from typing import List


@dataclass
class Paper:

    title: str
    journal: str
    year: int
    authors: str

    abstract: str

    pmid: str
    doi: str
    url: str

    gene: str
    drug: str
    disease: str

    publication_type: str = ""

    source: str = "Europe PMC"

    keywords: List[str] = field(default_factory=list)

    score: float = 0.0