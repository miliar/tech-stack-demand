import unittest
from job_keywords_parser import JobKeywordsParser


class TestJobKeywordsParser(unittest.TestCase):
    def setUp(self):
        self.expected_keywords = set('android ios java swift'.split())
        self.job_description = ('You are an open-minded and creative team player enjoying '
                                'constructive code and architecture discussions '
                                'Writing clean, maintainable and well documented code comes naturally '
                                'Android (Java) and/or iOS (Swift) experience is a plus '
                                'Fluency in English, German language skills are a plus though not mandatory')

    def test_get(self):
        keywords = set(JobKeywordsParser(self.job_description).get().split())
        self.assertEqual(keywords, self.expected_keywords)
