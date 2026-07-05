class MutationAnalysisService:

    def analyze(self, genes):

        results = []

        for gene in genes:

            results.append(

                {

                    "gene": gene,

                    "driver": True,

                    "clinical_significance": "High"

                }

            )

        return results