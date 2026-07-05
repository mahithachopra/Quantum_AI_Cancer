from pydantic import BaseModel


class MutationResponse(BaseModel):

    mutation_id: int

    gene_symbol: str

    mutation_type: str | None = None

    clinical_significance: str | None = None

    chromosome: str | None = None

    position: int | None = None

    phenotype: str | None = None