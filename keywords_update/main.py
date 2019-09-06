import requests
import itertools
from tags import Tags


def batches(batch_size=100):
    iter_all = iter(Tags().all())
    batch = list(itertools.islice(iter_all, batch_size))
    while batch:
        yield batch
        batch = list(itertools.islice(iter_all, batch_size))


if __name__ == '__main__':
    for batch in batches():
        json = {key: value for key, value in batch}
        response = requests.put('http://keywords_api:4000/keywords',
                                json=json
                                )
        print(response.status_code, list(zip(json.keys(),
                                             json.values(),
                                             response.json()
                                             )
                                         )
              )
