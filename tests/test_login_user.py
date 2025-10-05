import requests
import pytest
import allure
from data import *
from urls import *

class TestLoginUser:

    @allure.title('Тестируем логин пользователя.')
    def test_login_user_success(self, user_generate_and_create):
        login_data = user_generate_and_create.copy()
        del login_data["name"]
        with allure.step(f'POST запрос к {Url.login_user} с данными {login_data}'):
            login_result = requests.post(f'{Url.main_url}{Url.login_user}', json = login_data)
        assert login_result.status_code == ResponseCodes.ok and Responses.success in str(login_result.json())

    @allure.title('Тестируем ошибку входа с неправильным данными.')
    @pytest.mark.parametrize('dataset_id', [1, 2])
    def test_login_user_wrong_login(self, user_generate_and_create, dataset_id):
        with allure.step(f'POST запрос к {Url.login_user} с данными {UserGeneratedData.login_data[dataset_id]}'):
            login_result = requests.post(f'{Url.main_url}{Url.login_user}', json = UserGeneratedData.login_data[dataset_id])
        assert login_result.status_code == ResponseCodes.unauthorized and login_result.json() == Responses.login_missing_data
