from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from neo4j import Session as Neo4jSession

from app.core.postgres import get_db
from app.core.neo4j import get_graph

from app.services.gene_service import GeneService

router = APIRouter(
    prefix="/genes",
    tags=["Genes"]
)


@router.get("/")
def get_genes(
    db: Session = Depends(get_db),
    graph: Neo4jSession = Depends(get_graph),
):
    service = GeneService(db, graph)
    return service.get_all_genes()


@router.get("/{symbol}")
def get_gene(
    symbol: str,
    db: Session = Depends(get_db),
    graph: Neo4jSession = Depends(get_graph),
):
    service = GeneService(db, graph)

    gene = service.get_gene(symbol)

    if gene is None:
        raise HTTPException(
            status_code=404,
            detail="Gene not found",
        )

    return gene


@router.get("/{symbol}/pathways")
def get_gene_pathways(
    symbol: str,
    db: Session = Depends(get_db),
    graph: Neo4jSession = Depends(get_graph),
):
    service = GeneService(db, graph)

    return service.get_gene_pathways(symbol)