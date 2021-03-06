from kafka import KafkaProducer, KafkaConsumer
from retry import retry
from config import KAFKA_CONSUMER_GROUP, KAFKA


@retry(tries=5, delay=30)
def get_producer():
    return KafkaProducer(bootstrap_servers=[KAFKA],
                         value_serializer=lambda x: x.encode('utf-8'),
                         key_serializer=lambda x: x.encode('utf-8')
                         )


@retry(tries=5, delay=30)
def get_consumer(topic):
    return KafkaConsumer(
        topic,
        bootstrap_servers=[KAFKA],
        group_id=KAFKA_CONSUMER_GROUP,
        value_deserializer=lambda x: x.decode('utf-8'),
        key_deserializer=lambda x: x.decode('utf-8')
    )
