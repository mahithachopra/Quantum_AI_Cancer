class EvidenceExplainer:

    def explain(self, recommendation, context):

        gene = recommendation.gene
        drug = recommendation.drug

        civic = context.evidence.get(gene, [])

        papers = [
            p for p in context.literature
            if p["drug"].upper() == drug.upper()
        ]

        trials = [
            t for t in context.clinical_trials
            if t.drug.upper() == drug.upper()
        ]

        return {

            "civic_count": len(civic),
            "paper_count": len(papers),
            "trial_count": len(trials),

            # keep only a few examples
            "top_civic": civic[:3],
            "top_papers": papers[:3],
            "top_trials": trials[:3]

        }