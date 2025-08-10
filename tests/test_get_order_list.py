import requests
import allure

from urls import Urls


class TestOrdersList:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверка кода ответа и что в теле ответа возвращается список заказов.')
    def test_orders_list_get_success(self):
        response = requests.get(Urls.GET_ORDERS)
        assert response.status_code == 200
        assert type(response.json()['orders']) == list and 'orders' in response.json()
