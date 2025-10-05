import requests
import pytest
import allure
from data import *
from urls import *

class TestCreateNewUser:

    @allure.title('Тестируем успешное создание нового пользователя.')
    def test_create_user_success(self, user_generate):
        with allure.step(f'POST запрос к {Url.create_user} с данными {user_generate}'):
            registration_result = requests.post(f'{Url.main_url}{Url.create_user}', json = user_generate)
        assert registration_result.status_code == ResponseCodes.ok and Responses.success in str(registration_result.json())

    @allure.title('Тестируем ошибку повторного создания пользователя с теми же данными.')
    def test_create_user_duplicate(self, user_generate_and_create):
        with allure.step(f'POST запрос к {Url.create_user} с данными {user_generate_and_create}'):
            registration_result = requests.post(f'{Url.main_url}{Url.create_user}', json = user_generate_and_create)
        assert registration_result.status_code == ResponseCodes.forbidden and registration_result.json() == Responses.user_already_exists
    
    @allure.title('Тестируем ошибку создания нового пользователя с неполными данными.')
    @pytest.mark.parametrize('generated_user_missing_data', UserGeneratedData.insufficient_params)
    def test_create_user_missing_data(self, generated_user_missing_data):
        with allure.step(f'POST запрос к {Url.create_user} с данными {generated_user_missing_data}'):
            registration_result = requests.post(f'{Url.main_url}{Url.create_user}', json = generated_user_missing_data)
        assert registration_result.status_code == ResponseCodes.forbidden and registration_result.json() == Responses.user_missing_data
