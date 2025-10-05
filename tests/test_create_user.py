import requests
import pytest
import allure
from data import *

class TestCreateNewUser:

    @allure.title('Тестируем успешное создание нового пользователя. Ручка /v1/user')
    def test_create_user_success(self, user_generate):
        registration_result = requests.post(f'{Url.main_url}{Url.create_user}', json = user_generate)
        assert registration_result.status_code == ResponseCodes.ok and Responses.success in str(registration_result.json())

    @allure.title('Тестируем ошибку повторного создания пользователя с теми же данными. Ручка /v1/user')
    def test_create_user_duplicate(self, user_generate):
        registration1_result = requests.post(f'{Url.main_url}{Url.create_user}', json = user_generate)
        registration2_result = requests.post(f'{Url.main_url}{Url.create_user}', json = user_generate)
        assert registration1_result.status_code == ResponseCodes.ok and registration2_result.status_code == ResponseCodes.forbidden and registration2_result.json() == Responses.user_already_exists
    
    @allure.title('Тестируем ошибку создания нового пользователя с неполными данными. Ручка /v1/user')
    @pytest.mark.parametrize('generated_user_missing_data', UserGeneratedData.insufficient_params)
    def test_create_user_missing_data(self, generated_user_missing_data):
        registration_result = requests.post(f'{Url.main_url}{Url.create_user}', json = generated_user_missing_data)
        assert registration_result.status_code == ResponseCodes.forbidden and registration_result.json() == Responses.user_missing_data
