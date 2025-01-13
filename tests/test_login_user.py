import allure
from api_requests.api_requests_user import ApiRequestsUser
import json

@allure.title("Login with invalid credentials")
@allure.step("Executing login with invalid credentials")
def test_login_with_invalid_credentials(new_user):
    user = ApiRequestsUser()
    user.login_user("wrong_email", "wrong_password")
    assert user.response.status_code == 401, f"Expected status 401, but got {user.response.status_code}"


@allure.title("Login with valid credentials")
@allure.step("Executing login with valid credentials")
def test_login_with_valid_credentials(new_user):
    with open('users.json', 'r') as file:
        user_data = json.load(file)

    email = user_data['email']
    password = user_data['password']

    user = ApiRequestsUser()
    response = user.login_user(email, password)

    assert user.response.status_code == 200, f"Expected status 200, but got {user.response.status_code}"
    assert user.is_authenticated()
    assert response['success'] is True







