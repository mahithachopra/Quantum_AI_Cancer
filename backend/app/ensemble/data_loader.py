from pathlib import Path

import pandas as pd


OUTPUT = Path("app/ml/output")


class EnsembleDataLoader:

    def __init__(self):

        self.train = pd.read_csv(
            OUTPUT / "train.csv"
        )

        self.test = pd.read_csv(
            OUTPUT / "test.csv"
        )

    def load(self):

        X_train = self.train.drop(columns=["target"])

        y_train = self.train["target"]

        X_test = self.test.drop(columns=["target"])

        y_test = self.test["target"]

        return X_train, X_test, y_train, y_test


if __name__ == "__main__":

    loader = EnsembleDataLoader()

    X_train, X_test, y_train, y_test = loader.load()

    print(X_train.shape)

    print(X_test.shape)