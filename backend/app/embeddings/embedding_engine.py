from app.embeddings.embedding_service import EmbeddingService


class EmbeddingEngine:

    def __init__(self):

        self.service = EmbeddingService()

    def embed(self, context):

        embeddings = {}

        for recommendation in context.recommendations:

            gene = recommendation["gene"]

            embeddings[gene] = self.service.embed(

                entity=gene,

                entity_type="Gene"

            )

        return embeddings