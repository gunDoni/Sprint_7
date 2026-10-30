import allure

from api.base_api import BaseApi
from urls import BASE_URL, GENERAL_PART_OF_THE_PATH, COURIER_PATH, LOGIN_PATH


class CourierApi(BaseApi):
    @allure.step('Создать курьера')
    def courier_creation(self, body=None):
        response = self.post(BASE_URL + GENERAL_PART_OF_THE_PATH + COURIER_PATH, body)
        return response

    @allure.step('Войти в аккаунт курьера')
    def courier_login(self, body=None):
        response = self.post(BASE_URL + GENERAL_PART_OF_THE_PATH + LOGIN_PATH, body)
        return response

    @allure.step('Удалить аккаунт курьера')
    def courier_delete(self, courier_id):
        response = self.delete(f'{BASE_URL}{GENERAL_PART_OF_THE_PATH}{COURIER_PATH}/{courier_id}')
        return response