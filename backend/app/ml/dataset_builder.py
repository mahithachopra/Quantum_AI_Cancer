from app.ml.feature_engineering import FeatureEngineer
from app.ml.graph_features import merge_graph_features
from app.ml.config import OUTPUT_DIR


def main():

    fe = FeatureEngineer()

    print("Loading mutation features...")
    mutations = fe.mutation_counts()

    print("Loading pathway features...")
    pathways = fe.pathway_counts()

    print("Loading drug features...")
    drugs = fe.drug_counts()

    print("Loading graph degree...")
    degree = fe.degree_features()

    dataset = merge_graph_features(
        mutations,
        pathways,
        drugs,
        degree
    )

    output = OUTPUT_DIR / "training_dataset.csv"

    dataset.to_csv(
        output,
        index=False
    )

    print(f"\nDataset saved to {output}")
    print(dataset.head())

    fe.close()


if __name__ == "__main__":
    main()