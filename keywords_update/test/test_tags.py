import unittest
from unittest.mock import patch
from tags import Tags
import json


class TestTags(unittest.TestCase):
    def setUp(self):
        self.expected_tags = [
            ('python', 'python'), ('py', 'python'), ('python-shell', 'python'), ('c', 'c')]

    def test_all(self):
        with patch('tags.Synonyms.all') as synonyms,\
                patch('tags.Tags._get_page', autospec=True) as mocked_get,\
                open('test/fixture/tags1.json') as tags_page_1,\
                open('test/fixture/tags2.json') as tags_page_2:
            synonyms.return_value = [('py', 'python'),
                                     ('python-shell', 'python')]
            mocked_get.side_effect = lambda _self: json.load(tags_page_1) \
                if _self.page_nr == 1 else json.load(tags_page_2)
            tags = [tag for tag in Tags().all()]
            self.assertEqual(tags, self.expected_tags)
