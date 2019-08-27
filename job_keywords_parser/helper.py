from time import sleep
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import NoBrokersAvailable


def get_producer():
    while True:
        try:
            producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
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
                bootstrap_servers=['kafka:9092'],
                auto_offset_reset='earliest',
                group_id='parsers',
                value_deserializer=lambda x: x.decode('utf-8'),
                key_deserializer=lambda x: x.decode('utf-8')
            )
            return consumer
        except NoBrokersAvailable:
            print('No Broker, reconnecting..')
            sleep(15)
            continue
