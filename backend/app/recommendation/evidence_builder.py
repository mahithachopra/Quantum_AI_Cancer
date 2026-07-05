class EvidenceBuilder:

    def build(self, recommendation):

        evidence = []

        if recommendation["approved"]:
            evidence.append("FDA Approved")

        if recommendation["anti_neoplastic"]:
            evidence.append("Antineoplastic Agent")

        if recommendation["immunotherapy"]:
            evidence.append("Immunotherapy")

        evidence.append(
            f"Interaction Score: {recommendation['interaction_score']:.3f}"
        )

        return evidence