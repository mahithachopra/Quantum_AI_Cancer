class DiseaseMatcher:

    def score(self, disease, paper):

        disease = (disease or "").lower()

        text = (
            (paper.title or "")
            + " "
            + (paper.abstract or "")
        ).lower()

        if disease == "":
            return 0.50

        if disease in text:
            return 1.0

        keywords = {

            "lung cancer": [
                "nsclc",
                "non-small cell lung",
                "lung adenocarcinoma"
            ],

            "breast cancer": [
                "breast carcinoma",
                "brca"
            ],

            "glioblastoma": [
                "glioblastoma",
                "gbm"
            ]
        }

        for key, values in keywords.items():

            if disease == key:

                for word in values:

                    if word in text:

                        return 0.90

        return 0.20