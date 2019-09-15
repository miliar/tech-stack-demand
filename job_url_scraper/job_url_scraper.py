import re
from helper import get_html
from time import sleep
from urllib.parse import quote_plus


class JobUrlScraper:
    def __init__(self, query, city, throttle_seconds=1):
        self.query = quote_plus(query)
        self.city = quote_plus(city)
        self.search_count = self._get_search_count()
        self.throttle_seconds = throttle_seconds

    def _get_search_count(self):
        html = get_html(self._get_search_page_url())
        search_count_text = html.find('div', id="searchCount").get_text()
        return int(re.findall(r'(\d+.?\d*) Jobs', search_count_text)[0].replace('.', ''))

    def _get_search_page_url(self, start=0):
        return f'https://de.indeed.com/Jobs?q={self.query}&l={self.city}&sort=date&limit=50&radius=25&filter=0&start={start}'

    def get_all_job_urls(self):
        for url in self._get_all_search_page_urls():
            for job_url in self._get_job_urls_for_search_page(url):
                yield job_url

    def _get_all_search_page_urls(self):
        # indeed never shows more than ~1000 Jobs
        MAX = self.search_count if self.search_count < 951 else 951
        for start in range(0, MAX, 50):
            yield self._get_search_page_url(start)

    def _get_job_urls_for_search_page(self, url):
        html = get_html(url)
        for link in html.find_all('a', class_="jobtitle"):
            yield 'https://de.indeed.com' + link.get('href')
            sleep(self.throttle_seconds)
