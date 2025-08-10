from faker import Faker
import random
import requests
from urls import Urls

faker = Faker("ru_RU")

def generate_courier_data():
    return {
        "login": f"courier_{random.randint(1000, 9999)}",
        "password": "01234",
        "firstName": faker.first_name()
    }

def login_courier_data(courier_data):
    login_response = requests.post(Urls.LOGIN_COURIER, json={
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    return login_response


def delete_courier(login_response):
    courier_id = login_response.get("id")
    requests.delete(f"{Urls.CREATE_COURIER}/{courier_id}")





