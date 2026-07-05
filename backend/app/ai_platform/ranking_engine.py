class RankingEngine:

    def rank(self, context):

        context.recommendations.sort(

            key=lambda x: x.get(
                "final_score",
                0.0
            ),

            reverse=True

        )

        return context.recommendations