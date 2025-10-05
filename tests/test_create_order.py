import requests
import pytest
import allure
from data import *
from urls import *

class TestCreateOrder:

    @allure.title('Тестируем создание заказа с авторизацией.')
    def test_authorized_order_create(self, user_generate_create_and_login):
        headers = {'Authorization': user_generate_create_and_login}
        payload = OrderGeneratedData.order_data
        with allure.step(f'POST запрос к {Url.create_order} с данными {payload}'):
            order_create_result = requests.post(f'{Url.main_url}{Url.create_order}', json = payload, headers = headers)
        assert order_create_result.status_code == ResponseCodes.ok and Responses.success in str(order_create_result.json())

    @allure.title('Тестируем создание заказа без авторизации.')
    def test_unauthorized_order_create(self):
        payload = OrderGeneratedData.order_data
        with allure.step(f'POST запрос к {Url.create_order} с данными {payload}'):
            order_create_result = requests.post(f'{Url.main_url}{Url.create_order}', json = payload)
        assert order_create_result.status_code == ResponseCodes.redirect and Responses.new_location in str(order_create_result.headers)

    @allure.title('Тестируем создание заказа без ингредиентов.')
    def test_empty_order_create(self, user_generate_create_and_login):
        headers = {'Authorization': user_generate_create_and_login}
        payload = OrderGeneratedData.empty_order_data
        with allure.step(f'POST запрос к {Url.create_order} с данными {payload}'):
            order_create_result = requests.post(f'{Url.main_url}{Url.create_order}', json = payload, headers = headers)
        assert order_create_result.status_code == ResponseCodes.bad_request and Responses.fail in str(order_create_result.json())

    @allure.title('Тестируем создание заказа с неверным хэшем ингредиентов.')
    def test_wrong_hash_order_create(self, user_generate_create_and_login):
        headers = {'Authorization': user_generate_create_and_login}
        payload = OrderGeneratedData.incorrect_order_data
        with allure.step(f'POST запрос к {Url.create_order} с данными {payload}'):
            order_create_result = requests.post(f'{Url.main_url}{Url.create_order}', json = payload, headers = headers)
        assert order_create_result.status_code == ResponseCodes.server_error
