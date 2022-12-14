from http import HTTPStatus

import pytest
import requests

from links import api_url
from api.api_helpers import get_token
from constants import POSITIVE_API_CREDS, NEGATIVE_API_CREDS


@pytest.fixture()
def token():
    return get_token()


@pytest.mark.usefixtures('token')
def test_login_positive(token):
    response = requests.post(f'{api_url}login', json=POSITIVE_API_CREDS)
    print(response.json())
    assert response.json().split(' ')[0] == "Auth_token:"
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize('data', NEGATIVE_API_CREDS, ids=["empty user", "empty password", "wrong data"])
def test_login_negative(data):
    response = requests.post(f'{api_url}login', json=data)
    assert response.json()['errorMessage'] == "Wrong password."
    assert response.status_code == HTTPStatus.OK


@pytest.mark.usefixtures('token')
def test_check(token):
    data = {"token": f'{token}'}
    response = requests.post(f'{api_url}check', json=data)
    assert response.json()['Item']['username'] == 'KateFox1'


def test_entries():
    response = requests.get(f'{api_url}entries')
    items = response.json()['Items']
    assert response.status_code == HTTPStatus.OK
    assert len(items) == 9


def test_pagination():
    response = requests.post(f'{api_url}pagination', json={"id": "9"})
    items = response.json()['Items']
    assert response.status_code == HTTPStatus.OK
    assert len(items) == 6


def test_view_all_items():
    for id in range(1, 15):
        response = requests.post(f'{api_url}view', json={"id": id})
        print(response.json())
        assert response.status_code == HTTPStatus.OK
