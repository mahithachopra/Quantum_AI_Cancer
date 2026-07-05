from datetime import datetime


class ReportTool:

    def generate(self, context):

        return {

            "generated_at":

                datetime.now().isoformat(),

            "genes":

                context["genes"],

            "mutations":

                context["mutation_analysis"],

            "pathways":

                context["pathways"],

            "recommendations":

                context["drug_candidates"],

            "quantum":

                context["quantum"],

            "summary":

                context["summary"]

        }