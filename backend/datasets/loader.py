from pathlib import Path
import pandas as pd


class DatasetLoader:

    def __init__(self):

        base = Path("app/ml/output")

        self.X_train = pd.read_csv(base / "X_train.csv")
        self.X_test = pd.read_csv(base / "X_test.csv")

        self.y_train = pd.read_csv(base / "y_train.csv").squeeze()
        self.y_test = pd.read_csv(base / "y_test.csv").squeeze()

        self.meta_train = pd.read_csv(base / "metadata_train.csv")
        self.meta_test = pd.read_csv(base / "metadata_test.csv")

    def load(self):

        return (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test,
            self.meta_train,
            self.meta_test,
        )


if __name__ == "__main__":

    loader = DatasetLoader()

    X_train, X_test, y_train, y_test, meta_train, meta_test = loader.load()

    print("X_train:", X_train.shape)
    print("X_test :", X_test.shape)
    print("y_train:", y_train.shape)
    print("y_test :", y_test.shape)
    print("Metadata:", meta_train.shape)