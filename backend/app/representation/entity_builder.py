from app.representation.entity import BiologicalEntity


class EntityBuilder:

    def build_gene(

        self,

        gene,

        context

    ):

        return BiologicalEntity(

            name=gene,

            entity_type="Gene",

            graph_features=context.graph_analysis.get(
                gene,
                {}
            )
        )