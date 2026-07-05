from app.ai_platform.models import PatientFeatures


class FeatureEngineering:

    def build(self, context):

        return PatientFeatures(

            genes=context.genes,

            graph_features=context.graph_analysis,

            pathway_features=context.pathway_analysis,

            evidence_features=context.evidence,

            literature_features=context.literature,

            trial_features=context.clinical_trials

        )