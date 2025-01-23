import allure
import pytest
import requests
from api_requests.api_requests_user import ApiRequestsUser
from data.url_api import UrlApi


@pytest.mark.usefixtures("new_user")
class TestCreateUser:
    @allure.title("Create unique user")
    def test_create_unique_user(self, new_user):
        response, email, password = new_user

        assert response.status_code == 200, f"Expected 200, but got {response.status_code}"

        response_json = response.json()

        assert response_json["success"], "User creation was not successful"
        assert "email" in response_json["user"], "User response does not contain email"
        assert response_json["user"]["email"] == email, "Email in response does not match registered email"

    @allure.title("Create existing user")
    def test_create_existing_user(self, new_user):
        response, email, password = new_user
        user = ApiRequestsUser()

        response = user.register_new_user(email, password, "test_user")
        response_json = response.json()

        assert response.status_code == 403, f"Expected 403, but got {response.status_code}"
        assert not response_json["success"], "User creation should not be successful"
        assert "message" in response_json, "Response should contain a message"




    @allure.title("Create user with missing fields")
    @pytest.mark.parametrize("missing_field, payload", [
        ("email", {"password": "some_password", "name": "test_user"}),
        ("password", {"email": "test_user@example.com", "name": "test_user"}),
        ("name", {"email": "test_user@example.com", "password": "some_password"}),
    ])
    def test_create_user_missing_field(self, missing_field, payload):
        user = ApiRequestsUser()
        url = user.base_url + UrlApi.API_REGISTER
        response = requests.post(url, json=payload)
        response_data = response.json()

        assert response.status_code == 403, f"Unexpected status code: {response.status_code}"
        assert "success" in response_data





