from app.literature.europe_pmc import EuropePMC
from app.literature.models import Paper
from app.literature.keyword_extractor import KeywordExtractor
from concurrent.futures import ThreadPoolExecutor


class LiteratureService:

    def __init__(self):

        self.client = EuropePMC()
        self.keyword_extractor = KeywordExtractor()

    def build_query(self, recommendation):
        """
        Build an intelligent Europe PMC query.
        """

        gene = recommendation.get("gene", "")
        drug = recommendation.get("drug", "")
        disease = recommendation.get("disease", "Cancer")

        return (
            f'"{gene}" '
            f'AND "{drug}" '
            f'AND "{disease}"'
        )

    def retrieve(
        self,
        graph_analysis,
        recommendations,
        pathways
    ):

        papers = []
        seen = set()

        # Search only for the top recommendations
        with ThreadPoolExecutor(max_workers=5) as executor:

            futures = {}

            for recommendation in recommendations[:5]:

                query = self.build_query(recommendation)

                future = executor.submit(
                    self.client.search,
                    query
                )

                futures[future] = recommendation

            for future, recommendation in futures.items():

                try:
                    results = future.result()

                except Exception:
                    continue

                for item in results:

                    title = item.get("title", "").strip()
                    doi = item.get("doi", "").strip()

                    key = (
                        title.lower(),
                        doi.lower()
                    )

                    if key in seen:
                        continue

                    seen.add(key)

                    paper = Paper(
                        title=title,
                        journal=item.get("journalTitle", ""),
                        year=int(item.get("pubYear", 0) or 0),
                        authors=item.get("authorString", ""),
                        abstract=item.get("abstractText", ""),
                        pmid=item.get("pmid", ""),
                        doi=doi,
                        url=item.get("fullTextUrl", ""),
                        gene=recommendation.get("gene", ""),
                        drug=recommendation.get("drug", ""),
                        disease=recommendation.get("disease", "Cancer"),
                        publication_type=item.get("pubType", ""),
                        source="Europe PMC",
                        keywords=[]
                    )

                    paper.keywords = (
                        self.keyword_extractor.extract(
                            paper
                        )
                    )

                    papers.append(paper)
        return papers
                