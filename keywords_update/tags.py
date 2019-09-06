from paginator import Paginator
from synonyms import Synonyms


class Tags(Paginator):
    def _url(self, page_nr):
        url = 'https://api.stackexchange.com/2.2/tags'
        params = {'page': page_nr,
                  'pagesize': 100,
                  'order': 'desc',
                  'sort': 'popular',
                  'site': 'stackoverflow',
                  'key': 'szJ1kzWRVDtVBf2OUzdw3g(('
                  }
        return url, params

    def all(self, min_count=1000):
        for item in self.items():
            if item['count'] > min_count:
                yield (item['name'], item['name'])
                if item['has_synonyms']:
                    for synonym in Synonyms(item['name']).all():
                        yield synonym
            else:
                break
