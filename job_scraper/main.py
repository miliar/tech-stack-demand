from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import re
from retry import retry


@retry(tries=3, delay=5)
def simple_get(url):
    with closing(get(url, stream=True)) as response:
        if is_good_response(response):
            return response.content
    raise RequestException(f'Error getting {url}')


def is_good_response(response):
    content_type = response.headers['Content-Type'].lower()
    return (response.status_code == 200 and
            content_type is not None and
            content_type.find('html') > -1)


def get_job_links(url):
    html = BeautifulSoup(simple_get(url), 'html.parser')
    for link in html.find_all('a', class_="jobtitle"):
        yield 'https://de.indeed.com' + link.get('href')


def get_job_description(url):
    html = BeautifulSoup(simple_get(url), 'html.parser')
    return html.find('div', id="jobDescriptionText").get_text()


def get_search_count(url):
    html = BeautifulSoup(simple_get(url), 'html.parser')
    search_count_text = html.find('div', id="searchCount").get_text()
    return int(re.findall(r'(\d+.?\d*) Jobs', search_count_text)[0].replace('.', ''))


def get_search_page_adress(start):
    return f'https://de.indeed.com/Jobs?q=software+developer&l=Berlin&sort=date&limit=50&radius=25&filter=0&start={start}'


def get_all_search_page_links():
    search_count = get_search_count(get_search_page_adress(0))
    # indeed never shows more than 1000 Jobs
    MAX = search_count if search_count < 951 else 951
    for start in range(0, MAX, 50):
        yield get_search_page_adress(start)


if __name__ == '__main__':
    for link in get_job_links(next(get_all_search_page_links())):
        print(get_job_description(link))
