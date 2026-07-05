from app.explainability.models import Explanation
from app.explainability.confidence_explainer import ConfidenceExplainer
from app.explainability.evidence_explainer import EvidenceExplainer
from app.explainability.pathway_explainer import PathwayExplainer
from app.explainability.graph_explainer import GraphExplainer


class RecommendationExplainer:

    def __init__(self):

        self.confidence = ConfidenceExplainer()

        self.evidence = EvidenceExplainer()

        self.pathways = PathwayExplainer()

        self.graph = GraphExplainer()

    def explain(self, recommendation, context):

        evidence = self.evidence.explain(
            recommendation,
            context
        )

        pathways = self.pathways.explain(
            recommendation,
            context
        )

        graph = self.graph.explain(
            recommendation,
            context
        )

        reasoning = [

            f"{recommendation.gene} mutation detected.",

            f"{recommendation.drug} recommended by fusion engine.",

            f"{evidence['civic_count']} CIViC evidence records.",

            f"{evidence['paper_count']} literature publications.",

            f"{evidence['trial_count']} clinical trials.",

            f"{pathways['count']} enriched pathways.",

            f"{graph['connections']} graph neighbours."

        ]

        return Explanation(

            gene=recommendation.gene,

            drug=recommendation.drug,

            confidence=recommendation.confidence,

            confidence_level=self.confidence.explain(
                recommendation.confidence
            ),

            reasoning=reasoning,

            ai_score=recommendation.ai_score,

            graph_score=recommendation.graph_score,

            pathway_score=recommendation.pathway_score,

            civic_score=recommendation.civic_score,

            literature_score=recommendation.literature_score,

            trial_score=recommendation.trial_score,

            graph_connections=graph["connections"],

            pathway_count=pathways["count"],

            literature_count=evidence["paper_count"],

            trial_count=evidence["trial_count"],

            civic_count=evidence["civic_count"],

             evidence={
        "top_civic": evidence["top_civic"],
        "top_papers": evidence["top_papers"],
        "top_trials": evidence["top_trials"]
    }

)

        