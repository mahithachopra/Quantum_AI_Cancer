from sqlalchemy import text

from app.core.postgres import SessionLocal


class CandidateGenerator:

    def __init__(self):
        self.db = SessionLocal()

    def get_candidate_drugs(self, genes):

        query = text("""
SELECT DISTINCT
    gene_symbol,
    drug_name,
    interaction_score,
    approved,
    immunotherapy,
    anti_neoplastic
FROM gene_drug
WHERE gene_symbol = ANY(:genes)
  AND drug_name IS NOT NULL
  AND interaction_score IS NOT NULL
ORDER BY interaction_score DESC
""")

        rows = self.db.execute(
            query,
            {"genes": genes}
        ).fetchall()

        return [
            dict(r._mapping)
            for r in rows
        ]

    def close(self):
        self.db.close()


if __name__ == "__main__":

    cg = CandidateGenerator()

    result = cg.get_candidate_drugs(
        [
            "EGFR",
            "TP53",
            "PIK3CA"
        ]
    )

    print(result[:5])

    cg.close()