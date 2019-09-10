import json
from kafka import KafkaProducer
from retry import retry
from config import KAFKA


@retry(tries=5, delay=30)
def get_producer():
    return KafkaProducer(bootstrap_servers=[KAFKA],
                         value_serializer=lambda x: json.dumps(
                             x).encode('ascii')
                         )
