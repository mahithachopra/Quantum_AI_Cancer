class EvidenceRanker:

    LEVEL_SCORE = {
        "A": 1.00,
        "B": 0.90,
        "C": 0.75,
        "D": 0.60,
        "E": 0.40
    }

    def rank(self, records):

        ranked = []

        for record in records:

            score = self.LEVEL_SCORE.get(
                record["evidence_level"],
                0.2
            )

            record["score"] = score

            ranked.append(record)

        ranked.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranked