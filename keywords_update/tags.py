import requests
import itertools
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
                  'key': 'szJ1kzWRVDtVBf2OUzdw3g(('}
        return url, params

    def _all(self, min_count=5000):
        for item in self.items():
            if item['count'] > min_count:
                yield (item['name'], item['name'])
                if item['has_synonyms']:
                    for synonym in Synonyms(item['name']).all():
                        yield synonym
            else:
                break

    def _batches(self, batch_size=100):
        iter_all = iter(self._all())
        batch = list(itertools.islice(iter_all, batch_size))
        while batch:
            yield batch
            batch = list(itertools.islice(iter_all, batch_size))

    def update(self):
        for batch in self._batches():
            json = {key: value for key, value in batch}
            response = requests.put('http://keywords_api:4000/keywords',
                                    json=json)
            print(response.status_code, list(zip(json.keys(),
                                                 json.values(),
                                                 response.json())))  # To do: error handling


if __name__ == '__main__':
    Tags().update()
