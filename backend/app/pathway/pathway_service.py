from collections import Counter


class PathwayService:

    def analyze(
        self,
        graph_analysis: dict
    ) -> list:

        pathway_counter = Counter()

        pathway_to_gene = {}

        # Collect pathway occurrences
        for gene, info in graph_analysis.items():

            pathways = info.get("pathways", [])

            for pathway in pathways:

                pathway_counter[pathway] += 1

                pathway_to_gene.setdefault(
                    pathway,
                    []
                ).append(gene)

        ranked = []

        # Compute pathway importance using graph metrics
        for pathway, count in pathway_counter.items():

            importance = 0.0

            for gene in pathway_to_gene[pathway]:

                graph = graph_analysis.get(gene, {})

                importance += (
                    graph.get("pagerank", 0.0)
                    + graph.get("betweenness", 0.0)
                    + graph.get("closeness", 0.0)
                )

            importance = round(importance, 3)

            ranked.append(
                {
                    "pathway": pathway,
                    "gene_count": count,
                    "genes": pathway_to_gene[pathway],
                    "importance": importance
                }
            )

        ranked.sort(
            key=lambda x: x["importance"],
            reverse=True
        )

        return ranked