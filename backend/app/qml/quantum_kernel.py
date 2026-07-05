from qiskit_aer import AerSimulator
from qiskit.primitives import StatevectorSampler

from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit_machine_learning.state_fidelities import ComputeUncompute

from app.qml.feature_map import build_feature_map


def build_quantum_kernel():

    feature_map = build_feature_map()

    sampler = StatevectorSampler()

    fidelity = ComputeUncompute(sampler=sampler)

    kernel = FidelityQuantumKernel(
        feature_map=feature_map,
        fidelity=fidelity
    )

    return kernel


if __name__ == "__main__":

    kernel = build_quantum_kernel()

    print(kernel)