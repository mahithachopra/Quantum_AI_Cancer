from qiskit.circuit.library import RealAmplitudes

from app.qml.config import N_QUBITS


def build_ansatz():

    return RealAmplitudes(

        num_qubits=N_QUBITS,

        reps=2,

        entanglement="full"

    )


if __name__ == "__main__":

    circuit = build_ansatz()

    print(circuit.draw())