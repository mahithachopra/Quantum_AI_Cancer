import numpy as np


class EmbeddingGenerator:

    DIMENSION = 128

    def generate(self, entity):

        np.random.seed(
            abs(hash(entity)) % (2**32)
        )

        return np.random.rand(
            self.DIMENSION
        ).tolist()