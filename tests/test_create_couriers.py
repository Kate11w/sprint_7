import pytest
import requests
import allure

from generators import *
from urls import Urls

class TestCourierCreate:
    @allure.title('Проверка успешного создания курьера')
    @allure.description('Запрос проверяет, что курьер создан со всеми обязательными полями')
    def test_create_courier_success(self):
        courier_data = generate_courier_data()
        response = requests.post(Urls.CREATE_COURIER, json=courier_data)
        assert response.status_code == 201, f"Неверный код ответа: {response.status_code}, {response.text}"
        assert response.json() == {"ok": True}, f"Неверное тело ответа: {response.json()}"

        login_response = login_courier_data(courier_data)
        delete_courier(login_response.json())


    @allure.title('Проверка создания двух одинаковых курьеров')
    @allure.description('Проверяем ошибку при создании курьера с уже существующими данными')
    def test_create_courier_duplicate(self):
        courier_data = generate_courier_data()
        requests.post(Urls.CREATE_COURIER, json=courier_data)
        response = requests.post(Urls.CREATE_COURIER, json=courier_data)
        assert response.status_code == 409, f"Ожидался код 409, а получен {response.status_code}"
        assert "Этот логин уже используется" in response.text, f"Неверный текст ошибки: {response.text}"

        login_response = login_courier_data(courier_data)
        delete_courier(login_response.json())


    @allure.title('Проверка регистрации курьера с недостающими данными')
    @allure.description('Проверяем ошибку создания курьера при отсутствии одного из обязательных полей')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_fields(self, missing_field):
        courier_data = generate_courier_data()
        courier_data.pop(missing_field)
        response = requests.post(Urls.CREATE_COURIER, json=courier_data)
        assert response.status_code == 400, f"Ожидался код 400, а получен {response.status_code}"
        assert "Недостаточно данных" in response.text or "нужно передать" in response.text, f"Неверный текст ошибки: {response.text}"

