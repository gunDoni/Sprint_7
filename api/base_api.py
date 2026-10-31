import allure
import requests


class BaseApi:
    @allure.step('Отправить POST-запрос на {address}')
    def post(self, address, body=None):
        return requests.post(address, json=body)

    @allure.step('Отправить GET-запрос на {address}')
    def get(self, address, params=None):
        return requests.get(address, params=params)

    @allure.step('Отправить DELETE-запрос на {address}')
    def delete(self, address, params=None):
        return requests.delete(address, params=params)