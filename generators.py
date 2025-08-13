from faker import Faker
import random


faker = Faker("ru_RU")

def generate_courier_data():
    return {
        "login": f"courier_{random.randint(1000, 9999)}",
        "password": "01234",
        "firstName": faker.first_name()
    }
