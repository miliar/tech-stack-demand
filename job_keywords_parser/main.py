from helper import get_producer, get_consumer
from config import KAFKA_INPUT_TOPIC, KAFKA_OUTPUT_TOPIC, KAFKA_ERROR_TOPIC
from job_keywords_parser import JobKeywordsParser
import traceback

if __name__ == '__main__':
    consumer = get_consumer(KAFKA_INPUT_TOPIC)
    producer = get_producer()

    for description in consumer:
        try:
            job_keywords = JobKeywordsParser(description.value).get()
        except Exception as e:
            tb = traceback.format_exc()
            producer.send(KAFKA_ERROR_TOPIC,
                          value=f'FOR: {description} \nERROR: {e}\n{tb}\n',
                          key='JobKeywordsParser'
                          )
            continue

        producer.send(KAFKA_OUTPUT_TOPIC,
                      value=job_keywords,
                      key=description.key
                      )
