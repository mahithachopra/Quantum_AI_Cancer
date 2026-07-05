from app.embeddings.embedding_generator import EmbeddingGenerator
from app.embeddings.embedding_models import Embedding


class EmbeddingService:

    def __init__(self):

        self.generator = EmbeddingGenerator()

    def embed(
        self,
        entity,
        entity_type
    ):

        vector = self.generator.generate(
            entity
        )

        return Embedding(

            entity=entity,

            entity_type=entity_type,

            vector=vector,

            source="SharedEmbedding"

        )