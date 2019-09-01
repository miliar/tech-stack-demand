import unittest
from unittest.mock import patch
from synonyms import Synonyms
import json


class TestSyonyms(unittest.TestCase):
    def setUp(self):
        self.expected_synonyms = [('py', 'python'), ('python-shell', 'python')]

    def test_all(self):
        with patch('synonyms.Synonyms._get_page') as mocked_get,\
                open('test/fixture/synonyms.json') as synonyms_page:
            mocked_get.return_value = json.load(synonyms_page)
            synonyms = [synonym for synonym in Synonyms('python').all()]
            self.assertEqual(synonyms, self.expected_synonyms)
