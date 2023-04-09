import requests
from helpers import *
import pytest


@pytest.mark.parametrize('url', ['https://reqres.in/api/users?page=2'])
def test_list_users(url):
    r = requests.get(url)
    assert r.status_code == 200
    jsonData = r.json()
    assert jsonData['data']


@pytest.mark.parametrize('url', ['https://reqres.in/api/users/2', 'https://reqres.in/api/users/3'])
def test_single_user(url):
    r = requests.get(url)
    assert r.status_code == 200
    jsonData = r.json()
    assert is_id(jsonData['data']['id'])
    assert is_email(jsonData['data']['email'])
    assert is_string(jsonData['data']['first_name'])
    assert is_string(jsonData['data']['last_name'])
    assert is_url(jsonData['data']['avatar'])


@pytest.mark.parametrize('url', ['https://reqres.in/api/users/23', 'https://reqres.in/api/users/24'])
def test_user_not_exist(url):
    r = requests.get(url)
    assert r.status_code == 404


def test_list_resource():
    r = requests.get('https://reqres.in/api/unknown')
    assert r.status_code == 200


@pytest.mark.parametrize('url', ['https://reqres.in/api/unknown/2', 'https://reqres.in/api/unknown/3'])
def test_single_resource(url):
    r = requests.get(url)
    assert r.status_code == 200
    jsonData = r.json()
    assert is_id(jsonData['data']['id'])
    assert is_string(jsonData['data']['name'])
    assert is_integer(jsonData['data']['year'])
    assert is_string(jsonData['data']['color'])
    assert is_string(jsonData['data']['pantone_value'])


@pytest.mark.parametrize('url', ['https://reqres.in/api/unknown/23', 'https://reqres.in/api/unknown/24'])
def test_single_resource_not_exist(url):
    r = requests.get(url)
    assert r.status_code == 404


@pytest.mark.parametrize('name, job', [('test_user', 'test_job')])
def test_create_user(name, job):
    r = requests.post('https://reqres.in/api/users', data={'name': name, 'job': job})
    assert r.status_code == 201
    jsonData = r.json()
    assert is_string(jsonData['id'])
    assert is_string(jsonData['name'])
    assert is_string(jsonData['job'])
    assert is_string(jsonData['createdAt'])


@pytest.mark.parametrize('name, job', [('test_user', 'test_job')])
def test_update_user_put(name, job):
    r = requests.put('https://reqres.in/api/users/2', data={'name': name, 'job': job})
    assert r.status_code == 200
    jsonData = r.json()
    assert is_string(jsonData['name'])
    assert is_string(jsonData['job'])
    assert is_string(jsonData['updatedAt'])


@pytest.mark.parametrize('name, job', [('test_user', 'test_job')])
def test_update_user_patch(name, job):
    r = requests.patch('https://reqres.in/api/users/2', data={'name': name, 'job': job})
    assert r.status_code == 200
    jsonData = r.json()
    assert is_string(jsonData['name'])
    assert is_string(jsonData['job'])
    assert is_string(jsonData['updatedAt'])


def test_delete_user():
    r = requests.patch('https://reqres.in/api/users/2')
    assert r.status_code == 200


@pytest.mark.parametrize('email, password', [('eve.holt@reqres.in', 'pistol')])
def test_register_user(email, password):
    r = requests.post('https://reqres.in/api/register', data={'email': email, 'password': password})
    assert r.status_code == 200


def test_register_user_unsuccessful():
    r = requests.post('https://reqres.in/api/register', data={'email': 'test_email@mail.ru'})
    assert r.status_code == 400


@pytest.mark.parametrize('email, password', [('eve.holt@reqres.in', 'cityslicka')])
def test_login_user(email, password):
    r = requests.post('https://reqres.in/api/register', data={'email': email, 'password': password})
    assert r.status_code == 200


def test_login_user_unsuccessful():
    r = requests.post('https://reqres.in/api/register', data={'email': 'eve.holt@reqres.in'})
    assert r.status_code == 400


def test_delayed_response():
    r = requests.get('https://reqres.in/api/users?delay=2')
    assert r.status_code == 200
