import requests
import redis


class Paginator:
    def __init__(self):
        self.page_nr = 1
        self.page = requests.get(self.url()).json()
        self.client = self.get_client()

    def url(self):
        raise NotImplementedError("Must override url()")

    def get_client(self):
        return redis.Redis(
            host='redis',
            port=6379,
            password='password')

    def update(self):
        while True:
            for key, value in self.items():
                self.set_item(key, value)
            if self.page['has_more']:
                self.next_page()
            else:
                break

    def items(self):
        raise NotImplementedError("Must override item()")

    def set_item(self, key, value):
        if self.client.set(key, value):
            print(f'SET {key}: {value}')
        else:
            print(f'ERROR SET {key}: {value}')  # Retry?

    def next_page(self):
        self.page_nr += 1
        self.page = requests.get(self.url()).json()
