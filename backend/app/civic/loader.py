from pathlib import Path
import pandas as pd


class CivicLoader:

    def __init__(self, data_dir="datasets/civic"):

        self.data_dir = Path(data_dir)

    def load(self):

        return {

            "features":
                pd.read_csv(
                    self.data_dir /
                    "nightly-FeatureSummaries.tsv",
                    sep="\t",
                    low_memory=False
                ),

            "variants":
                pd.read_csv(
                    self.data_dir /
                    "nightly-VariantSummaries.tsv",
                    sep="\t",
                    low_memory=False
                ),

            "evidence":
                pd.read_csv(
                    self.data_dir /
                    "nightly-AcceptedClinicalEvidenceSummaries.tsv",
                    sep="\t",
                    low_memory=False
                ),

            "assertions":
                pd.read_csv(
                    self.data_dir /
                    "nightly-AcceptedAssertionSummaries.tsv",
                    sep="\t",
                    low_memory=False
                )
        }