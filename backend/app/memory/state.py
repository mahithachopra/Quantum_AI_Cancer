from enum import Enum


class AgentState(Enum):

    CREATED = "created"

    RUNNING = "running"

    FINISHED = "finished"

    FAILED = "failed"