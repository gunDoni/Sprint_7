import allure
import pytest

from api.courier_api import CourierApi
from data import NOT_ENOUGH_DATA_CREATION, REPEATING_LOGIN_CREATION, REQUIRED_FIELDS_CREATION_LOGIN
from helpers import generate_courier_data


class TestCourierCreation:
    @allure.title('Курьера можно создать')
    def test_courier_creation_valid_data_success(self, generate_data):
        courier = CourierApi()
        response = courier.courier_creation(generate_data)
        assert response.json() == {"ok": True}
        assert response.status_code == 201

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_courier_creation_duplicate_data_conflict(self, generate_data):
        courier = CourierApi()
        creation_data = generate_data
        courier.courier_creation(creation_data)
        response = courier.courier_creation(creation_data)
        assert response.json()['message'] == REPEATING_LOGIN_CREATION
        assert response.status_code == 409

    @allure.title('Нельзя создать курьера без поля {missing_field}')
    @pytest.mark.parametrize('missing_field', REQUIRED_FIELDS_CREATION_LOGIN)
    def test_courier_creation_missing_field_bad_request(self, missing_field):
        courier = CourierApi()
        data = generate_courier_data()
        data.pop(missing_field)
        response = courier.courier_creation(data)
        assert response.json()['message'] == NOT_ENOUGH_DATA_CREATION
        assert response.status_code == 400