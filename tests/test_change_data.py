import allure
import requests
import pytest
from data.url_api import UrlApi


@pytest.mark.usefixtures("new_user")
class TestUpdateUser:
    @allure.title("Update user with auth")
    def test_update_user_with_auth(self, new_user):
        response, email, password = new_user
        response_json = response.json()
        token = response_json["accessToken"]
        payload = {'name': "Updated Name"}
        headers = {"Authorization": token}
        update_response = requests.patch(f"{UrlApi.BASE_URL}{UrlApi.API_USER}", json=payload, headers=headers)

        assert update_response.status_code == 200, f"Expected 200, but got {update_response.status_code}"
        assert update_response.json()["user"]["name"] == "Updated Name", "User name was not updated"



    @allure.title("Update user without auth")
    def test_update_user_without_auth(self):
        payload = {'name': "New Name"}
        response = requests.patch(f"{UrlApi.BASE_URL}{UrlApi.API_USER}", json=payload)

        assert response.status_code == 401, f"Expected 401, but got {response.status_code}"

