import allure
import requests
from data.url_api import UrlApi

@allure.title("Update user with auth")
@allure.step("Executing update user with auth")
def test_update_user_with_auth(new_user):
    token = new_user['accessToken']
    headers = {'Authorization': f"{token}", 'Content-Type': 'application/json'}

    payload = {'name': "New Name"}

    response = requests.patch(f"{UrlApi.BASE_URL}/{UrlApi.API_USER}", headers=headers, json=payload)

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.json()['user']['name'] == "New Name", "Name was not updated"


@allure.title("Update user without auth")
@allure.step("Executing update user without auth")
def test_update_user_without_auth():
    payload = {'name': "New Name"}

    response = requests.patch(f"{UrlApi.BASE_URL}/{UrlApi.API_USER}", json=payload)

    assert response.status_code == 401
    assert response.json()['success'] is False
    assert response.json()['message'] == "You should be authorised"
