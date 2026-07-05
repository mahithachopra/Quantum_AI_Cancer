from dataclasses import dataclass


@dataclass
class QuantumModelMetadata:

    name: str

    version: str

    backend: str

    feature_dimension: int

    qubits: int

    optimizer: str

    accuracy: float