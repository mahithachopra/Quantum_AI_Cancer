import requests


class EuropePMC:

    BASE = (
        "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
    )

    def search(self, query, limit=10):

        params = {

            "query": query,

            "format": "json",

            "pageSize": limit

        }

        r = requests.get(
            self.BASE,
            params=params,
            timeout=30
        )

        r.raise_for_status()

        data = r.json()

        return data.get("resultList", {}).get("result", [])