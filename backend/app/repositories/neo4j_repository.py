class Neo4jRepository:

    def __init__(self, session):
        self.session = session

    def run(self, query, parameters=None):
        result = self.session.run(query, parameters or {})
        return [record.data() for record in result]