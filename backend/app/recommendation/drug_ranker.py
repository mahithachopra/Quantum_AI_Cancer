import pandas as pd


class DrugRanker:

    def rank(self, candidates):

        df = pd.DataFrame(candidates)

        if df.empty:
            return []

        # Remove rows without drug names
        df = df[df["drug_name"].notna()]

        # Fill missing values
        df["interaction_score"] = (
            df["interaction_score"]
            .fillna(0)
            .astype(float)
        )

        df["approved"] = (
            df["approved"]
            .fillna(False)
            .astype(bool)
            .astype(int)
        )

        df["anti_neoplastic"] = (
            df["anti_neoplastic"]
            .fillna(False)
            .astype(bool)
            .astype(int)
        )

        df["immunotherapy"] = (
            df["immunotherapy"]
            .fillna(False)
            .astype(bool)
            .astype(int)
        )

        df["score"] = (
            0.70 * df["interaction_score"]
            + 0.20 * df["approved"]
            + 0.10 * df["anti_neoplastic"]
        )

        df = df.sort_values(
            "score",
            ascending=False
        )

        return df.to_dict("records")