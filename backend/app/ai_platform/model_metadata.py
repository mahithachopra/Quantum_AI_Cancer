from dataclasses import dataclass


@dataclass
class ModelMetadata:

    name: str

    version: str

    framework: str

    task: str

    input_dimension: int

    output_dimension: int