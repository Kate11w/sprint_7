import requests
import allure

from data import OrderData
from urls import Urls


class TestOrdersList:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверка кода ответа и что в теле ответа возвращается список заказов.')
    def test_orders_list_get_success(self):
        with allure.step("Отправляем GET-запрос на получение списка заказов"):
            response = requests.get(Urls.GET_ORDERS)

        with allure.step("Проверяем код ответа"):
            assert response.status_code == OrderData.order_expected_response["status_code"], \
                f"Код ответа: {response.status_code}, тело: {response.text}"

        with allure.step("Проверяем, что в ответе есть 'orders'"):
            assert isinstance(response.json().get("orders"), list) and \
                   OrderData.order_expected_response["key_in_response"] in response.json(), \
                f"В ответе нет 'orders' {OrderData.order_expected_response['key_in_response']} или 'orders' не является списком"

