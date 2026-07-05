import time

from app.ai_platform.knowledge_bus import AIKnowledgeBus


class AIPlatformTool:

    def __init__(self):
        self.bus = AIKnowledgeBus()

    def predict(self, context):

        start = time.perf_counter()
        context.recommendations = self.bus.predict(context)
        print(f"AI Predict      : {time.perf_counter() - start:.3f} sec")

        start = time.perf_counter()
        context.recommendations = self.bus.rank(context)
        print(f"AI Rank         : {time.perf_counter() - start:.3f} sec")

        start = time.perf_counter()
        context.ai_confidence = self.bus.confidence_score(context)
        print(f"AI Confidence   : {time.perf_counter() - start:.3f} sec")

        start = time.perf_counter()
        context.embeddings = self.bus.embed(context)
        print(f"AI Embeddings   : {time.perf_counter() - start:.3f} sec")

        return context