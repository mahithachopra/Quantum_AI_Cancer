from app.explainability.recommendation_explainer import RecommendationExplainer


class ExplanationEngine:

    def __init__(self):
        self.recommender = RecommendationExplainer()

    def explain(self, context):

        explanations = []

        # Priority 1: fused recommendations
        if hasattr(context, "fused_recommendations") and context.fused_recommendations:
            recommendations = context.fused_recommendations

        # Priority 2: legacy fusion results
        elif hasattr(context, "fusion_results") and context.fusion_results:
            recommendations = context.fusion_results

        # Priority 3: raw AI recommendations
        else:
            recommendations = context.recommendations

        print(f"Generating explanations for {len(recommendations)} recommendations")

        for recommendation in recommendations:

            explanation = self.recommender.explain(
                recommendation,
                context
            )

            explanations.append(explanation)

        return explanations