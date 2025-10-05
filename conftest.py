import pytest
import requests
from data import *

@pytest.fixture(scope='function')
def user_generate():
    user = UserGeneratedData.correctly_generated
    yield user
    user_login = UserGeneratedData.login_data[0]
    login_result = requests.post(f'{Url.main_url}{Url.login_user}', data = user_login)
    token = login_result.json()['accessToken']
    headers = {'Authorization': token}
    requests.delete(f'{Url.main_url}{Url.delete_user}', headers=headers)

@pytest.fixture(scope='function')
def user_generate_and_create():
    user = UserGeneratedData.correctly_generated
    requests.post(f'{Url.main_url}{Url.create_user}', json = user)
    user_login = UserGeneratedData.login_data
    yield user_login
    login_result = requests.post(f'{Url.main_url}{Url.login_user}', data = user_login[0])
    token = login_result.json()["accessToken"]
    headers = {'Authorization': token}
    requests.delete(f'{Url.main_url}{Url.delete_user}', headers=headers)

@pytest.fixture(scope='function')
def user_generate_create_and_login():
    user = UserGeneratedData.correctly_generated
    requests.post(f'{Url.main_url}{Url.create_user}', data = user)
    user_login = UserGeneratedData.login_data
    login_result = requests.post(f'{Url.main_url}{Url.login_user}', data = user_login[0])
    token = login_result.json()["accessToken"]
    yield token
    headers = {'Authorization': token}
    requests.delete(f'{Url.main_url}{Url.delete_user}', headers=headers)

