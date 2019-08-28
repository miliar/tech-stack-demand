from time import sleep
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable


def get_consumer(topic):
    while True:
        try:
            consumer = KafkaConsumer(
                topic,
                bootstrap_servers=['kafka:9092'],
                auto_offset_reset='earliest',
                group_id='loaders',
                value_deserializer=lambda x: x.decode('utf-8'),
                key_deserializer=lambda x: x.decode('utf-8')
            )
            return consumer
        except NoBrokersAvailable:
            print('No Broker, reconnecting..')
            sleep(15)
            continue
