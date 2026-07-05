from pathlib import Path

from app.quantum.serialization import QuantumSerializer


class QuantumModelLoader:

    MODEL_DIR = Path("app/quantum/models")

    def load(self, filename):

        return QuantumSerializer.load(

            self.MODEL_DIR / filename

        )