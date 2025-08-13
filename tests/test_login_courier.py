import pytest
import requests
import allure

from data import CourierData
from urls import Urls
from generators import *

class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверка "id" курьера при авторизации')
    def test_success_login_courier(self, create_and_delete_courier):
        courier_data = create_and_delete_courier
        with allure.step("Отправляем POST-запрос на авторизацию курьера"):
            login_response = requests.post(Urls.LOGIN_COURIER, data=courier_data)

        with allure.step("Проверяем код ответа"):
            assert login_response.status_code == CourierData.login_success_response["status_code"], \
                f"Не удалось авторизоваться: {login_response.text}"

        with allure.step("Проверяем, что в ответе есть id"):
            assert CourierData.login_success_response["key_in_response"] in login_response.json(), "В ответе нет id"

    @allure.title('Ошибка аутентификации при пустом значении обязательного поля')
    @allure.description('Передаем пустое значение в login или password. '
                        'Ожидаем код 400 и сообщение об ошибке.')
    @pytest.mark.parametrize("empty_field", ["login", "password"])
    def test_login_empty_required_fields(self, create_and_delete_courier, empty_field):
        courier_data = create_and_delete_courier
        login_data = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        login_data[empty_field] = ""

        with allure.step(f"Отправляем POST-запрос на авторизацию с пустым полем '{empty_field}'"):
            response = requests.post(Urls.LOGIN_COURIER, json=login_data)

        with allure.step("Проверяем код ответа"):
            assert response.status_code == CourierData.login_empty_field_response["status_code"], \
                f"Ожидался 400, получили {response.status_code}"

        with allure.step("Проверяем текст ошибки"):
            assert CourierData.login_empty_field_response["error_text"] in response.text, \
                f"Ожидалось сообщение '{CourierData.login_empty_field_response['error_text']}', получили {response.text}"

    @allure.title("Ошибка при неправильном логине или пароле")
    @allure.description("Передаем неверный логин или пароль. Ожидаем код 404 и сообщение об ошибке.")
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_with_wrong_credentials(self, create_and_delete_courier, wrong_field):
        courier_data = create_and_delete_courier
        login_data = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        login_data[wrong_field] = "wrongvalue"

        with allure.step(f"Отправляем POST-запрос на авторизацию с неверным '{wrong_field}'"):
            response = requests.post(Urls.LOGIN_COURIER, json=login_data)

        with allure.step("Проверяем код ответа"):
            assert response.status_code == CourierData.login_wrong_field_response["status_code"], \
                f"Ожидался 404, получили {response.status_code}"

        with allure.step("Проверяем текст ошибки"):
            assert CourierData.login_wrong_field_response["error_text"] in response.text
