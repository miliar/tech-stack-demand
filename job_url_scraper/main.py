from helper import get_producer
from config import KAFKA_ERROR_TOPIC, KAFKA_OUTPUT_TOPIC
from job_url_scraper import JobUrlScraper
import traceback


if __name__ == '__main__':
    producer = get_producer()

    try:
        for url in JobUrlScraper().get_all_job_urls():
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
