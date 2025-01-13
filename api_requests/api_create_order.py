from data.url_api import UrlApi
import requests


class ApiRequestsOrder:
    def __init__(self, access_token=None):
        self.base_url = f'{UrlApi.BASE_URL}/{UrlApi.API_ORDER}'
        self.headers = {'Authorization': access_token} if access_token else {}

    def create_order(self, ingredients, authorization=True):
        payload = {'ingredients': ingredients}
        headers = {'Content-Type': 'application/json'}
        if authorization:
            headers.update(self.headers)

        response = requests.post(self.base_url, json=payload, headers=headers)

        return response










