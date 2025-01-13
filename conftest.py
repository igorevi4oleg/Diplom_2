from helpers.generate import Generate
from api_requests.api_requests_user import ApiRequestsUser
import json
import pytest


@pytest.fixture
def new_user():
    # Генерация случайных данных для пользователя
    user_data = Generate.generate_random_string()
    email = f"{user_data}@rambler.ru"
    password = Generate.generate_random_string()
    name = Generate.generate_random_string()

    # Создание пользователя через API
    user = ApiRequestsUser()
    user_info = user.register_new_user(email, password, name)

    # Сохранение данных пользователя в файл
    user_info_to_save = {
        'email': email,
        'password': password,
        'name': name
    }

    # Сохраняем в файл users.json (данные пользователя)
    with open('users.json', 'w') as file:
        json.dump(user_info_to_save, file)


    yield user_info


