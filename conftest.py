from http.client import responses
from platform import java_ver

from main_data.pet import pet_dict
from main_data.user import user_dict
from main_data.store import order_dict
import requests
import pytest

@pytest.fixture()
def url():
    return "https://petstore.swagger.io/v2"

@pytest.fixture
def create_pet(url):
    response = requests.post(url + "/pet", json = pet_dict)
    assert response.status_code == 200
    pet_id = response.json()["id"]
    yield pet_id
    delete_pet = requests.delete(url + f"/pet/{pet_id}")
    if delete_pet.status_code not in (200, 404):
        assert False


@pytest.fixture
def create_user(url):
    response = requests.post(url + "/user" , json=user_dict)
    assert response.status_code == 200
    username = user_dict["username"]
    yield username
    delete_user = requests.delete(url + f"/user/{username}")
    assert delete_user.status_code == 200

@pytest.fixture
def create_user_for_login(url):
    response = requests.post(url + "/user" , json=user_dict)
    assert response.status_code == 200
    username = user_dict["username"]
    yield user_dict
    delete_user = requests.delete(url + f"/user/{username}")
    if delete_user.status_code not in (200, 404):
        assert False


@pytest.fixture
def create_order(url):
    response = requests.post(url + "/store/order", json=order_dict)
    assert response.status_code == 200
    order_id = response.json()["id"]
    yield order_id
    delete_order = requests.delete(url + f"/store/order/{order_id}")
    if delete_order.status_code not in (200, 404):
        assert False



@pytest.fixture
def delete_pet(url):
    def _delete_pet(pet_id):
        response = requests.delete(url + f"/pet/{pet_id}")
        assert response.status_code == 200

    yield _delete_pet

@pytest.fixture()
def delete_user(url):
    def _delete_user(user_id):
        response = requests.delete(url + f"/user/{user_id}")
        assert response.status_code == 200

    yield _delete_user

@pytest.fixture
def delete_order(url):
    def _delete_order(order_id):
        response = requests.delete(url + f"/store/order/{order_id}")
        assert response.status_code == 200

    yield _delete_order