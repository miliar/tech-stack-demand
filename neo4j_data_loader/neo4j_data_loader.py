from neo4j import GraphDatabase, basic_auth
from neo4j.exceptions import ServiceUnavailable
from time import sleep
from config import GRAPH_DATABASE_URI, GRAPH_DATABASE_USER, GRAPH_DATABASE_PASSWORD


class Neo4jDataLoader:
    def __init__(self):
        self.driver = self._get_driver()

    def _get_driver(self):
        while True:
            try:
                driver = GraphDatabase.driver(
                    GRAPH_DATABASE_URI, auth=basic_auth(GRAPH_DATABASE_USER, GRAPH_DATABASE_PASSWORD))
                return driver
            except ServiceUnavailable:
                print('Can not connect to neo4j, reconnecting..')
                sleep(15)
                continue

    def insert_data(self, company, tags):
        data = [[company, tag] for tag in tags.split()]
        with self.driver.session() as session:
            session.run('UNWIND {pairs} as pair '
                        'MERGE (c:Company {name:pair[0]}) '
                        'MERGE (t:Tag {name:pair[1]}) '
                        'MERGE (c)-[:USES]-(t);', parameters={"pairs": data})
