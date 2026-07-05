from app.representation.entity_builder import EntityBuilder
from app.representation.entity_repository import EntityRepository
from app.representation.entity_embedding import EntityEmbedding


class RepresentationService:

    def __init__(self):

        self.builder = EntityBuilder()

        self.repository = EntityRepository()

        self.embedding = EntityEmbedding()

    def build(self, context):

        for gene in context.genes:

            entity = self.builder.build_gene(

                gene,

                context

            )

            entity = self.embedding.embed(
                entity
            )

            self.repository.add(
                entity
            )

        return self.repository