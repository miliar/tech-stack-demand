from neo4j import GraphDatabase, basic_auth
from retry import retry
from config import (GRAPH_DATABASE_URI,
                    GRAPH_DATABASE_USER,
                    GRAPH_DATABASE_PASSWORD)


class Neo4jDataLoader:
    def __init__(self):
        self.driver = self._get_driver()

    @retry(tries=5, delay=30)
    def _get_driver(self):
        return GraphDatabase.driver(GRAPH_DATABASE_URI,
                                    auth=basic_auth(
                                        GRAPH_DATABASE_USER,
                                        GRAPH_DATABASE_PASSWORD
                                    )
                                    )

    def insert_data(self, company, tags):
        data = [[company, tag] for tag in tags.split()]
        with self.driver.session() as session:
            session.run('UNWIND {pairs} as pair '
                        'MERGE (c:Company {name:pair[0]}) '
                        'MERGE (t:Tag {name:pair[1]}) '
                        'MERGE (c)-[:USES]-(t);',
                        parameters={"pairs": data}
                        )
