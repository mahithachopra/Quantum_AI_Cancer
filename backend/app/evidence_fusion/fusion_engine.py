from app.evidence_fusion.models import FusionRecommendation
from app.evidence_fusion.confidence_calculator import ConfidenceCalculator


class FusionEngine:

    def __init__(self):

        self.calculator = ConfidenceCalculator()

    def fuse(

        self,

        context

    ):

        recommendations=[]

        for drug in context.recommendations:

            gene=drug["gene"]

            ai = drug.get(
    "final_score",
    drug.get(
        "ai_probability",
        0.0
    )
)

            civic=self._civic_score(

                context,

                gene

            )

            literature=self._literature_score(

                context,

                gene

            )

            trials=self._trial_score(

                context,

                gene

            )

            graph=self._graph_score(

                context,

                gene

            )

            pathway=self._pathway_score(

                context,

                gene

            )

            confidence=self.calculator.calculate(

                ai,

                civic,

                literature,

                trials,

                graph,

                pathway

            )

            recommendations.append(

                FusionRecommendation(

                    gene=gene,

                    drug=drug["drug"],

                    ai_score=ai,

                    civic_score=civic,

                    literature_score=literature,

                    trial_score=trials,

                    graph_score=graph,

                    pathway_score=pathway,

                    confidence=confidence

                )

            )

        return recommendations
    def _civic_score(self, context, gene):

        if gene not in context.evidence:

            return 0.0

        records=context.evidence[gene]

        if len(records)==0:

            return 0.0

        levels={

            "A":1.0,

            "B":0.9,

            "C":0.8,

            "D":0.7,

            "E":0.6

        }

        return max(

            levels.get(

                r["evidence_level"],

                0.5

            )

            for r in records

        )


    def _literature_score(self, context, gene):

        papers=[

            p for p in context.literature

            if p["gene"]==gene

        ]

        return min(

            len(papers)/20,

            1.0

        )


    def _trial_score(self, context, gene):

        trials=[

            t for t in context.clinical_trials

            if t.gene==gene

        ] if hasattr(context, "clinical_trials") else []

        return min(

            len(trials)/10,

            1.0

        )


    def _graph_score(self, context, gene):

        graph=context.graph_analysis.get(

            gene,

            {}

        )

        return min(

            len(

                graph.get(

                    "pathways",

                    []

                )

            )/50,

            1.0

        )


    def _pathway_score(self, context, gene):

        pathways=[

            p for p in context.pathway_analysis

            if gene in p["genes"]

        ]

        return min(

            len(pathways)/20,

            1.0

        )