import requests
import allure
import pytest

from data import *
from urls import Urls

class TestOrderCreate:

    @allure.title('Проверка создания заказа с разными цветами')
    @allure.description('''Возможные варианты:
    - BLACK
    - GREY
    - оба цвета
    - без указания цвета''')
    @pytest.mark.parametrize('colors', OrderData.scooter_color)

    def test_create_order_with_colors(self, colors):
        order_data = OrderData.order_data
        order_data['color'] = colors

        response = requests.post(Urls.CREATE_ORDER, json=order_data)
        assert response.status_code == 201, f"Код ответа: {response.status_code}, тело: {response.text}"
        assert "track" in response.json(), f"В ответе нет track: {response.json()}"

        track = response.json()["track"]
        cancel_response = requests.put(f"{Urls.ORDER_CANCEL}{track}")
        assert cancel_response.status_code == 200, f"Не удалось отменить заказ {track}"
