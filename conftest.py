from helpers.generate import Generate
from api_requests.api_requests_user import ApiRequestsUser
import pytest
import requests
from data.url_api import UrlApi


@pytest.fixture
def new_user():
    user_data = Generate.generate_random_string()
    email = f"{user_data}@rambler.ru"
    password = Generate.generate_random_string()
    name = Generate.generate_random_string()

    user = ApiRequestsUser()
    response = user.register_new_user(email, password, name)

    response_json = response.json()

    if "accessToken" not in response_json:
        raise ValueError(f"User registration response does not contain accessToken: {response_json}")

    yield response, email, password

    if "accessToken" in response_json:
        user.token = response_json["accessToken"]
        delete_response = user.delete_user()

        assert delete_response.get("success") is True, f"Failed to delete the user: {delete_response.get('message', 'No message')}"



@pytest.fixture
def get_ingredients():
    url = UrlApi.BASE_URL + UrlApi.API_INGREDIENTS
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['data']






