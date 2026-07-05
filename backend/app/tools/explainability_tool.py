from app.explainability.explanation_engine import ExplanationEngine


class ExplainabilityTool:

    def __init__(self):

        self.engine = ExplanationEngine()

    def explain(self, context):

        return self.engine.explain(context)