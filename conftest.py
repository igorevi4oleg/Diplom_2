from helpers.generate import Generate
from api_requests.api_requests_user import ApiRequestsUser
import json
import pytest


@pytest.fixture
def new_user():
    user_data = Generate.generate_random_string()
    email = f"{user_data}@rambler.ru"
    password = Generate.generate_random_string()
    name = Generate.generate_random_string()

    user = ApiRequestsUser()
    user_info = user.register_new_user(email, password, name)

    user_info_to_save = {
        'email': email,
        'password': password,
        'name': name
    }

    with open('users.json', 'w') as file:
        json.dump(user_info_to_save, file)

    yield user_info

    if 'accessToken' in user_info:
        user.token = user_info['accessToken']
        delete_response = user.delete_user()
        assert delete_response.get('success', False), f"Failed to delete the user: {delete_response.get('message', 'No message')}"
    else:
        raise ValueError("Access token not found for user cleanup.")



