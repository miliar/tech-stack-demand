import requests


class Paginator:
    def __init__(self):
        self.page_nr = 1
        self.page = self._get_page()

    def _get_page(self):
        url, params = self._url(self.page_nr)
        return requests.get(url, params=params).json()

    def _url(self, page_nr):
        raise NotImplementedError("Must override url()")

    def items(self):
        while True:
            for item in self.page['items']:
                yield item
            if self.page['has_more']:
                self._next_page()
            else:
                break

    def _next_page(self):
        self.page_nr += 1
        self.page = self._get_page()
