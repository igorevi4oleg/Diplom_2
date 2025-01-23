import allure
import pytest
from api_requests.api_requests_user import ApiRequestsUser


@pytest.mark.usefixtures("new_user")
class TestLoginUser:
    @allure.title("Login with invalid credentials")
    def test_login_with_invalid_credentials(self):
        user = ApiRequestsUser()
        response = user.login_user("wrong_email_user", "wrong_password_user")
        assert response.json()['success'] is False
        assert response.status_code == 401, f"Expected status 401, but got {response.status_code}"


    @allure.title("Login with valid credentials")
    def test_login_with_valid_credentials(self, new_user):
        user_api = ApiRequestsUser()
        response, email, password = new_user
        response = user_api.login_user(email, password)
        assert response.json()['success'] is True
        assert response.status_code == 200, f"Expected 200, but got {response.status_code}"









