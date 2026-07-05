from app.repositories.mutation_repository import MutationRepository


class MutationService:

    def __init__(self, repository):
        self.repository = repository

    def get_mutation(self, mutation_id):

        return self.repository.get_by_id(mutation_id)

    def search_gene(self, gene):

        return self.repository.search_gene(gene)

    def list_mutations(self):

        return self.repository.list_mutations()