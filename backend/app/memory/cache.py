class AgentCache:

    def __init__(self):

        self.cache = {}

    def get(

        self,

        key

    ):

        return self.cache.get(key)

    def put(

        self,

        key,

        value

    ):

        self.cache[key] = value

    def exists(

        self,

        key

    ):

        return key in self.cache

    def clear(self):

        self.cache.clear()