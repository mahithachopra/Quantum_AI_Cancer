import uuid

from app.memory.context import AgentContext
from app.memory.history import ExecutionHistory
from app.memory.cache import AgentCache
from app.memory.session_memory import SessionMemory


class AgentSession:

    def __init__(self):

        self.id = str(
            uuid.uuid4()
        )

        self.context = AgentContext()

        self.history = ExecutionHistory()

        self.cache = AgentCache()

        self.memory = SessionMemory()

        #
        # Make memory accessible from every agent
        #

        self.context.memory = self.memory