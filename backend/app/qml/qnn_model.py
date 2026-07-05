import numpy as np

from qiskit.primitives import StatevectorEstimator

from qiskit.quantum_info import SparsePauliOp

from qiskit_machine_learning.neural_networks import EstimatorQNN

from app.qml.feature_map import build_feature_map
from app.qml.ansatz import build_ansatz


def build_qnn():

    feature_map = build_feature_map()

    ansatz = build_ansatz()

    circuit = feature_map.compose(ansatz)

    estimator = StatevectorEstimator()

    observable = SparsePauliOp.from_list([("Z" + "I"*5, 1)])

    qnn = EstimatorQNN(

        circuit=circuit,

        estimator=estimator,

        observables=observable,

        input_params=feature_map.parameters,

        weight_params=ansatz.parameters

    )

    return qnn


if __name__ == "__main__":

    qnn = build_qnn()

    print(qnn)