from helper import get_consumer, get_producer
from config import KAFKA_INPUT_TOPIC, KAFKA_OUTPUT_TOPIC, KAFKA_ERROR_TOPIC
from job_description_scraper import JobDescriptionScraper
import traceback

if __name__ == '__main__':
    consumer = get_consumer(KAFKA_INPUT_TOPIC)
    producer = get_producer()

    for url in consumer:
        try:
            scraper = JobDescriptionScraper(url.value)
            value = scraper.get_job_description()
            key = scraper.get_job_company()
        except Exception as e:
            tb = traceback.format_exc()
            producer.send(KAFKA_ERROR_TOPIC,
                          value=f'FOR: {url} \nERROR: {e}\n{tb}\n',
                          key='JobDescriptionScraper'
                          )
            continue

        producer.send(KAFKA_OUTPUT_TOPIC,
                      value=value,
                      key=key
                      )
