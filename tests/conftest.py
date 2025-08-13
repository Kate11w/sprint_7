import pytest
import requests

from generators import generate_courier_data
from urls import Urls


@pytest.fixture()
def create_and_delete_courier():
    courier_data = generate_courier_data()
    requests.post(Urls.CREATE_COURIER, json=courier_data)
    yield courier_data
    login_response = requests.post(Urls.LOGIN_COURIER, data=courier_data)
    courier_id = login_response.json()['id']
    requests.delete(f"{Urls.CREATE_COURIER}/{courier_id}")

@pytest.fixture()
def login_and_delete_courier():
    courier_data = generate_courier_data()
    yield courier_data
    login_response = requests.post(Urls.LOGIN_COURIER, data=courier_data)
    courier_id = login_response.json()['id']
    requests.delete(f"{Urls.CREATE_COURIER}/{courier_id}")

@pytest.fixture()
def order_delete():
    track = {}
    yield track
    requests.put(f"{Urls.ORDER_CANCEL}{track['track']}")
