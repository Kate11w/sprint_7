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


