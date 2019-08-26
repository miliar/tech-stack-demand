from helper import get_html, get_consumer, get_producer


def get_job_description(url):
    return get_html(url).find('div', id="jobDescriptionText").get_text()


if __name__ == '__main__':
    consumer = get_consumer('job_urls')
    producer = get_producer()
    for url in consumer:
        producer.send('job_descriptions', get_job_description(url.value))
