import requests


class ClinicalTrialsClient:

    BASE = "https://clinicaltrials.gov/api/v2/studies"

    def search(self, gene, drug, limit=10):

        query = f"{gene} {drug}"

        params = {
            "query.term": query,
            "pageSize": limit
        }

        response = requests.get(
            self.BASE,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return data.get("studies", [])