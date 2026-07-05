class PaperFilter:

    def unique(self, papers):

        seen = set()

        filtered = []

        for paper in papers:

            key = (
                paper.title.lower(),
                paper.doi
            )

            if key in seen:
                continue

            seen.add(key)

            filtered.append(paper)

        return filtered