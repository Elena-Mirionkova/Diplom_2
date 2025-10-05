import pytest
import requests
import allure
from data import *
from urls import *

@pytest.fixture(scope='function')
def user_generate():
    user = UserGeneratedData.correctly_generated
    yield user
    user_login = UserGeneratedData.login_data[0]
    with allure.step(f'POST запрос к {Url.login_user} с данными {user_login}'):
        login_result = requests.post(f'{Url.main_url}{Url.login_user}', data = user_login)
    token = login_result.json()['accessToken']
    headers = {'Authorization': token}
    with allure.step(f'DELETE запрос к {Url.delete_user}'):
        requests.delete(f'{Url.main_url}{Url.delete_user}', headers=headers)

@pytest.fixture(scope='function')
def user_generate_and_create():
    user = UserGeneratedData.correctly_generated
    with allure.step(f'POST запрос к {Url.create_user} с данными {user}'):
        requests.post(f'{Url.main_url}{Url.create_user}', json = user)
    user_login = UserGeneratedData.login_data[0]
    yield user
    with allure.step(f'POST запрос к {Url.login_user} с данными {user_login} для обновления токена'):
        login_result = requests.post(f'{Url.main_url}{Url.login_user}', data = user_login)
    token = login_result.json()["accessToken"]
    headers = {'Authorization': token}
    with allure.step(f'DELETE запрос к {Url.delete_user}'):
        requests.delete(f'{Url.main_url}{Url.delete_user}', headers=headers)

@pytest.fixture(scope='function')
def user_generate_create_and_login():
    user = UserGeneratedData.correctly_generated
    with allure.step(f'POST запрос к {Url.login_user} с данными {user}'):
        requests.post(f'{Url.main_url}{Url.create_user}', data = user)
    user_login = UserGeneratedData.login_data[0]
    with allure.step(f'POST запрос к {Url.login_user} с данными {user_login}'):
        login_result = requests.post(f'{Url.main_url}{Url.login_user}', data = user_login)
    token = login_result.json()["accessToken"]
    yield token
    headers = {'Authorization': token}
    with allure.step(f'DELETE запрос к {Url.delete_user}'):
        requests.delete(f'{Url.main_url}{Url.delete_user}', headers=headers)

