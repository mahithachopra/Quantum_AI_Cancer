from sqlalchemy import text


class MutationRepository:

    def __init__(self, db):
        self.db = db

    def get_by_id(self, mutation_id: int):

        query = text("""
            SELECT *
            FROM mutations
            WHERE mutation_id = :mutation_id
            LIMIT 1
        """)

        result = self.db.execute(
            query,
            {"mutation_id": mutation_id}
        )

        return result.mappings().first()

    def search_gene(self, gene_symbol: str, limit: int = 100):

        query = text("""
            SELECT *
            FROM mutations
            WHERE gene_symbol = :gene_symbol
            LIMIT :limit
        """)

        result = self.db.execute(
            query,
            {
                "gene_symbol": gene_symbol,
                "limit": limit
            }
        )

        return result.mappings().all()

    def list_mutations(self, limit: int = 100):

        query = text("""
            SELECT *
            FROM mutations
            LIMIT :limit
        """)

        result = self.db.execute(
            query,
            {"limit": limit}
        )

        return result.mappings().all()