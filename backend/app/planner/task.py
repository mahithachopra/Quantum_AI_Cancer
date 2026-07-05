from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Any


class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass
class Task:

    name: str

    agent: str

    description: str = ""

    priority: int = 0

    depends_on: List[str] = field(default_factory=list)

    input_data: Dict[str, Any] = field(default_factory=dict)

    output_data: Dict[str, Any] = field(default_factory=dict)

    status: TaskStatus = TaskStatus.PENDING