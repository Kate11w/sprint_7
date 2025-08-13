import pytest
import requests
import allure

from data import CourierData
from generators import *
from urls import Urls

class TestCourierCreate:

    @allure.title('Проверка успешного создания курьера')
    @allure.description('Запрос проверяет, что курьер создан со всеми обязательными полями')
    def test_create_courier_success(self, login_and_delete_courier):
        courier_data = login_and_delete_courier
        with allure.step("Отправляем POST-запрос на создание курьера"):
            response = requests.post(Urls.CREATE_COURIER, json=courier_data)

        with allure.step("Проверяем код ответа и тело ответа"):
            assert response.status_code == CourierData.create_courier_success_response["status_code"], \
                f"Неверный код ответа: {response.status_code}, {response.text}"
            assert response.json() == CourierData.create_courier_success_response["json_response"], \
                f"Неверное тело ответа: {response.json()}"

    @allure.title('Проверка создания двух одинаковых курьеров')
    @allure.description('Проверяем ошибку при создании курьера с уже существующими данными')
    def test_create_courier_duplicate(self, login_and_delete_courier):
        courier_data = login_and_delete_courier
        with allure.step("Создаём первого курьера"):
            requests.post(Urls.CREATE_COURIER, json=courier_data)

        with allure.step("Пробуем создать курьера с теми же данными"):
            response = requests.post(Urls.CREATE_COURIER, json=courier_data)

        with allure.step("Проверяем код ответа и текст ошибки"):
            assert response.status_code == CourierData.create_courier_duplicate_response["status_code"], \
                f"Ожидался код 409, а получен {response.status_code}"
            assert CourierData.create_courier_duplicate_response["error_text"] in response.text, \
                f"Неверный текст ошибки: {response.text}"

    @allure.title('Проверка регистрации курьера с недостающими данными')
    @allure.description('Проверяем ошибку создания курьера при отсутствии одного из обязательных полей')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_fields(self, missing_field):
        courier_data = generate_courier_data()
        courier_data.pop(missing_field)

        with allure.step(f"Отправляем POST-запрос на создание курьера без поля '{missing_field}'"):
            response = requests.post(Urls.CREATE_COURIER, json=courier_data)

        with allure.step("Проверяем код ответа и текст ошибки"):
            assert response.status_code == CourierData.create_courier_missing_field_response["status_code"], \
                f"Ожидался код 400, а получен {response.status_code}"
            assert CourierData.create_courier_missing_field_response["error_text_options"] in response.text, \
                f"Неверный текст ошибки: {response.text}"

