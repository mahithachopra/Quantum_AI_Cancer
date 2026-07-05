import pandas as pd


def merge_graph_features(
    mutation_df,
    pathway_df,
    drug_df,
    degree_df,
):
    """
    Merge all engineered graph features into a single dataset.
    """

    df = mutation_df.merge(
        pathway_df,
        on="gene_symbol",
        how="left"
    )

    df = df.merge(
        drug_df,
        on="gene_symbol",
        how="left"
    )

    df = df.merge(
        degree_df,
        on="gene_symbol",
        how="left"
    )

    df.fillna(0, inplace=True)

    return df