import urequests as requests


class BaseClient:
    base_url: str

    def do_request(self, query):
        response = requests.get(f'{self.base_url}{query}')
        return response.json()
