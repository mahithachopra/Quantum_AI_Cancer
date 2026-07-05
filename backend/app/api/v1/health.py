from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.postgres import get_db
from app.core.neo4j import get_graph

router = APIRouter(tags=["Health"])


@router.get("/health")
def health(
    db: Session = Depends(get_db),
    graph=Depends(get_graph)
):
    postgres = "OK"
    neo4j = "OK"

    try:
        db.execute(text("SELECT 1"))
    except Exception:
        postgres = "FAILED"

    try:
        graph.run("RETURN 1")
    except Exception:
        neo4j = "FAILED"

    return {
        "status": "healthy" if postgres == "OK" and neo4j == "OK" else "degraded",
        "postgres": postgres,
        "neo4j": neo4j
    }