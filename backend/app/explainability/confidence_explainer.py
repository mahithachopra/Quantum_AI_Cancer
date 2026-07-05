class ConfidenceExplainer:

    def explain(self, score):

        if score >= 0.90:
            return "Very High"

        if score >= 0.75:
            return "High"

        if score >= 0.60:
            return "Moderate"

        if score >= 0.40:
            return "Low"

        return "Very Low"