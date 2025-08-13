from faker import Faker
import random

faker = Faker("ru_RU")

class OrderData:
    order_data = {
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
        "address": faker.address().replace("\n", ", "),
        "metroStation": random.randint(1, 15),
        "phone": faker.phone_number(),
        "rentTime": random.randint(1, 7),
        "deliveryDate": faker.date_this_year().isoformat(),
        "comment": faker.sentence(nb_words=5)
}

    scooter_color = [["BLACK"], ["GREY"], ["BLACK", "GREY"], None]

    order_create_status = {
        "status_code": 201,
        "key_in_response": "track"
    }

    order_expected_response = {
        "status_code": 200,
        "key_in_response": "orders"
    }

class CourierData:
    empty_fields = ["login", "password"]

    wrong_fields = ["login", "password"]

    login_success_response = {
        "status_code": 200,
        "key_in_response": "id"
    }

    login_empty_field_response = {
        "status_code": 400,
        "error_text": "Недостаточно данных для входа"
    }

    login_wrong_field_response = {
        "status_code": 404,
        "error_text": "Учетная запись не найдена"
    }

    missing_required_fields = ["login", "password"]

    create_courier_success_response = {
        "status_code": 201,
        "json_response": {"ok": True}
    }

    create_courier_duplicate_response = {
        "status_code": 409,
        "error_text": "Этот логин уже используется"
    }

    create_courier_missing_field_response = {
        "status_code": 400,
        "error_text_options": "Недостаточно данных для создания учетной записи"
    }