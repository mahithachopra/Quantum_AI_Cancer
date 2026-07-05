from dataclasses import dataclass


@dataclass
class ClinicalTrial:
    gene: str

    drug: str

    nct_id: str

    title: str

    status: str

    phase: str

    condition: str

    intervention: str

    country: str

    url: str

    score: float = 0.0