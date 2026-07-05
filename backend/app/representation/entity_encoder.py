class EntityEncoder:

    def encode(

        self,

        entity

    ):

        return {

            "name": entity.name,

            "type": entity.entity_type

        }