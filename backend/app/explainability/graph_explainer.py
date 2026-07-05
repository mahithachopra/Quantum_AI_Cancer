class GraphExplainer:

    def explain(self, recommendation, context):

        gene = recommendation.gene

        node = context.graph_analysis.get(gene, {})

        # If already a list
        if isinstance(node, list):

            neighbours = node

        # If dictionary
        elif isinstance(node, dict):

            neighbours = (
                node.get("connections")
                or node.get("neighbors")
                or node.get("neighbours")
                or []
            )

        else:

            neighbours = []

        return {

            "connections": len(neighbours),

            "top_neighbours": neighbours[:10]

        }