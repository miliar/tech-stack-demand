import requests


class Paginator:
    def __init__(self):
        self.page_nr = 1
        self.page = requests.get(self.url()).json()

    def url(self):
        raise NotImplementedError("Must override url()")

    def update(self):
        while True:
            self.send_page()
            if self.page['has_more']:
                self.next_page()
            else:
                break

    def send_page(self):
        item_batch = {key: value for key, value in self.items()}
        response = requests.put('http://keywords_api:4000/keywords',
                                json=item_batch)
        print(response.status_code, list(zip(item_batch.keys(),
                                             item_batch.values(),
                                             response.json())))  # To do: error handling

    def items(self):
        raise NotImplementedError("Must override item()")

    def next_page(self):
        self.page_nr += 1
        self.page = requests.get(self.url()).json()
