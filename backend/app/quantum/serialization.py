import pickle


class QuantumSerializer:

    @staticmethod
    def save(path, obj):

        with open(path, "wb") as f:

            pickle.dump(obj, f)

    @staticmethod
    def load(path):

        with open(path, "rb") as f:

            return pickle.load(f)