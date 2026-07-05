from sqlalchemy import text


class PostgresRepository:

    def __init__(self, db):
        self.db = db

    def execute(self, query: str, params=None):
        return self.db.execute(text(query), params or {})

    def fetch_all(self, query: str, params=None):
        result = self.execute(query, params)
        return result.mappings().all()

    def fetch_one(self, query: str, params=None):
        result = self.execute(query, params)
        return result.mappings().first()