import requests
from time import sleep
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable


class Paginator:
    def __init__(self):
        self.page_nr = 1
        self.page = requests.get(self.url()).json()
        self.producer = self.get_producer()

    def url(self):
        raise NotImplementedError("Must override url()")

    def get_producer(self):
        while True:
            try:
                producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                                         value_serializer=lambda x: x.encode('utf-8'))
                return producer
            except NoBrokersAvailable:
                print('No Broker, reconnecting..')
                sleep(15)
                continue

    def send(self, topic):
        while True:
            for item in self.items():
                self.producer.send(topic, value=item)
                print(f'send {item}')
                sleep(2) # To be removed
            if self.page['has_more']:
                self.next_page()
            else:
                break

    def items(self):
        raise NotImplementedError("Must override item()")

    def next_page(self):
        self.page_nr += 1
        self.page = requests.get(self.url()).json()
