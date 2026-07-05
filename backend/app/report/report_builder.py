from app.report.models import Report


class ReportBuilder:

    def build(self, context):

        return Report(

            patient_id=context.patient_id,

            genes=context.genes,

            recommendations=context.fused_recommendations,

            evidence=context.evidence,

            literature=context.literature,

            clinical_trials=context.clinical_trials,

            pathways=context.pathway_analysis,

            graph=context.graph_analysis,

            explanations=context.explanations,

            metadata=context.metadata

        )