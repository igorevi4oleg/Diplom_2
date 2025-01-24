import allure
import pytest
from api_requests.api_create_order import ApiRequestsOrder
from helpers.random_ingridients import get_random_ingredients


@pytest.mark.usefixtures("new_user", "get_ingredients")
class TestCreateOrders:
    @allure.title("Create order with auth")
    def test_create_order_with_auth(self, new_user, get_ingredients, get_random_ingredients):
        response, email, password = new_user
        access_token = response.json()['accessToken']
        selected_ingredients = get_random_ingredients
        order_api = ApiRequestsOrder(access_token=access_token)
        response = order_api.create_order(selected_ingredients)

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'order' in response.json()


    @allure.title("Create order without auth")
    def test_create_order_without_auth(self, get_ingredients, get_random_ingredients):
        selected_ingredients = get_random_ingredients
        order_api = ApiRequestsOrder()
        response = order_api.create_order(selected_ingredients, authorization=False)
        assert response.json()['success'] is True
        assert response.status_code == 200, f"Expected 401, but got {response.status_code}"
        assert response.json().get('success') is True, "Expected success=True for unauthorized order creation"


    @allure.title("Create order with auth")
    def test_create_order_with_ingredients(self, new_user, get_ingredients, get_random_ingredients):
        response, email, password = new_user
        user_data = response.json()

        selected_ingredients = get_random_ingredients

        order_api = ApiRequestsOrder(access_token=user_data["accessToken"])
        response = order_api.create_order(selected_ingredients, authorization=True)

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'order' in response.json()

    @allure.title("Create order without ingredient hash")
    def test_create_order_without_ingredients(self, new_user):
        response, email, password = new_user
        access_token = response.json()['accessToken']

        order_api = ApiRequestsOrder(access_token=access_token)
        response = order_api.create_order([])
        assert response.json()['success'] is False
        assert response.json()['message'] == 'Ingredient ids must be provided'
        assert response.status_code == 400, f"Expected 400, but got {response.status_code}"


    @allure.title("Create order with invalid ingredient hash")
    def test_create_order_with_invalid_ingredient_hash(self, new_user):
        response, email, password = new_user
        access_token = response.json()['accessToken']

        invalid_ingredient_hash = "invalid_hash_value"
        order_api = ApiRequestsOrder(access_token=access_token)
        response = order_api.create_order([invalid_ingredient_hash])
        assert response.status_code == 500, f"Expected 500, but got {response.status_code}"











