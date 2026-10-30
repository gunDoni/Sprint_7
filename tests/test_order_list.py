import allure

from api.order_api import OrderApi


class TestOrderList:
    @allure.title('Список заказов возвращается в теле ответа')
    def test_order_list_without_params_success(self):
        order_list = OrderApi()
        response = order_list.order_list()
        assert isinstance(response.json()['orders'], list)
        assert response.status_code == 200