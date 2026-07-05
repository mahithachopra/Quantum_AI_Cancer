from app.quantum.model_loader import QuantumModelLoader


class QuantumModelManager:

    def __init__(self):

        self.loader = QuantumModelLoader()

        self.models = {}

    def register(

        self,

        name,

        model

    ):

        self.models[name] = model

    def get(self, name):

        return self.models.get(name)