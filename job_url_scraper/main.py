from helper import get_producer, get_consumer
from config import KAFKA_ERROR_TOPIC, KAFKA_OUTPUT_TOPIC, KAFKA_INPUT_TOPIC
from job_url_scraper import JobUrlScraper
import traceback


if __name__ == '__main__':
    producer = get_producer()
    consumer = get_consumer(KAFKA_INPUT_TOPIC)

    for message in consumer:
        try:
            for url in JobUrlScraper(query=message.value['query'],
                                     city=message.value['city']).get_all_job_urls():
                producer.send(KAFKA_OUTPUT_TOPIC, url)
        except Exception as e:
            tb = traceback.format_exc()
            producer.send(KAFKA_ERROR_TOPIC,
                          value=f'ERROR: {e}\n{tb}\n',
                          key='JobUrlScraper'
                          )
            raise
        finally:
            producer.flush()
