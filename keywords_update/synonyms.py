from paginator import Paginator
from urllib.parse import quote


class Synonyms(Paginator):
    def __init__(self, tag):
        self.tag = quote(tag)
        super().__init__()

    def _url(self, page_nr):
        url = f'https://api.stackexchange.com/2.2/tags/{self.tag}/synonyms'
        params = {'page': page_nr,
                  'pagesize': 100,
                  'order': 'desc',
                  'sort': 'applied',
                  'site': 'stackoverflow',
                  'key': 'szJ1kzWRVDtVBf2OUzdw3g(('}
        return url, params

    def all(self):
        for item in self.items():
            yield (item['from_tag'], item['to_tag'])
