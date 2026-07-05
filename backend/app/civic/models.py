from dataclasses import dataclass


@dataclass
class CivicEvidence:

    gene: str

    variant: str

    disease: str

    drug: str

    evidence_level: str

    evidence_type: str

    significance: str

    citation: str

    source: str

    score: float = 0.0