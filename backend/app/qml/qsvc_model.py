from qiskit_machine_learning.algorithms import QSVC

from app.qml.quantum_kernel import build_quantum_kernel


def build_qsvc():

    kernel = build_quantum_kernel()

    model = QSVC(
        quantum_kernel=kernel
    )

    return model


if __name__ == "__main__":

    model = build_qsvc()

    print(model)