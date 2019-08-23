import requests


class Paginator:
    def __init__(self):
        self.page_nr = 1
        self.page = requests.get(self.url()).json()

    def url(self):
        raise NotImplementedError("Must override url()")

    def all(self):
        while True:
            for item in self.items():
                yield item
            if self.page['has_more']:
                self.next_page()
            else:
                break

    def items(self):
        raise NotImplementedError("Must override item()")

    def next_page(self):
        self.page_nr += 1
        self.page = requests.get(self.url()).json()
