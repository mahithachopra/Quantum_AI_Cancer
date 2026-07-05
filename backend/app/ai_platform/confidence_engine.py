class ConfidenceEngine:

    def compute(self, context):

        scores = []

        for r in context.recommendations:

            scores.append(

                r.get(
                    "ai_probability",
                    0
                )

            )

        if not scores:

            return 0

        return sum(scores) / len(scores)