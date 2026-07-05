class GraphAnalyticsService:

    def analyze_gene(self, gene_context):

        pathways = gene_context.get("pathways", [])

        drugs = gene_context.get("drugs", [])

        neighbours = gene_context.get("neighbors", [])

        approved = sum(
            1
            for d in drugs
            if d.get("approved")
        )

        immunotherapy = sum(
            1
            for d in drugs
            if d.get("immunotherapy")
        )

        anti_neoplastic = sum(
            1
            for d in drugs
            if d.get("anti_neoplastic")
        )

        degree = len(neighbours)

        graph_degree = degree

        pathway_count = len(pathways)

        drug_count = len(drugs)

        interaction_score = degree + drug_count + pathway_count

        #
        # Temporary graph metrics.
        # Later these will come from Neo4j GDS.
        #

        pagerank = degree / 100

        betweenness = degree / 50

        closeness = degree / 25

        component = 1

        return {

            **gene_context,

            "interaction_score": interaction_score,

            "approved": approved,

            "immunotherapy": immunotherapy,

            "anti_neoplastic": anti_neoplastic,

            "pathway_count": pathway_count,

            "drug_count": drug_count,

            "degree": degree,

            "graph_degree": graph_degree,

            "pagerank": pagerank,

            "betweenness": betweenness,

            "closeness": closeness,

            "component": component

        }