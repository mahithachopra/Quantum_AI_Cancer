from pydantic import BaseModel


class GeneResponse(BaseModel):

    gene_symbol: str
    description: str | None = None
    chromosome: str | None = None
    gene_type: str | None = None