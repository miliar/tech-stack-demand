from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from retry import retry
from time import sleep
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import NoBrokersAvailable


def get_producer():
    while True:
        try:
            producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                                     value_serializer=lambda x: x.encode(
                                         'utf-8'),
                                     key_serializer=lambda x: x.encode('utf-8') if x else x)
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
                group_id='scrapers',
                value_deserializer=lambda x: x.decode('utf-8')
            )
            return consumer
        except NoBrokersAvailable:
            print('No Broker, reconnecting..')
            sleep(15)
            continue


@retry(tries=3, delay=5)
def get_html(url):
    with closing(get(url, stream=True)) as response:
        if _is_good_response(response):
            return BeautifulSoup(response.content, 'html.parser')
    raise RequestException(f'Error getting {url}')


def _is_good_response(response):
    content_type = response.headers['Content-Type'].lower()
    return (response.status_code == 200 and
            content_type is not None and
            content_type.find('html') > -1)
