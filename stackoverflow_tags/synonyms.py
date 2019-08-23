from paginator import Paginator


class Synonyms(Paginator):
    def url(self):
        return f'https://api.stackexchange.com/2.2/tags/synonyms?page={self.page_nr}&pagesize=100&order=desc&sort=applied&site=stackoverflow&key=szJ1kzWRVDtVBf2OUzdw3g(('

    def items(self):
        for item in self.page['items']:
            yield (item['to_tag'], item['from_tag'])
