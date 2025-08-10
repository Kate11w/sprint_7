class Urls:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = f'{MAIN_URL}/api/v1/courier'
    LOGIN_COURIER = f'{MAIN_URL}/api/v1/courier/login'
    CREATE_ORDER = f'{MAIN_URL}/api/v1/orders'
    GET_ORDERS = f'{MAIN_URL}/api/v1/orders'
    ORDER_CANCEL = f'{MAIN_URL}/api/v1/orders/cancel?track='
    DELETE_COURIER = f'{MAIN_URL}/api/v1/courier/'
