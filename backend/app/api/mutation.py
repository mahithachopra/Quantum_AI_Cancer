from fastapi import APIRouter
from app.tools.mutation_api_tool import MutationTool

router = APIRouter(
    prefix="/mutations",
    tags=["Mutations"]
)

@router.get("/")
def list_mutations():
    return {"message": "Mutation API working"}