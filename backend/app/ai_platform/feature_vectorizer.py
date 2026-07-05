import pandas as pd

import numpy as np
class FeatureVectorizer:

    FEATURES = [
        "interaction_score",
        "approved",
        "immunotherapy",
        "anti_neoplastic",
        "mutation_count",
        "pathway_count",
        "drug_count",
        "degree",
        "graph_degree",
        "pagerank",
        "betweenness",
        "closeness",
        "component"
    ]

    def vectorize(self, features):

        graph = features.graph_features

        if not graph:

            return np.zeros(
                (1, len(self.FEATURES)),
                dtype=np.float32
            )

        #
        # Aggregate graph metrics
        #

        interaction_score = 0
        approved = 0
        immunotherapy = 0
        anti_neoplastic = 0
        pathway_count = 0
        drug_count = 0
        degree = 0
        graph_degree = 0
        pagerank = 0
        betweenness = 0
        closeness = 0
        component = 1

        n = len(graph)

        for gene_data in graph.values():

            interaction_score += gene_data["interaction_score"]

            approved += gene_data["approved"]

            immunotherapy += gene_data["immunotherapy"]

            anti_neoplastic += gene_data["anti_neoplastic"]

            pathway_count += gene_data["pathway_count"]

            drug_count += gene_data["drug_count"]

            degree += gene_data["degree"]

            graph_degree += gene_data["graph_degree"]

            pagerank += gene_data["pagerank"]

            betweenness += gene_data["betweenness"]

            closeness += gene_data["closeness"]

        vector = [

            interaction_score / n,

            approved / n,

            immunotherapy / n,

            anti_neoplastic / n,

            len(features.genes),

            pathway_count / n,

            drug_count / n,

            degree / n,

            graph_degree / n,

            pagerank / n,

            betweenness / n,

            closeness / n,

            component

        ]

        return pd.DataFrame(
    [vector],
    columns=self.FEATURES
)