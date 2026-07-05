from pathlib import Path
import pandas as pd


class FeatureBuilder:

    def __init__(self):

        self.df = pd.read_csv(
            Path("app/ml/output/ml_training_dataset_graph.csv")
        )

    def get_features(self, gene, drug):

        row = self.df[
            (self.df["gene_symbol"] == gene)
            &
            (self.df["drug_name"] == drug)
        ]

        if row.empty:
            return None

        X = row[
    [
        "interaction_score",
        "approved",
        "immunotherapy",
        "anti_neoplastic",
        "mutation_count",
        "pathway_count",
        "drug_count",
        "degree",
    ]
]

        X = X.replace({True: 1, False: 0}).astype(float)

        X = X.astype(float)

        return X.iloc[0]


if __name__ == "__main__":

    fb = FeatureBuilder()

    x = fb.get_features(
        "DPH1",
        "BMS-536924"
    )

    print(x)