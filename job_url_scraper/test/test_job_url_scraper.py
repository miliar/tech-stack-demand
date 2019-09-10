import unittest
from unittest.mock import patch
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from job_url_scraper import JobUrlScraper


class TestJobUrlScraper(unittest.TestCase):
    def setUp(self):
        with open("test/fixture/indeed.html", "rb") as main_page:
            self.main_page = BeautifulSoup(main_page, 'html.parser')
        self.expected_job_urls = ['https://de.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0BxmYOcUAOCxszE55UOx1TO4Bjpw4RpwxvlqCjBXNXKm2wRvcoD9J4--SNUQesMtSy-vr2yh68bNFxNdRpV4kVHIk-0G8b1eqbnBWRmTbYe3d8AFUqxS4FW2GJmr3H1tD7AWf2RZydIQoMWTDhR3G1P24FJNdHhfY5aglKdywfs-OG1HbmTSC-kgxb83VSs8iBeBWPM0nynD-hD6oML61Ann4BsxGJ9f5kENuOy2avf9D5sW0L1Gk7FUpkoQvqpeoQ16VZfVbwy0-nm5d3vEu4fpmL7gdC-kEISLlsufw3f8pEhoJEu7eFn7KUR89LHguia_qDuGhIRopvxfP0htKCjSFf6-Xl5xs882im12Y7Je4qMzgosSjAysBAg0P6Yz9mPSKT-r_UcZCf8ebx6sX0-v5canBGmjtVcG53hWAl6jVkFxmDyKkKlSo3WfhYaN1_wH48gEm3k-TCauiKV3yPZoWL6pC4YS4MbPFlNEgMrfH_npv29JFat_403no1bP3jdsU-fPVjUQWusDix4aS9RcV0fv_dh5oIf2BaER3HdPbtblte5Banf&p=0&fvj=0&vjs=3',
                                  'https://de.indeed.com/rc/clk?jk=408631187bf9f4cc&fccid=a7afbf852fe5faac&vjs=3', 'https://de.indeed.com/rc/clk?jk=1b690bbe180f0368&fccid=51e9cda0233157b6&vjs=3', 'https://de.indeed.com/rc/clk?jk=cf1feef5bb5eadd4&fccid=1a0eee8ef41e113f&vjs=3', 'https://de.indeed.com/rc/clk?jk=a5c928125514f410&fccid=1a0eee8ef41e113f&vjs=3']

    def test_get_all_job_urls(self):
        def get_html(url):
            if url == 'https://de.indeed.com/Jobs?q=software+developer+c%23&l=Berlin&sort=date&limit=50&radius=25&filter=0&start=0':
                return self.main_page
            raise RequestException(f'Error getting {url}')

        with patch('job_url_scraper.get_html') as mocked_get:
            mocked_get.side_effect = get_html
            job_urls = [url for url in JobUrlScraper(
                query='software developer c#',
                city='Berlin',
                throttle_seconds=0).get_all_job_urls()]
            self.assertEqual(job_urls, self.expected_job_urls)
