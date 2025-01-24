import random
import pytest

@pytest.fixture
def get_random_ingredients(get_ingredients, count=3):
    ingredient_ids = [ingredient['_id'] for ingredient in get_ingredients if ingredient.get('_id')]
    return random.sample(ingredient_ids, 3)
