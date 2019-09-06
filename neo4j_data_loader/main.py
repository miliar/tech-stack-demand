from helper import get_consumer, get_producer
from config import KAFKA_ERROR_TOPIC, KAFKA_INPUT_TOPIC
from neo4j_data_loader import Neo4jDataLoader
import traceback

if __name__ == '__main__':
    consumer = get_consumer(KAFKA_INPUT_TOPIC)
    producer = get_producer()
    loader = Neo4jDataLoader()

    for keywords in consumer:
        try:
            loader.insert_data(company=keywords.key, tags=keywords.value)
        except Exception as e:
            tb = traceback.format_exc()
            producer.send(KAFKA_ERROR_TOPIC,
                          value=f'FOR: {keywords} \nERROR: {e}\n{tb}\n',
                          key='Neo4jDataLoader')
            continue
