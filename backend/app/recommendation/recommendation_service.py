from app.recommendation.candidate_generator import CandidateGenerator
from app.recommendation.evidence_builder import EvidenceBuilder
from app.recommendation.drug_ranker import DrugRanker


class RecommendationService:

    def __init__(self):

        self.generator = CandidateGenerator()
        self.evidence = EvidenceBuilder()
        self.ranker = DrugRanker()

    def recommend(self, genes, top_k=10):

        # -------------------------------------------------
        # Step 1: Candidate Retrieval
        # -------------------------------------------------

        candidates = self.generator.get_candidate_drugs(
            genes
        )

        if not candidates:
            return []

        # -------------------------------------------------
        # Step 2: Biological Ranking
        # -------------------------------------------------

        ranked = self.ranker.rank(candidates)

        recommendations = []

        for drug in ranked:

            recommendations.append(

                {

                    "gene": drug["gene_symbol"],

                    "drug": drug["drug_name"],

                    # Biological score only
                    "interaction_score": round(
                        float(drug["interaction_score"]),
                        4
                    ),

                    # AI Platform will populate these
                    "rf_probability": None,

                    "xgb_probability": None,

                    "lr_probability": None,

                    "ai_probability": None,

                    "final_score": None,

                    # Drug metadata
                    "approved": bool(
                        drug["approved"]
                    ),

                    "immunotherapy": bool(
                        drug["immunotherapy"]
                    ),

                    "anti_neoplastic": bool(
                        drug["anti_neoplastic"]
                    ),

                    # Evidence
                    "evidence": self.evidence.build(
                        drug
                    )

                }

            )

        # Keep only top biological candidates
        recommendations.sort(

            key=lambda x: x["interaction_score"],

            reverse=True

        )

        return recommendations[:top_k]


if __name__ == "__main__":

    service = RecommendationService()

    recommendations = service.recommend(

        [

            "EGFR",

            "TP53",

            "PIK3CA"

        ]

    )

    from pprint import pprint

    pprint(recommendations)