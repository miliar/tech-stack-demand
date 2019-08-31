from time import sleep
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import NoBrokersAvailable
from config import KAFKA, KAFKA_CONSUMER_GROUP


def get_producer():
    while True:
        try:
            producer = KafkaProducer(bootstrap_servers=[KAFKA],
                                     value_serializer=lambda x: x.encode(
                                         'utf-8'),
                                     key_serializer=lambda x: x.encode('utf-8'))
            return producer
        except NoBrokersAvailable:
            print('No Broker, reconnecting..')
            sleep(15)
            continue


def get_consumer(topic):
    while True:
        try:
            consumer = KafkaConsumer(
                topic,
                bootstrap_servers=[KAFKA],
                auto_offset_reset='earliest',
                group_id=KAFKA_CONSUMER_GROUP,
                value_deserializer=lambda x: x.decode('utf-8'),
                key_deserializer=lambda x: x.decode('utf-8')
            )
            return consumer
        except NoBrokersAvailable:
            print('No Broker, reconnecting..')
            sleep(15)
            continue
