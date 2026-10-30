import allure
import pytest

from api.order_api import OrderApi
from data import ORDER_DATA, COLORS


class TestOrderCreation:
    @allure.title('Заказ можно создать с цветом {color}')
    @pytest.mark.parametrize('color', COLORS)
    def test_order_creation_with_color_success(self, color):
        order = OrderApi()
        order_data = ORDER_DATA.copy()
        order_data.update({'color': color})
        response = order.order_creation(order_data)
        assert 'track' in response.json()
        assert response.status_code == 201