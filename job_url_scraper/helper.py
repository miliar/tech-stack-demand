from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from retry import retry
from kafka import KafkaProducer
from config import KAFKA


@retry(tries=5, delay=30)
def get_producer():
    return KafkaProducer(bootstrap_servers=[KAFKA],
                         value_serializer=lambda x: x.encode('utf-8'),
                         key_serializer=lambda x: x.encode('utf-8') if x else x
                         )


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
