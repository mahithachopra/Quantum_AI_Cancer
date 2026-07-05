class EntityRepository:

    def __init__(self):

        self.entities = {}

    def add(

        self,

        entity

    ):

        self.entities[entity.name] = entity

    def get(

        self,

        name

    ):

        return self.entities.get(name)

    def all(self):

        return list(self.entities.values())