import allure
import pytest

from api.courier_api import CourierApi
from data import NOT_ENOUGH_DATA_LOGIN, NON_EXISTING_USER_LOGIN, REQUIRED_FIELDS_CREATION_LOGIN
from helpers import generate_random_string, generate_courier_data


class TestCourierLogin:
    @allure.title('Курьер может авторизоваться')
    def test_courier_login_valid_data_success(self, create_courier):
        courier = CourierApi()
        data_creation = create_courier
        data_login = {
            'login': data_creation['login'],
            'password': data_creation['password']
        }
        response = courier.courier_login(data_login)
        assert "id" in response.json()
        assert response.status_code == 200

    @allure.title('Нельзя авторизоваться без поля {missing_field}')
    @pytest.mark.parametrize('missing_field', REQUIRED_FIELDS_CREATION_LOGIN)
    def test_courier_login_missing_field_bad_request(self, create_courier, missing_field):
        courier = CourierApi()
        data_creation = create_courier
        one_required_field_data = data_creation.copy()
        one_required_field_data.pop('firstName', None)
        one_required_field_data.pop(missing_field, None)
        response = courier.courier_login(one_required_field_data)
        assert response.json()['message'] == NOT_ENOUGH_DATA_LOGIN
        assert response.status_code == 400

    @allure.title('Нельзя авторизоваться с неверным значением поля {replaced_field}')
    @pytest.mark.parametrize('replaced_field', REQUIRED_FIELDS_CREATION_LOGIN)
    def test_courier_login_wrong_field_not_found(self, create_courier, replaced_field):
        courier = CourierApi()
        data_creation = create_courier
        one_replaced_field_data = data_creation.copy()
        one_replaced_field_data.pop('firstName', None)
        one_replaced_field_data[replaced_field] = generate_random_string(10)
        response = courier.courier_login(one_replaced_field_data)
        assert response.json()['message'] == NON_EXISTING_USER_LOGIN
        assert response.status_code == 404

    @allure.title('Авторизация несуществующего пользователя возвращает ошибку')
    def test_courier_login_non_existing_user_not_found(self):
        courier = CourierApi()
        payload = generate_courier_data()
        payload.pop('firstName', None)
        response = courier.courier_login(payload)
        assert response.json()['message'] == NON_EXISTING_USER_LOGIN
        assert response.status_code == 404