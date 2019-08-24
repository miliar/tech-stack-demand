from paginator import Paginator


class Tags(Paginator):
    def url(self):
        return f'https://api.stackexchange.com/2.2/tags?page={self.page_nr}&pagesize=100&order=desc&sort=popular&site=stackoverflow&key=szJ1kzWRVDtVBf2OUzdw3g(('

    def items(self):
        for item in self.page['items']:
            yield (item['name'], item['name'])


if __name__ == '__main__':
    Tags().update()
