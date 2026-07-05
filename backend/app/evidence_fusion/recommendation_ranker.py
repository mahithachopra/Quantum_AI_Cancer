class RecommendationRanker:

    def rank(

        self,

        recommendations

    ):

        recommendations.sort(

            key=lambda x:x.confidence,

            reverse=True

        )

        return recommendations