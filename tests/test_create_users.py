import allure
import pytest
import requests
from api_requests.api_requests_user import ApiRequestsUser
from data.url_api import UrlApi


@allure.title("Create unique user")
@allure.step("Executing create unique user")
def test_create_unique_user(new_user):
    assert new_user is not None
    assert 'email' in new_user['user']


@allure.title("Create existing user")
@allure.step("Executing create existing user")
def test_create_existing_user(new_user):
    user = ApiRequestsUser()
    email = new_user['user']['email']
    name = new_user['user']['name']
    password = "some_password"

    user_data = user.register_new_user(email=email, password=password, name=name)


    assert user_data['success'] is False


@allure.title("Create user with missing fields")
@allure.step("Executing create user with missing fields")
@pytest.mark.parametrize("missing_field, payload", [
    ("email", {"password": "some_password", "name": "test_user"}),
    ("password", {"email": "test_user@example.com", "name": "test_user"}),
    ("name", {"email": "test_user@example.com", "password": "some_password"}),
])
def test_create_user_missing_field(missing_field, payload):
    user = ApiRequestsUser()
    url = user.base_url + UrlApi.API_REGISTER

    response = requests.post(url, json=payload)
    response_data = response.json()

    assert response.status_code == 403, f"Unexpected status code: {response.status_code}"
    assert "success" in response_data





