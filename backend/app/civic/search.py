class CivicSearch:

    def __init__(self, data):

        self.data = data

    def search_gene(self, gene):

        evidence = self.data["evidence"]

        return evidence[
            evidence["molecular_profile"]
            .str.contains(
                gene,
                case=False,
                na=False
            )
        ]

    def search_assertions(self, gene):

        assertions = self.data["assertions"]

        return assertions[
            assertions["molecular_profile"]
            .str.contains(
                gene,
                case=False,
                na=False
            )
        ]