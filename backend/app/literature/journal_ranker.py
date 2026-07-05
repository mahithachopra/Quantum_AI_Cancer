class JournalRanker:

    def __init__(self):

        self.rankings = {

            "Nature": 1.00,
            "Nature Medicine": 0.99,
            "Nature Cancer": 0.99,
            "Cancer Discovery": 0.98,
            "Lancet Oncology": 0.98,
            "Journal of Clinical Oncology": 0.97,
            "Clinical Cancer Research": 0.96,
            "Cancer Research": 0.95,
            "Annals of Oncology": 0.95,
            "JNCI": 0.94,
            "Molecular Cancer": 0.94,
            "Oncogene": 0.92,
            "Molecular Oncology": 0.90,
            "Cancers": 0.85,
            "Frontiers in Oncology": 0.82,
            "Scientific Reports": 0.80,
            "PLOS ONE": 0.75
        }

    def score(self, journal: str):

        if not journal:
            return 0.60

        for name, score in self.rankings.items():

            if name.lower() in journal.lower():

                return score

        return 0.70