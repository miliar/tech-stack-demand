from helper import get_consumer, get_producer
import requests


class JobKeywordsParser:
    def __init__(self, text):
        self.text = text

    def get(self):
        return ' '.join(requests.get('http://keywords_api:4000/keywords/' +
                                     self._preprocess_text()).json())

    def _preprocess_text(self):
        text = ''.join(
            ' ' if c in '! ” $ % & ( ) * / : ; , < = > ? @ | [ ] ` ~ ^ { } \\ \''.split() else c for c in self.text)
        text = text.replace('. ', ' ').replace(
            '.\n', ' ').replace('#', 'sharp')
        return ' '.join(text.lower().split())


if __name__ == '__main__':
    consumer = get_consumer('job_descriptions')
    producer = get_producer()

    for description in consumer:
        job_keywords = JobKeywordsParser(description.value).get()
        producer.send('job_keywords',
                      value=job_keywords,
                      key=description.key)
        print(job_keywords, flush=True)
