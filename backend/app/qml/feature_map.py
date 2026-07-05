from qiskit.circuit.library import ZZFeatureMap

from app.qml.config import N_QUBITS


def build_feature_map():

    return ZZFeatureMap(

        feature_dimension=N_QUBITS,

        reps=2,

        entanglement="full"

    )


if __name__ == "__main__":

    circuit = build_feature_map()

    print(circuit.draw())