from app.services.mutation_service import MutationService
from app.repositories.mutation_repository import MutationRepository

from app.core.postgres import get_db


class MutationTool:

    def __init__(self):

        db = next(get_db())

        repository = MutationRepository(db)

        self.service = MutationService(repository)

    def search(self, gene):

        return self.service.search_gene(gene)

    def list_all(self):

        return self.service.list_mutations()