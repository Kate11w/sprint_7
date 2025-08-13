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
    def test_create_order_with_colors(self, colors, order_delete):
        order_data = OrderData.order_data
        order_data['color'] = colors

        with allure.step(f"Отправляем POST-запрос на создание заказа с цветом: {colors}"):
            response = requests.post(Urls.CREATE_ORDER, json=order_data)

        with allure.step("Проверяем код ответа"):
            assert response.status_code == OrderData.order_create_status["status_code"], \
                f"Код ответа: {response.status_code}, тело: {response.text}"

        with allure.step(f"Проверяем, что ответ содержит '{OrderData.order_create_status['key_in_response']}'"):
            assert OrderData.order_create_status["key_in_response"] in response.json(), \
                f"В ответе нет {OrderData.order_create_status['key_in_response']}: {response.json()}"

        with allure.step("Отмена созданного заказа"):
            order_delete["track"] = response.json()["track"]
