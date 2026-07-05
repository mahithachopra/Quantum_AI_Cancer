class PathwayExplainer:

    def explain(self, recommendation, context):

        gene = recommendation.gene

        pathways = []

        for pathway in context.pathway_analysis:

            if gene in pathway["genes"]:

                pathways.append(pathway)

        return {

            "count": len(pathways),

            "pathways": pathways

        }