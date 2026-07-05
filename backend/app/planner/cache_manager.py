from app.memory.memory_keys import MemoryKeys


class CacheManager:

    CACHE = {

        "Mutation Agent": MemoryKeys.MUTATION,

        "Graph Agent": MemoryKeys.GRAPH,

        "Pathway Agent": MemoryKeys.PATHWAY,

        "Drug Agent": MemoryKeys.RECOMMENDATIONS,

        "Evidence Agent": MemoryKeys.EVIDENCE,

        "Literature Agent": MemoryKeys.LITERATURE,

        "Clinical Trial Agent": MemoryKeys.CLINICAL_TRIALS,

        "Evidence Fusion Agent": MemoryKeys.FUSION,

        "Explainability Agent": MemoryKeys.EXPLAINABILITY,

        "Report Agent": MemoryKeys.REPORT,

    }

    def has_result(

        self,

        context,

        agent_name

    ):

        key = self.CACHE.get(agent_name)

        if key is None:

            return False

        return context.memory.memory.has(key)