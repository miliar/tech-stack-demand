from neo4j import GraphDatabase, basic_auth
from neo4j.exceptions import ServiceUnavailable
from time import sleep
from helper import get_consumer


class Neo4jDataLoader:
    def __init__(self):
        self.driver = self._get_driver()

    def _get_driver(self):
        while True:
            try:
                driver = GraphDatabase.driver(
                    "bolt://neo4j", auth=basic_auth("neo4j", "password"))
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


if __name__ == '__main__':
    consumer = get_consumer('job_keywords')
    loader = Neo4jDataLoader()

    for keywords in consumer:
        loader.insert_data(company=keywords.key, tags=keywords.value)
        print(f'Insert Company: {keywords.key} --> Tags: {keywords.value}', flush=True)
