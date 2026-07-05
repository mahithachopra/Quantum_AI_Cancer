import pandas as pd

from app.qml.config import OUTPUT_DIR


class QuantumDataLoader:

    def load(self):

        X = pd.read_csv(
            OUTPUT_DIR / "X_quantum.csv"
        )

        y = pd.read_csv(
            OUTPUT_DIR / "y_quantum.csv"
        ).squeeze()

        print()

        print("=" * 60)

        print("Quantum Dataset")

        print("=" * 60)

        print(X.shape)

        print(y.shape)

        print()

        return X, y


if __name__ == "__main__":

    QuantumDataLoader().load()