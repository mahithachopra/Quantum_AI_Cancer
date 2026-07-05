from app.memory.memory_store import MemoryStore


class MemoryService:

    def __init__(self):

        self.store = MemoryStore()

    def save(

        self,

        key,

        value

    ):

        self.store.put(

            key,

            value

        )

    def load(

        self,

        key

    ):

        return self.store.get(

            key

        )

    def has(

        self,

        key

    ):

        return self.store.exists(

            key

        )

    def clear(self):

        self.store.clear()

    def dump(self):

        return self.store.all()