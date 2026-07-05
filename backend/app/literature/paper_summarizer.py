class PaperSummarizer:

    def summarize(self, paper):

        summary = (
            f"{paper.drug} has been investigated for "
            f"{paper.gene}-associated cancers. "
            f"Published in {paper.journal} ({paper.year})."
        )

        return {

            "title": paper.title,

            "journal": paper.journal,

            "year": paper.year,

            "gene": paper.gene,

            "drug": paper.drug,

            "authors": paper.authors,

            "doi": paper.doi,

            "pmid": paper.pmid,

            "url": paper.url,

            "score": paper.score,

            "summary": summary

        }