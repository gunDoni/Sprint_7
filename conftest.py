import pytest

from api.courier_api import CourierApi
from helpers import generate_courier_data


@pytest.fixture
def create_courier():
    courier = CourierApi()
    data_creation = generate_courier_data()
    courier.courier_creation(data_creation)
    yield data_creation
    data_login = {
        'login': data_creation['login'],
        'password': data_creation['password']
    }
    response = courier.courier_login(data_login)
    courier_id = response.json()['id']
    courier.courier_delete(courier_id)


@pytest.fixture
def generate_data():
    courier = CourierApi()
    data_creation = generate_courier_data()
    yield data_creation
    data_login = {
        'login': data_creation['login'],
        'password': data_creation['password']
    }
    response = courier.courier_login(data_login)
    courier_id = response.json()['id']
    courier.courier_delete(courier_id)