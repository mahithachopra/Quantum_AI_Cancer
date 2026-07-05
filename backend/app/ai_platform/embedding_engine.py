from app.embeddings.embedding_service import EmbeddingService


class EmbeddingEngine:

    def __init__(self):

        self.service = EmbeddingService()

    def embed(self, context):

        embeddings = {}

        for gene in context.genes:

            embeddings[gene] = self.service.embed(

                gene,

                "Gene"

            )

        return embeddings