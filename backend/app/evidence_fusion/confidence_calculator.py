class ConfidenceCalculator:

    WEIGHTS = {

        "ai": 0.35,
        "civic": 0.20,
        "literature": 0.15,
        "trial": 0.15,
        "graph": 0.10,
        "pathway": 0.05

    }

    @staticmethod
    def _safe(value):

        if value is None:
            return 0.0

        return float(value)

    def calculate(

        self,

        ai,

        civic,

        literature,

        trial,

        graph,

        pathway

    ):

        ai = self._safe(ai)
        civic = self._safe(civic)
        literature = self._safe(literature)
        trial = self._safe(trial)
        graph = self._safe(graph)
        pathway = self._safe(pathway)

        return (

            ai * self.WEIGHTS["ai"]

            + civic * self.WEIGHTS["civic"]

            + literature * self.WEIGHTS["literature"]

            + trial * self.WEIGHTS["trial"]

            + graph * self.WEIGHTS["graph"]

            + pathway * self.WEIGHTS["pathway"]

        )