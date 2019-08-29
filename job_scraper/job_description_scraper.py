from helper import get_html, get_consumer, get_producer


class JobDescriptionScraper:
    def __init__(self, url):
        self.html = get_html(url)

    def get_job_description(self):
        return self.html.find('div', id="jobDescriptionText").get_text()

    def get_job_company(self):
        return next(self.html.find('div', class_='jobsearch-CompanyInfoWithoutHeaderImage').stripped_strings)


if __name__ == '__main__':
    consumer = get_consumer('job_urls')
    producer = get_producer()
    for url in consumer:
        scraper = JobDescriptionScraper(url.value)
        value = scraper.get_job_description()
        key = scraper.get_job_company()
        producer.send('job_descriptions',
                      value=value,
                      key=key)
        print('SEND KEY: ' + key)
        print('SEND VALUE: ' + value, flush=True)
