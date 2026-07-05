from app.memory.session_memory import SessionMemory
from app.memory.memory_keys import MemoryKeys


memory = SessionMemory()

memory.memory.save(

    MemoryKeys.GRAPH,

    {

        "EGFR": {

            "degree": 15

        }

    }

)

print()

print(memory.memory.load(

    MemoryKeys.GRAPH

))

print()

print(memory.memory.dump())