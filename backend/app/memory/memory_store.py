class MemoryStore:

    def __init__(self):

        self._store = {}

    def put(

        self,

        key,

        value

    ):

        self._store[key] = value

    def get(

        self,

        key,

        default=None

    ):

        return self._store.get(

            key,

            default

        )

    def exists(

        self,

        key

    ):

        return key in self._store

    def clear(self):

        self._store.clear()

    def all(self):

        return self._store