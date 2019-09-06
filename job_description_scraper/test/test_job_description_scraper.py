import unittest
from unittest.mock import patch
from bs4 import BeautifulSoup
from job_description_scraper import JobDescriptionScraper


class TestJobDescriptionScraper(unittest.TestCase):
    def setUp(self):
        with open("test/fixture/indeed.html", "rb") as description_page:
            self.description_page = BeautifulSoup(description_page, 'html5lib')
        self.expected_job_description = 'Test description'
        self.expected_job_company = 'Test company'

    def test_get_job_description(self):
        with patch('job_description_scraper.get_html') as mocked_get:
            mocked_get.side_effect = lambda url: self.description_page
            job_description = JobDescriptionScraper(
                'https://test').get_job_description()
            self.assertEqual(job_description, self.expected_job_description)

    def test_get_job_company(self):
        with patch('job_description_scraper.get_html') as mocked_get:
            mocked_get.side_effect = lambda url: self.description_page
            job_company = JobDescriptionScraper(
                'https://test').get_job_company()
            self.assertEqual(job_company, self.expected_job_company)
