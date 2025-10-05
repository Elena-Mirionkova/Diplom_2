import requests
import pytest
import allure
from data import *

class TestLoginUser:

    @allure.title('Тестируем логин пользователя. Ручка /v1/user/login')
    def test_login_user_success(self, user_generate_and_create):
        login_result = requests.post(f'{Url.main_url}{Url.login_user}', json = user_generate_and_create[0])
        assert login_result.status_code == ResponseCodes.ok and Responses.success in str(login_result.json())

    @allure.title('Тестируем ошибку входа с неправильным логином. Ручка /v1/user/login')
    def test_login_user_wrong_login(self, user_generate_and_create):
        login_result = requests.post(f'{Url.main_url}{Url.login_user}', json = user_generate_and_create[1])
        assert login_result.status_code == ResponseCodes.unauthorized and login_result.json() == Responses.login_missing_data

    @allure.title('Тестируем ошибку входа с неправильным паролем. Ручка /v1/user/login')
    def test_login_user_wrong_password(self, user_generate_and_create):
        login_result = requests.post(f'{Url.main_url}{Url.login_user}', json = user_generate_and_create[2])
        assert login_result.status_code == ResponseCodes.unauthorized and login_result.json() == Responses.login_missing_data