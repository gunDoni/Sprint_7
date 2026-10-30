import allure

from api.base_api import BaseApi
from urls import BASE_URL, GENERAL_PART_OF_THE_PATH, ORDER_PATH


class OrderApi(BaseApi):
    @allure.step('Создать заказ')
    def order_creation(self, body=None):
        response = self.post(BASE_URL + GENERAL_PART_OF_THE_PATH + ORDER_PATH, body)
        return response

    @allure.step('Получить список заказов')
    def order_list(self):
        response = self.get(BASE_URL + GENERAL_PART_OF_THE_PATH + ORDER_PATH)
        return response