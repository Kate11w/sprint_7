import pytest
import requests
import allure

from urls import Urls
from generators import *

class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверка "id" курьера при авторизации')
    def test_success_login_courier(self):
        courier_data = generate_courier_data()
        response = requests.post(Urls.CREATE_COURIER, json=courier_data)

        login_response = login_courier_data(courier_data)
        assert login_response.status_code == 200, f"Не удалось авторизоваться: {login_response.text}"
        assert "id" in login_response.json(), "В ответе нет id"

        delete_courier(login_response.json())


    @allure.title('Ошибка аутентификации при пустом значении обязательного поля')
    @allure.description('Передаем пустое значение в login или password. '
                        'Ожидаем код 400 и сообщение об ошибке.')
    @pytest.mark.parametrize("empty_field", ["login", "password"])
    def test_login_empty_required_fields(self, empty_field):
        courier_data = generate_courier_data()
        response = requests.post(Urls.CREATE_COURIER, json=courier_data)
        login_data = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        login_data[empty_field] = ""
        response = requests.post(Urls.LOGIN_COURIER, json=login_data)
        assert response.status_code == 400, f"Ожидался 400, получили {response.status_code}"
        assert "Недостаточно данных" in response.text, \
            f"Ожидалось сообщение 'Недостаточно данных', получили {response.text}"

        login_response = login_courier_data(courier_data)
        delete_courier(login_response.json())


    @allure.title("Ошибка при неправильном логине или пароле")
    @pytest.mark.parametrize("login,password", [
        ("wronglogin", "01234"),
        ("correctlogin", "wrongpass")
    ])
    def test_login_with_wrong_credentials(self, login, password):
        courier_data = generate_courier_data()
        response = requests.post(Urls.CREATE_COURIER, json=courier_data)

        if login == "correctlogin":
            login = courier_data["login"]
        response = requests.post(Urls.LOGIN_COURIER, json={"login": login, "password": password})

        assert response.status_code == 404, f"Ожидался 404, получили {response.status_code}"
        assert "не найдена" in response.text.lower()

        login_response = login_courier_data(courier_data)
        delete_courier(login_response.json())
