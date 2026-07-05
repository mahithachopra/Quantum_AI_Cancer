from app.ai_platform.model_loader import ModelLoader


class ModelManager:

    def __init__(self):

        loader = ModelLoader()

        self.rf = loader.random_forest()

        self.xgb = loader.xgboost()

        self.lr = loader.logistic()

        #
        # Sprint 8
        #

        self.qnn = None

        self.qsvc = None

    def random_forest(self):

        return self.rf

    def xgboost(self):

        return self.xgb

    def logistic(self):

        return self.lr

    def quantum(self):

        return self.qnn

    def quantum_svc(self):

        return self.qsvc