from data.url_api import UrlApi
import requests

class ApiRequestsUser:
    def __init__(self):
        self.base_url = UrlApi.BASE_URL
        self.token = None

    def register_new_user(self, email, password, name):
        url = self.base_url + UrlApi.API_REGISTER
        response = requests.post(url, json={'email': email, 'password': password, 'name': name})
        return response.json()

    def login_user(self, email, password):
        url = self.base_url + UrlApi.API_LOGIN
        response = requests.post(url, json={'email': email, 'password': password})
        self.response = response
        if response.status_code == 200:
           data = response.json()
           self.token = data.get('accessToken')
        else:
           self.token = None
        return response.json()

    def get_user_info(self):
        if not self.is_authenticated():
            raise ValueError("User is not authenticated. Login to get a valid token.")

        url = self.base_url + UrlApi.API_USER
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(url, headers=headers)
        return response.json()

    def is_authenticated(self):
        return hasattr(self, 'token') and self.token is not None

    def delete_user(self):
        if not self.is_authenticated():
            raise ValueError("User is not authenticated. Login to get a valid token.")

        url = f"{self.base_url}{UrlApi.API_USER}"
        headers = {'Authorization': f'{self.token}'}
        response = requests.delete(url, headers=headers)

        return response.json()

