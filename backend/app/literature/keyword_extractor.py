import re


class KeywordExtractor:

    def extract(self, paper):

        text = (
            f"{paper.title} "
            f"{paper.abstract}"
        ).lower()

        words = re.findall(
            r"[a-zA-Z0-9\-]+",
            text
        )

        stopwords = {
            "the", "and", "of", "for",
            "with", "from", "into",
            "that", "this", "their",
            "have", "were", "been",
            "using", "study", "analysis",
            "patient", "patients", "between",
            "during", "after", "before",
            "into", "onto", "also"
        }

        keywords = []

        for word in words:

            if len(word) < 4:
                continue

            if word in stopwords:
                continue

            if word not in keywords:
                keywords.append(word)

        return keywords[:20]